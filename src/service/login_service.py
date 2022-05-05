import json
import time

import requests
from envs import env
from jose import jwt, jwk
from jose.utils import base64url_decode
import logging

from src.config.cognito_config import CognitoConfig
from src.exception.login_exception import LoginException
from src.exception.logout_exception import LogoutException
from src.exception.validation_token_exception import ValidationTokenException
from src.utils.login_validate_request import LoginValidateRequest


class LoginService:

    def __init__(self, event):
        self.event = event
        self.connection = CognitoConfig().get_connection_cognito()
        self.validation = LoginValidateRequest()

    def sign_in(self):
        try:
            if (type(self.event['body']) == dict):
                body = self.event['body']
            else:
                body = json.loads(self.event['body'])

            if (type(self.event['headers']) == dict):
                header = self.event['headers']
            else:
                header = json.loads(self.event['headers'])

            self.validation.validate_header_login(header)
            self.validation.validate_body_login(body)

            response = self.connection.initiate_auth(
                AuthFlow='USER_PASSWORD_AUTH',
                AuthParameters={
                    'USERNAME': body['username'],
                    'PASSWORD': body['password']
                },
                ClientId=header['client_id']
            )

            if response['ChallengeName'] == 'MFA_SETUP':
                return {"message": "Necessário cadastrar um MFA para prosseguir", "session": response['Session']}
            if response['ChallengeName'] == 'SOFTWARE_TOKEN_MFA':
                return {"message": "Necessário validar o MFA para prosseguir", "session": response['Session']}

            return {"message": "Recurso não mapeado para o MFA"}

        except Exception as error:
            print(error)
            raise LoginException("Não foi possível realizar o login " + str(error))

    def validateMFA(self):
        try:
            if (type(self.event['body']) == dict):
                body = self.event['body']
            else:
                body = json.loads(self.event['body'])

            if (type(self.event['headers']) == dict):
                header = self.event['headers']
            else:
                header = json.loads(self.event['headers'])

            self.validation.validate_header_mfa(header)
            self.validation.validate_body_mfa(body)

            response = self.connection.respond_to_auth_challenge(
                ClientId=header['client_id'],
                ChallengeName='SOFTWARE_TOKEN_MFA',
                Session=header['session'],
                ChallengeResponses={
                    'USERNAME': body['username'],
                    'SOFTWARE_TOKEN_MFA_CODE': body['software_token_mfa_code']
                }
            )

            return response

        except Exception as error:
            print(error)
            raise LoginException("Falha na validação do MFA para realizar o login " + str(error))

    def sign_out(self):
        try:
            if (type(self.event['headers']) == dict):
                header = self.event['headers']
            else:
                header = json.loads(self.event['headers'])

            self.validation.validate_header_logout(header)

            self.connection.global_sign_out(
                AccessToken=header['authorization']
            )

            return {"message": "Logout realizado com sucesso"}

        except Exception as error:
            print(error)
            raise LogoutException("Erro ao realizar logout para o usuário " + str(error))

    def validation_token(self):
        try:
            if (type(self.event['headers']) == dict):
                header = self.event['headers']
            else:
                header = json.loads(self.event['headers'])

            self.validation.validate_header_validation_token(header)

            token = header['authorization']
            app_client_id = header['client_id']

            if not self.obter_usuario(token):
                print('Token was rovoked')
                raise Exception("Acesso não autorizado")

            keys = self.get_keys().get('keys')

            # get the kid from the headers prior to verification
            headers = jwt.get_unverified_headers(token)
            kid = headers['kid']
            # search for the kid in the downloaded public keys
            key_index = -1
            for i in range(len(keys)):
                if kid == keys[i]['kid']:
                    key_index = i
                    break
            if key_index == -1:
                print('Public key not found in jwks.json')
                raise Exception("Acesso não autorizado")
            # construct the public key
            public_key = jwk.construct(keys[key_index])
            # get the last two sections of the token,
            # message and signature (encoded in base64)
            message, encoded_signature = str(token).rsplit('.', 1)
            # decode the signature
            decoded_signature = base64url_decode(encoded_signature.encode('utf-8'))
            # verify the signature
            if not public_key.verify(message.encode("utf8"), decoded_signature):
                print('Signature verification failed')
                raise Exception("Acesso não autorizado")
            print('Signature successfully verified')
            # since we passed the verification, we can now safely
            # use the unverified claims
            claims = jwt.get_unverified_claims(token)
            # additionally we can verify the token expiration
            if time.time() > claims['exp']:
                print('Token is expired')
                raise Exception("Token Expirado")
            # and the Audience  (use claims['client_id'] if verifying an access token)
            if claims['client_id'] != app_client_id:
                print('Token was not issued for this audience')
                raise Exception("Acesso não autorizado")
            # now we can use the claims
            print(claims)

            return {"message": "Acesso autorizado"}

        except Exception as error:
            print(error)
            raise ValidationTokenException(str(error))

    def obter_usuario(self, access_token):
        try:
            self.connection.get_user(
                AccessToken=access_token
            )
            return True
        except Exception as error:
            print(error)
            return False

    def get_keys(self):
        try:
            return self.pool_jwk
        except AttributeError:
            # Check for the dictionary in environment variables.
            pool_jwk_env = env('COGNITO_JWKS', {}, var_type='dict')
            if len(pool_jwk_env.keys()) > 0:
                self.pool_jwk = pool_jwk_env
                return self.pool_jwk
            # If it is not there use the requests library to get it
            self.pool_jwk = requests.get(
                'https://cognito-idp.{}.amazonaws.com/{}/.well-known/jwks.json'.format(
                    'us-east-1', 'us-east-1_dIRX8NWV2'
                )).json()
            return self.pool_jwk

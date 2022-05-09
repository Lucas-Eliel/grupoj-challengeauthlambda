import json

from src.config.cognito_config import CognitoConfig
from src.exception.forgot_password_exception import ForgotPasswordException
from src.utils.esqueceu_senha_validate_request import EsqueceuSenhaValidateRequest


class ForgotPasswordService:

    def __init__(self, event):
        self.event = event
        self.connection = CognitoConfig().get_connection_cognito()
        self.validation = EsqueceuSenhaValidateRequest()

    def forgot_password(self):
        try:
            if (type(self.event['body']) == dict):
                body = self.event['body']
            else:
                body = json.loads(self.event['body'])

            if (type(self.event['headers']) == dict):
                header = self.event['headers']
            else:
                header = json.loads(self.event['headers'])

            self.validation.validate_body(body)
            self.validation.validate_header(header)

            self.connection.forgot_password(
                ClientId=header['client_id'],
                Username=body['username'],
            )

            return {"message": "Processo de esqueci minha senha iniciado. Foi enviado um código de verificação para seu email " + str(body['username'])}

        except Exception as error:
            print(error)
            raise ForgotPasswordException("Houve um problema no processo de esqueci minha senha: " + str(error))

    def confirm_forgot_password(self):
        try:
            if (type(self.event['body']) == dict):
                body = self.event['body']
            else:
                body = json.loads(self.event['body'])

            if (type(self.event['headers']) == dict):
                header = self.event['headers']
            else:
                header = json.loads(self.event['headers'])

            self.validation.validate_body_confirmation(body)
            self.validation.validate_header(header)

            self.connection.confirm_forgot_password(
                ClientId=header['client_id'],
                Username=body['username'],
                ConfirmationCode=body['confirmation_code'],
                Password=body['password'],
            )

            return {"message": "Processo de esqueci minha senha completo"}

        except Exception as error:
            print(error)
            raise ForgotPasswordException("Houve um problema no processo de confirmar o esqueci minha senha: " + str(error))
import boto3
import datetime
from jose import jwt, jwk
from envs import env
import requests
from jose.utils import base64url_decode
import time
import urllib.request
import json

def get_connection_cognito():
    return boto3.client('cognito-idp', region_name='us-east-1', aws_access_key_id='AKIARK3PD7LHNAHHOJNL', aws_secret_access_key='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')


class LoginRepository:

    def __init__(self):
        self.connection = get_connection_cognito()

    def login(self):
        try:
            return self.connection.initiate_auth(
                AuthFlow='USER_PASSWORD_AUTH',
                AuthParameters={
                    'USERNAME': 'lucaseliel.study@gmail.com',
                    'PASSWORD': 'Abc@123'
                },
                ClientId='20tfh1piiu8pja1khmjuve6ra0',
            )
        except Exception as error:
            print(error)

    def validaLoginMFA(self):
        try:
            return self.connection.respond_to_auth_challenge(
                ClientId='20tfh1piiu8pja1khmjuve6ra0',
                ChallengeName='SOFTWARE_TOKEN_MFA',
                Session='AYABeKoSfit4rGefvNew58vZ4N8AHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHiG0oCCDoro3IaeecGyxCZJOVZkUqttbPnF4J7Ar-5byAFsD69OdYizoKyqPv857G5vAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMiJ2FhAB4I9dnvxAxAgEQgDt4qOoU75ShcMiAZD_aqENYCbDl6ivrYuDP3ocrt0_64pV_6y6Br-0y8XzxiFAFkMTVHJZ4_vy3yM9UEwIAAAAADAAAEAAAAAAAAAAAAAAAAADB2YVdicesQ12VuK4DDjBU_____wAAAAEAAAAAAAAAAAAAAAEAAAEBuChU9rjsqqKAYekXtAcBXqvMF7CsINmoSt8HDMdzfEz33rb9l7aCZpG0ovUoGd8OU6Z4Ap8sMoqyhQNPw9hBd4yGeT2edPzE37nlwsXblbJW_7a0eyjc4fGK3O1lebQO2pdQl17qMxPqomNsOpMRjLZ1gfieVqfhZPIzEXQl4sD4Xb04igW0E6SfCzUsl0i0ckgjGBCWp9DJJi1cm5Wy8yw_W83f7KCXp5lKn8v0KBlcF-zlgP03H9QlVfZrSQykhC-4GM_S_bgmHDNVroCCi0KPHe9mTN-0QLXE_Ivn5L-ziJ3hcAU2r_9h831d_0nq7-xkeBrcG3jHAPeV349vbGyyXY-eD2KOtB3_h7WfKWab',
                ChallengeResponses={
                    'USERNAME': 'lucaseliel.study@gmail.com',
                    'SOFTWARE_TOKEN_MFA_CODE': '288998'
                }
            )
        except Exception as error:
            print(error)

    def get_keys(self):
        try:
            return self.pool_jwk
        except AttributeError:
            #Check for the dictionary in environment variables.
            pool_jwk_env = env('COGNITO_JWKS', {}, var_type='dict')
            if len(pool_jwk_env.keys()) > 0:
                self.pool_jwk = pool_jwk_env
                return self.pool_jwk
            #If it is not there use the requests library to get it
            self.pool_jwk = requests.get(
                'https://cognito-idp.{}.amazonaws.com/{}/.well-known/jwks.json'.format(
                    'us-east-1','us-east-1_dIRX8NWV2'
                )).json()
            return self.pool_jwk

    def sair_token(self):
        try:
            return self.connection.global_sign_out(
                AccessToken='eyJraWQiOiJ6cmtkZlpkVWdxVnRmR2UzZWZUNU5RdU9vaXZjejF2aFwvN1wvYm5PQlNjVGM9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJjYTg0MjAzOC0yNzAxLTQyZWMtYWFkYS01OGRiNTNjNWVkMTMiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9kSVJYOE5XVjIiLCJjbGllbnRfaWQiOiIyMHRmaDFwaWl1OHBqYTFraG1qdXZlNnJhMCIsIm9yaWdpbl9qdGkiOiIwYWYyNmNlYy04ZjQ0LTQ5NTEtYjBmZS0xODQ5YjgwYWUxNDQiLCJldmVudF9pZCI6IjUwMWRmN2RlLTY3MmEtNDZiZC05OGFiLWZkYzVhZDM5MzBjZCIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2NTE1MzAwMjMsImV4cCI6MTY1MTUzMzYyMywiaWF0IjoxNjUxNTMwMDIzLCJqdGkiOiJiZjQyNWE0ZC0wYjhmLTQ5YzYtYmVkOS02OWEwMmYyMjExYmQiLCJ1c2VybmFtZSI6ImNhODQyMDM4LTI3MDEtNDJlYy1hYWRhLTU4ZGI1M2M1ZWQxMyJ9.QLF6upp43S7i1dTOLARedfyF1jj0DKNrDNCtvN-U8iPVB4AlLRjrz4XfDEyYD0rqOtwZW12unsSrYQ8HSEeZchQBW025MoMCPWpUCq2tilj_Epn3_azV7ol1F-AI4GmVAzM-8ubdykeK9nyErMH8kmUDuHFjKVFRaCuphR7MUaN9ePI6Sel4GDgzCngvk8jh1Dudzu_PepUrJogXLYPRUSnQJdUnPxSxrdRa3jhnkSpQnq7amBdONtW8ci5LK_pFsvewMmGCw-Bzu4BGGNYKvAaotmNqVVJNaOif4JF_OtbkqSBAezR92DyR-_jFNLKZZBfldWJPMvtZeWq5Np28IA'
            )
        except Exception as error:
            print(error)

    def verificacao_token(self):
        try:
            token = 'eyJraWQiOiJ6cmtkZlpkVWdxVnRmR2UzZWZUNU5RdU9vaXZjejF2aFwvN1wvYm5PQlNjVGM9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJjYTg0MjAzOC0yNzAxLTQyZWMtYWFkYS01OGRiNTNjNWVkMTMiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9kSVJYOE5XVjIiLCJjbGllbnRfaWQiOiIyMHRmaDFwaWl1OHBqYTFraG1qdXZlNnJhMCIsIm9yaWdpbl9qdGkiOiIwYWYyNmNlYy04ZjQ0LTQ5NTEtYjBmZS0xODQ5YjgwYWUxNDQiLCJldmVudF9pZCI6IjUwMWRmN2RlLTY3MmEtNDZiZC05OGFiLWZkYzVhZDM5MzBjZCIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2NTE1MzAwMjMsImV4cCI6MTY1MTUzMzYyMywiaWF0IjoxNjUxNTMwMDIzLCJqdGkiOiJiZjQyNWE0ZC0wYjhmLTQ5YzYtYmVkOS02OWEwMmYyMjExYmQiLCJ1c2VybmFtZSI6ImNhODQyMDM4LTI3MDEtNDJlYy1hYWRhLTU4ZGI1M2M1ZWQxMyJ9.QLF6upp43S7i1dTOLARedfyF1jj0DKNrDNCtvN-U8iPVB4AlLRjrz4XfDEyYD0rqOtwZW12unsSrYQ8HSEeZchQBW025MoMCPWpUCq2tilj_Epn3_azV7ol1F-AI4GmVAzM-8ubdykeK9nyErMH8kmUDuHFjKVFRaCuphR7MUaN9ePI6Sel4GDgzCngvk8jh1Dudzu_PepUrJogXLYPRUSnQJdUnPxSxrdRa3jhnkSpQnq7amBdONtW8ci5LK_pFsvewMmGCw-Bzu4BGGNYKvAaotmNqVVJNaOif4JF_OtbkqSBAezR92DyR-_jFNLKZZBfldWJPMvtZeWq5Np28IA'
            app_client_id = '20tfh1piiu8pja1khmjuve6ra0'

            if not self.obter_usuario(token):
                print('Token was rovoked')
                return False

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
                return False
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
                return False
            print('Signature successfully verified')
            # since we passed the verification, we can now safely
            # use the unverified claims
            claims = jwt.get_unverified_claims(token)
            # additionally we can verify the token expiration
            if time.time() > claims['exp']:
                print('Token is expired')
                return False
            # and the Audience  (use claims['client_id'] if verifying an access token)
            if claims['client_id'] != app_client_id:
                print('Token was not issued for this audience')
                return False
            # now we can use the claims
            print(claims)
            return True
        except Exception as error:
            print(error)


    def obter_usuario(self, access_token):
        try:
            self.connection.get_user(
                AccessToken=access_token
            )
            return True
        except Exception as error:
            print(error)
            return False

if __name__ == '__main__':
    resp = LoginRepository().verificacao_token()
    print(resp)

#{'ChallengeParameters': {}, 'AuthenticationResult': {'AccessToken': 'eyJraWQiOiJ6cmtkZlpkVWdxVnRmR2UzZWZUNU5RdU9vaXZjejF2aFwvN1wvYm5PQlNjVGM9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJjYTg0MjAzOC0yNzAxLTQyZWMtYWFkYS01OGRiNTNjNWVkMTMiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9kSVJYOE5XVjIiLCJjbGllbnRfaWQiOiIyMHRmaDFwaWl1OHBqYTFraG1qdXZlNnJhMCIsIm9yaWdpbl9qdGkiOiIwYWYyNmNlYy04ZjQ0LTQ5NTEtYjBmZS0xODQ5YjgwYWUxNDQiLCJldmVudF9pZCI6IjUwMWRmN2RlLTY3MmEtNDZiZC05OGFiLWZkYzVhZDM5MzBjZCIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2NTE1MzAwMjMsImV4cCI6MTY1MTUzMzYyMywiaWF0IjoxNjUxNTMwMDIzLCJqdGkiOiJiZjQyNWE0ZC0wYjhmLTQ5YzYtYmVkOS02OWEwMmYyMjExYmQiLCJ1c2VybmFtZSI6ImNhODQyMDM4LTI3MDEtNDJlYy1hYWRhLTU4ZGI1M2M1ZWQxMyJ9.QLF6upp43S7i1dTOLARedfyF1jj0DKNrDNCtvN-U8iPVB4AlLRjrz4XfDEyYD0rqOtwZW12unsSrYQ8HSEeZchQBW025MoMCPWpUCq2tilj_Epn3_azV7ol1F-AI4GmVAzM-8ubdykeK9nyErMH8kmUDuHFjKVFRaCuphR7MUaN9ePI6Sel4GDgzCngvk8jh1Dudzu_PepUrJogXLYPRUSnQJdUnPxSxrdRa3jhnkSpQnq7amBdONtW8ci5LK_pFsvewMmGCw-Bzu4BGGNYKvAaotmNqVVJNaOif4JF_OtbkqSBAezR92DyR-_jFNLKZZBfldWJPMvtZeWq5Np28IA', 'ExpiresIn': 3600, 'TokenType': 'Bearer', 'RefreshToken': 'eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.fJwdZ3n-fi3aMvDFLZjIxOwCbIhvwlymyTNWMADgAtlRo4FKMEzwO1ZN0QI-nqT7O1Vs2m056fLHUnytqi5t3jZawNFabcSXPYmEMlxsZdGU8CHkC017RLZ5wLBVFEywA32QohVwr7q_j32bs1PPG-vYFA_g9xnj3KUwytbmMu1r8gAjRuMptPfeJqHZmeDTDhWc_uNNPtsG0exQnejXF9DZP99Yeu14QIG8CTkaoZf96koygCvFROIML-OdAUoYg2tq3ltZGbVZ9xL1HITGFElLtM6lpCPRFx-lpc-mpwxS_D0s7ePKL6eSccLffA9vFsYHlZaEnyGBEFCAxXyKtA.Xuq05tL9XxecakuD.GwahF4Ny93xMJL5pi2sEt0WyEFZ9uEdXlMJNSt4WES8ttXqL_p_zQMstqgCb7ExD9B-0H6AUZAsHXKLy0DwGRwhhnvPfw1TbVP7QNpwtjZBsWXd2Qi3U9LqUrDwDguUkjaxkMIKnf95logwtOUOZv1VdBugBCOZ9qM_5uIe73NtSJF8I2lvMcHr6p3EqT9XqIIIkU2PhNDsd8CsZs6hO-8hvjZ3YRBMKzSlxWUTICUy_d5anpM3z31nEaZ0lK6r8KfxuVhTAndOiiq0imUUAvdRo57UlfLO22NNm9L9r9-n1o8lC1DJNZPN2CsOQJHZQf91pxCDoOnyjKOisAKMboE0xtAJAmqsiv3ytOwzfzJxxFWaTXyE6nbJxfHZKm_WVQyfq3imcEZJ8wpp8qOrR4JKsoNnbaXPHIll3OWcbIWmFpryHI_a0NWIm7ZAnzkpVpPBj2KFCG5FHqH4hEpEKN7zAFZ8aXff7bLX-PKCqh36bB4OCDS9mHfvUYVE9OHRFJ8yG98LBSXOVm56SRJOlLlWpzDyhkLzga4Fu-SkBoOFdhzBpcg9RMpMWWmOMYPkQHwX8Zd6znptWN-f0v7KLcNZf_smUeWBMbrV6ekUHNG6PZBWfDfEYwAEQLsRxdx-gs85r1xzK_DSN7nAZ6AtpfMClfrPRnGeLksLz6M3_HXfqz8-D5T6o0xOWENNlq0eLEyLR8hiDRxi_pcZlrX-2QnGcMAtMoq2DhOR640bg8ny7ZI8kWnfQQfhT1gETq5Zn9O1hzdwpUV8oz7URu4T3miloNL6vaiul6ltYRFspdhsRBIBbGSmgVJqW2NhZU2s5OkQZWlFn4jGZwvXoHH3H4IbgWJqWOf5afQHNyu_nlVe-i6EGD2NTEK22fBDwtiRUk7QIOaFO-HLFogl5MuYlFhjyPFDJ2pvhqXxDvFAulDX9nIuWJwDhV2EY0nvUHQS-Me-yabUyD2kDMoONnwB2tjZwoyFsJK2MT3iIVdSdKDNE7W_VQxh8rrb4jm9FLy3i-FsBfaWMip9EQEwGT-gC32PdYyDwepOgmUGsFrVp3l15hhUxphxyWrrQlUK4xswNEpG0hTS8BYicPwEW_lMEB6R8F3R0xG21iiOl7d18joP97sTd3kRpn0C34h2X2DZ1h6e73sP13GKJNZFA7p5LFxwFJrAZBXQHb7WCkwvhvq79AMgKXmBbYnFb6ze70_LCkNTgDes9EhE3-1fAjRmKxtJk0BfQhMxeezAgSXAK5rZPUSZ-oaQul-7PMNczkFlkMCC1-tIUukPSouEKByO5HWiVUI9VB3hgy6Pj8na5ZeQmf_0MwlZy3khi8lM.J62as5ND-fyh5aEfNRwCqQ', 'IdToken': 'eyJraWQiOiJ1aDdIZVI0OUFLZFFCd2Z6UU5lZVZRMkNTR1VDK1piRjdxZitvSFRLWHlRPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjYTg0MjAzOC0yNzAxLTQyZWMtYWFkYS01OGRiNTNjNWVkMTMiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYWRkcmVzcyI6eyJmb3JtYXR0ZWQiOiJSdWEgQWxmYSJ9LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9kSVJYOE5XVjIiLCJwaG9uZV9udW1iZXJfdmVyaWZpZWQiOmZhbHNlLCJjb2duaXRvOnVzZXJuYW1lIjoiY2E4NDIwMzgtMjcwMS00MmVjLWFhZGEtNThkYjUzYzVlZDEzIiwibG9jYWxlIjoiQnJhc2lsIiwibWlkZGxlX25hbWUiOiJTb3V6YSIsIm9yaWdpbl9qdGkiOiIwYWYyNmNlYy04ZjQ0LTQ5NTEtYjBmZS0xODQ5YjgwYWUxNDQiLCJhdWQiOiIyMHRmaDFwaWl1OHBqYTFraG1qdXZlNnJhMCIsImV2ZW50X2lkIjoiNTAxZGY3ZGUtNjcyYS00NmJkLTk4YWItZmRjNWFkMzkzMGNkIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2NTE1MzAwMjMsIm5hbWUiOiJKb2FvIiwicGhvbmVfbnVtYmVyIjoiKzE1NTU1NTU1NTU1IiwiZXhwIjoxNjUxNTMzNjIzLCJpYXQiOjE2NTE1MzAwMjMsImp0aSI6ImMzYzNkYjQ3LTdhMWEtNDJmOS1iZWMxLTk5NTViM2FmNDlhYiIsImVtYWlsIjoibHVjYXNlbGllbC5zdHVkeUBnbWFpbC5jb20ifQ.HfgbVWIGrUliDKsqIqpvPB6_yCYZaQItP-yP6kuGVbHB6ocpSTqApQEt67kri0X7gTOgkE4y6dCBqScC8BPHqC2ZLj3pgbGcdY-YaZm1ZxOCAVufHQgWHX6_RCDiSa7qAtIMohZw8fqUaO3DkP9jU8-Jylpnn9zPYfJJ6j9oa1gAxjldgAYhhVp9F2D4fczqaC5vOqTHu7wQWb8zuaHgEPWycVOWoYwStLjSiWmBKud6Ojv_s7aGM_9XHgya8rsK6ZPXqPaEce9Nv2cWI0Yuapo9sgjYxZc9itX3d4DwpCfqRGrUrO5FyZxdj-BdBPVV6uhGEpAXg_yxh3BoyWBsjg'}, 'ResponseMetadata': {'RequestId': 'ca92d285-fbee-4c1b-bd9f-4621fa787770', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Mon, 02 May 2022 22:20:23 GMT', 'content-type': 'application/x-amz-json-1.1', 'content-length': '4289', 'connection': 'keep-alive', 'x-amzn-requestid': 'ca92d285-fbee-4c1b-bd9f-4621fa787770'}, 'RetryAttempts': 0}}

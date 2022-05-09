from src.config.cognito_config import CognitoConfig
from src.exception.generate_qr_code_exception import GenerateQRCodeException
from src.exception.validate_qr_code_exception import ValidateQRCodeException
from src.utils.mfa_validate_request import MFAValidateRequest
import json


class MFAService:

    def __init__(self, event):
        self.event = event
        self.connection = CognitoConfig().get_connection_cognito()
        self.validation = MFAValidateRequest()

    def obterQRCode(self):
        try:
            if (type(self.event['headers']) == dict):
                header = self.event['headers']
            else:
                header = json.loads(self.event['headers'])

            self.validation.validate_header_qr_code(header)

            response = self.connection.associate_software_token(
                Session=header['session']
            )

            return {"codigo_qr_code": response['SecretCode'], "session": response['Session']}

        except Exception as error:
            print(error)
            raise GenerateQRCodeException("Erro ao gerar o codigo válido para o QRCode " + str(error))

    def verifica(self):
        try:
            if (type(self.event['body']) == dict):
                body = self.event['body']
            else:
                body = json.loads(self.event['body'])

            if (type(self.event['headers']) == dict):
                header = self.event['headers']
            else:
                header = json.loads(self.event['headers'])

            self.validation.validate_header_qr_code(header)
            self.validation.validate_body_qr_code(body)

            self.connection.verify_software_token(
                UserCode=body['user_code'],
                Session=header['session'],
                FriendlyDeviceName=body['friendly_device_name']
            )

            return {"message": "Confirmação de criação de mfa para o usuário realizada com sucesso."}

        except Exception as error:
            print(error)
            raise ValidateQRCodeException("Não foi possível ser validado o MFA criado " + str(error))
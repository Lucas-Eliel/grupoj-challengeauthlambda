import json

from src.config.cognito_config import CognitoConfig
from src.exception.create_user_exception import CreateUserException
from src.utils.cadastro_usuario_validate_request import CadastroUsuarioValidateRequest


class CadastroUsuarioService:

    def __init__(self, event):
        self.event = event
        self.connection = CognitoConfig().get_connection_cognito()
        self.validation = CadastroUsuarioValidateRequest()

    def criar(self):
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

            self.connection.sign_up(
                ClientId=header['client_id'],
                Username=body['username'],
                Password=body['password'],
                UserAttributes=[
                    {
                        'Name': 'name',
                        'Value': body['attributes']['name']
                    },
                    {
                        'Name': 'middle_name',
                        'Value': body['attributes']['middle_name']
                    },
                    {
                        'Name': 'email',
                        'Value': body['attributes']['email']
                    },
                    {
                        'Name': 'locale',
                        'Value': body['attributes']['locale']
                    },
                    {
                        'Name': 'phone_number',
                        'Value': body['attributes']['phone_number']
                    },
                    {
                        'Name': 'address',
                        'Value': body['attributes']['address']
                    }
                ]
            )

            return {"message": "O usuário foi criado com sucesso, mas para concluir o cadastro confirme o código de autenticação que foi enviado para seu email "+ str(body['attributes']['email'])}

        except Exception as error:
            print(error)
            raise CreateUserException("Não foi prossível criar o usuario " + str(error))
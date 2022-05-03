from src.config.cognito_config import CognitoConfig
from src.exception.confirmation_user_exception import ConfirmationUserException
from src.utils.confirmacao_usuario_validate_request import ConfirmacaoUsuarioValidateRequest


class ConfirmacaoUsuarioService:

    def __init__(self, event):
        self.event = event
        self.connection = CognitoConfig().get_connection_cognito()
        self.validation = ConfirmacaoUsuarioValidateRequest()

    def confirmar(self):
        try:
            body = self.event['body']

            self.validation.validate_body(body)

            self.connection.confirm_sign_up(
                ClientId=body['client_id'],
                Username=body['username'],
                ConfirmationCode=body['confirmation_code']
            )

            return {"message": "Cadastro de usuário confirmado com sucesso"}

        except Exception as error:
            print(error)
            raise ConfirmationUserException("Houve um probema ao confirmar o cadastro do usuário " + str(error))
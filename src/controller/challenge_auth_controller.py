from http import HTTPStatus

from src.exception.dynamodb_integration_exception import DynamodbIntegrationException
from src.exception.validation_request_exception import ValidationRequestException
from src.service.cadastro_usuario_service import CadastroUsuarioService
from src.service.confirmacao_usuario_service import ConfirmacaoUsuarioService
from src.utils.response_utils import ResponseUtils


class ChallengeAuthController:

    def __init__(self, event):
        self.event = event
        self.service_cadastro_usuario = CadastroUsuarioService(event)
        self.service_confirmacao_usuario = ConfirmacaoUsuarioService(event)

    def invoke(self):
        try:
            if self.event['resource'] == '/criar_usuario':
                if self.event['httpMethod'] == 'POST':
                    result = self.service_cadastro_usuario.criar()
                    return ResponseUtils.sucess(HTTPStatus.CREATED, result)
                raise ValidationRequestException("Método HTTP inválido")

            if self.event['resource'] == '/confirmar_cadastro_usuario':
                if self.event['httpMethod'] == 'POST':
                    result = self.service_confirmacao_usuario.confirmar()
                    return ResponseUtils.sucess(HTTPStatus.CREATED, result)
                raise ValidationRequestException("Método HTTP inválido")

            raise ValidationRequestException("Endpoint inválido")

        except ValidationRequestException as error:
            return ResponseUtils.error(HTTPStatus.BAD_REQUEST, error.message)

        except DynamodbIntegrationException as error:
            return ResponseUtils.error(HTTPStatus.SERVICE_UNAVAILABLE, error.message)

        except Exception as error:
            return ResponseUtils.error(HTTPStatus.INTERNAL_SERVER_ERROR, str(error))



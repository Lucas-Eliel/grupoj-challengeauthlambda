from http import HTTPStatus

from src.exception.confirmation_user_exception import ConfirmationUserException
from src.exception.create_user_exception import CreateUserException
from src.exception.forgot_password_exception import ForgotPasswordException
from src.exception.generate_qr_code_exception import GenerateQRCodeException
from src.exception.login_exception import LoginException
from src.exception.logout_exception import LogoutException
from src.exception.validate_qr_code_exception import ValidateQRCodeException
from src.exception.validation_request_exception import ValidationRequestException
from src.exception.validation_token_exception import ValidationTokenException
from src.service.cadastro_usuario_service import CadastroUsuarioService
from src.service.confirmacao_usuario_service import ConfirmacaoUsuarioService
from src.service.esqueceu_senha_service import ForgotPasswordService
from src.service.login_service import LoginService
from src.service.mfa_service import MFAService
from src.utils.response_utils import ResponseUtils


class ChallengeAuthController:

    def __init__(self, event):
        self.event = event
        self.service_cadastro_usuario = CadastroUsuarioService(event)
        self.service_confirmacao_usuario = ConfirmacaoUsuarioService(event)
        self.service_mfa = MFAService(event)
        self.service_login = LoginService(event)
        self.service_forgot = ForgotPasswordService(event)

    def invoke(self):
        try:
            if self.event['resource'] == '/usuario':
                if self.event['httpMethod'] == 'POST':
                    result = self.service_cadastro_usuario.criar()
                    return ResponseUtils.sucess(HTTPStatus.CREATED, result)
                raise ValidationRequestException("Método HTTP inválido")

            if self.event['resource'] == '/usuario_confirmacao':
                if self.event['httpMethod'] == 'POST':
                    result = self.service_confirmacao_usuario.confirmar()
                    return ResponseUtils.sucess(HTTPStatus.CREATED, result)
                raise ValidationRequestException("Método HTTP inválido")

            if self.event['resource'] == '/mfa_qr_code':
                if self.event['httpMethod'] == 'GET':
                    result = self.service_mfa.obterQRCode()
                    return ResponseUtils.sucess(HTTPStatus.CREATED, result)
                raise ValidationRequestException("Método HTTP inválido")

            if self.event['resource'] == '/mfa_qr_code_confirmacao':
                if self.event['httpMethod'] == 'POST':
                    result = self.service_mfa.verifica()
                    return ResponseUtils.sucess(HTTPStatus.CREATED, result)
                raise ValidationRequestException("Método HTTP inválido")

            if self.event['resource'] == '/sign_in':
                if self.event['httpMethod'] == 'POST':
                    result = self.service_login.sign_in()
                    return ResponseUtils.sucess(HTTPStatus.CREATED, result)
                raise ValidationRequestException("Método HTTP inválido")

            if self.event['resource'] == '/validate_mfa':
                if self.event['httpMethod'] == 'POST':
                    result = self.service_login.validateMFA()
                    return ResponseUtils.sucess(HTTPStatus.CREATED, result)
                raise ValidationRequestException("Método HTTP inválido")

            if self.event['resource'] == '/validation_token':
                if self.event['httpMethod'] == 'POST':
                    result = self.service_login.validation_token()
                    return ResponseUtils.sucess(HTTPStatus.CREATED, result)
                raise ValidationRequestException("Método HTTP inválido")

            if self.event['resource'] == '/sign_out':
                if self.event['httpMethod'] == 'POST':
                    result = self.service_login.sign_out()
                    return ResponseUtils.sucess(HTTPStatus.CREATED, result)
                raise ValidationRequestException("Método HTTP inválido")

            if self.event['resource'] == '/forgot_password':
                if self.event['httpMethod'] == 'POST':
                    result = self.service_forgot.forgot_password()
                    return ResponseUtils.sucess(HTTPStatus.CREATED, result)
                raise ValidationRequestException("Método HTTP inválido")

            if self.event['resource'] == '/confirmation_forgot_password':
                if self.event['httpMethod'] == 'POST':
                    result = self.service_forgot.confirm_forgot_password()
                    return ResponseUtils.sucess(HTTPStatus.CREATED, result)
                raise ValidationRequestException("Método HTTP inválido")

            raise ValidationRequestException("Endpoint inválido")

        except (CreateUserException, ConfirmationUserException, ForgotPasswordException, LoginException, LogoutException,
                ValidationRequestException, GenerateQRCodeException, ValidateQRCodeException) as error:
            return ResponseUtils.error(HTTPStatus.BAD_REQUEST, error.message)

        except ValidationTokenException as error:
            return ResponseUtils.error(HTTPStatus.FORBIDDEN, error.message)

        except Exception as error:
            return ResponseUtils.error(HTTPStatus.INTERNAL_SERVER_ERROR, str(error))



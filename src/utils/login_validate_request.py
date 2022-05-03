from src.exception.validation_request_exception import ValidationRequestException


class LoginValidateRequest:

    def validate_header_login(self, header):
        if not 'client_id' in header:
            raise ValidationRequestException("Necessário informar o client_id no header da request")

    def validate_body_login(self, body):
        if not 'username' in body:
            raise ValidationRequestException("Necessário informar o username no body da request")
        if not 'password' in body:
            raise ValidationRequestException("Necessário informar o password no body da request")

    def validate_header_mfa(self, body):
        if not 'client_id' in body:
            raise ValidationRequestException("Necessário informar o client_id no header da request")
        if not 'session' in body:
            raise ValidationRequestException("Necessário informar o session no header da request")

    def validate_body_mfa(self, body):
        if not 'username' in body:
            raise ValidationRequestException("Necessário informar o username no body da request")
        if not 'software_token_mfa_code' in body:
            raise ValidationRequestException("Necessário informar o software_token_mfa_code no body da request")

    def validate_header_logout(self, body):
        if not 'access_token' in body:
            raise ValidationRequestException("Necessário informar o access_token no header da request")

    def validate_body_validation_token(self, body):
        if not 'access_token' in body:
            raise ValidationRequestException("Necessário informar o access_token no body da request")
        if not 'client_id' in body:
            raise ValidationRequestException("Necessário informar o client_id no body da request")
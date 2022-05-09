from src.exception.validation_request_exception import ValidationRequestException


class ConfirmacaoUsuarioValidateRequest:

    def validate_body(self, body):
        if not 'username' in body:
            raise ValidationRequestException("Necessário informar o username no body da request")
        if not 'confirmation_code' in body:
            raise ValidationRequestException("Necessário informar o confirmation_code no body da request")

    def validate_header(self, header):
        if not 'client_id' in header:
            raise ValidationRequestException("Necessário informar o client_id no header da request")

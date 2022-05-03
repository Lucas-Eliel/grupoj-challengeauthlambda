from src.exception.validation_request_exception import ValidationRequestException


class ValidationRequest:

    def __init__(self, event):
        self.event = event

    def validate_body(self, body):
        if not 'cupom' in body:
            raise ValidationRequestException("Necessário informar o cupom no body da request")
        if not 'cnpj' in body:
            raise ValidationRequestException("Necessário informar o cnpj no body da request")
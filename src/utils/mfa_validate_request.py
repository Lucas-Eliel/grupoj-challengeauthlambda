from src.exception.validation_request_exception import ValidationRequestException


class MFAValidateRequest:

    def validate_header_qr_code(self, header):
        if not 'session' in header:
            raise ValidationRequestException("Necessário informar o session no header da request")

    def validate_body_qr_code(self, body):
        if not 'user_code' in body:
            raise ValidationRequestException("Necessário informar o user_code no body da request")
        if not 'friendly_device_name' in body:
            raise ValidationRequestException("Necessário informar o friendly_device_name no body da request")
from src.exception.validation_request_exception import ValidationRequestException


class CadastroUsuarioValidateRequest:

    def validate_body(self, body):
        if not 'username' in body:
            raise ValidationRequestException("Necessário informar o username no body da request")

        if not 'password' in body:
            raise ValidationRequestException("Necessário informar o password no body da request")

        if not 'attributes' in body:
            raise ValidationRequestException("Necessário informar o attributes no body da request")

        if not 'name' in body['attributes']:
            raise ValidationRequestException("Necessário informar o name para attributes no body da request")

        if not 'middle_name' in body['attributes']:
            raise ValidationRequestException("Necessário informar o middle_name para attributes no body da request")

        if not 'email' in body['attributes']:
            raise ValidationRequestException("Necessário informar o email para attributes no body da request")

        if not 'locale' in body['attributes']:
            raise ValidationRequestException("Necessário informar o locale para attributes no body da request")

        if not 'phone_number' in body['attributes']:
            raise ValidationRequestException("Necessário informar o phone_number para attributes no body da request")

        if not 'address' in body['attributes']:
            raise ValidationRequestException("Necessário informar o address para attributes no body da request")

    def validate_header(self, header):
        if not 'client_id' in header:
            raise ValidationRequestException("Necessário informar o client_id no header da request")

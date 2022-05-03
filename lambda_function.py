from src.controller.challenge_auth_controller import ChallengeAuthController


def lambda_handler(event, context):
    return ChallengeAuthController(event).invoke()


#lambda_handler({"resource": "/criar_usuario", "httpMethod": "POST", "body": {"client_id": "20tfh1piiu8pja1khmjuve6ra0", "username": "lucaseliel.study@gmail.com",
#    "password": "Abc@123",
#    "attributes": {
#        "name": "Joao",
#        "middle_name": "Souza",
#        "email": "lucaseliel.study@gmail.com",
#        "locale": "Brasil",
#        "phone_number": "+15555555555",
#        "address": "Rua Alfa"
#    }
#}}, {})


lambda_handler({"resource": "/confirmar_cadastro_usuario", "httpMethod": "POST", "body": {"client_id": "20tfh1piiu8pja1khmjuve6ra0", "username": "lucaseliel.study@gmail.com", "confirmation_code": "696681"}}, {})
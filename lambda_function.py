from src.controller.challenge_auth_controller import ChallengeAuthController


def lambda_handler(event, context):
    response = ChallengeAuthController(event).invoke()
    print(response)
    return response

#Criar usuario
#lambda_handler({"resource": "/usuario", "httpMethod": "POST", "body": {"client_id": "20tfh1piiu8pja1khmjuve6ra0", "username": "lucaseliel.study@gmail.com",
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

#Confirmar cadastro do usuario
#lambda_handler({"resource": "/usuario_confirmacao", "httpMethod": "POST", "body": {"client_id": "20tfh1piiu8pja1khmjuve6ra0", "username": "lucaseliel.study@gmail.com", "confirmation_code": "879764"}}, {})

#Obter QR Code MFA
#lambda_handler({"resource": "/usuario_confirmacao", "httpMethod": "POST", "body": {"client_id": "20tfh1piiu8pja1khmjuve6ra0", "username": "lucaseliel.study@gmail.com", "confirmation_code": "879764"}}, {})

##Entrar
#lambda_handler({"resource": "/sign_in", "httpMethod": "POST", "headers": {"client_id": "20tfh1piiu8pja1khmjuve6ra0"}, "body": {"username": "lucaseliel.study@gmail.com", "password": "Abc@123"}}, {})

##Validar MFA login
#lambda_handler({"resource": "/sign_in", "httpMethod": "POST", "headers": {"client_id": "20tfh1piiu8pja1khmjuve6ra0", "session": "AYABeKGlAKnA7qx6m8P8A4aY-eUAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHiG0oCCDoro3IaeecGyxCZJOVZkUqttbPnF4J7Ar-5byAGpVK_9D7YKzHArWQtaAKyDAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMLV3BhV0s64gHElLMAgEQgDsRi86KQPcrAUTTAA8TBiuxpFJ8jCcv-38dFOvY94XPDF9t9rjn6HHlc7DfZT5Mmk44DHJMt2nPFPYaNgIAAAAADAAAEAAAAAAAAAAAAAAAAAChhT4p0wCTbXqPB0ZVH8lf_____wAAAAEAAAAAAAAAAAAAAAEAAAEDaRmw-04Vqf78qLxA5yWWFTBW1Pf4lOQjKU5pmro68kHV2l6kBXpR1SGRGHuX77amiTFOeasZdI8T0a8iISOiLlMv9mavnaioJaWF_mMc_4-yKqaBkgoRaTpNQ3BthaTMvDFmZYvl462NvY_ssyvluVXhCwJ5r59ZFBFokCJM1_4ro-MMdkZcVtPa71SsS-GT186k7y7MymQdw-ruMcp69EbpE5AxsS4a7iKnVs4YNuVcxm0r9Ugj8T0P6gOzHDb70CP_TQNveqiHy-3VJoY00wXI2_L14q92tqHdA373yO0mjLEqQMEeaF6JRuKRkODXttlZ2T1d-u3t-rQRSxQ2DBRjPbFjX11XhSKVu4Pdkm3E2uM"},"body": {"username": "lucaseliel.study@gmail.com", "password": "Abc@123"}}, {})
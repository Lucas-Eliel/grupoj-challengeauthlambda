from src.controller.challenge_auth_controller import ChallengeAuthController


def lambda_handler(event, context):
    return ChallengeAuthController(event).invoke()

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
#lambda_handler({"resource": "/mfa_qr_code", "httpMethod": "GET", "headers": {"session": "AYABeA670j0XdE1cvRk620dbZhoAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHiG0oCCDoro3IaeecGyxCZJOVZkUqttbPnF4J7Ar-5byAEVbcjtt7SHhfbl9Rsf3tjeAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMvAC_n_VG5AAqLHH0AgEQgDtAbrnUolTbhG4R_OcLjTDWLWhCFNjp6oQf5cxhf2M5vy6bOqSuhrUOS1z0vOkYuE1FcakzKyjJGY3TywIAAAAADAAAEAAAAAAAAAAAAAAAAABwLEIOAgVO7mz2ez2A_zFt_____wAAAAEAAAAAAAAAAAAAAAEAAAED2fH3ulU3NAxB8sxGQt_lsdhZ15UQM04FEDnDqJpPcbAj22wGrf5hAL6G9wv01zsaIcluzgdO7MNCPI-tpYh512_ZCZtwLmWhZTAJxqmA897QBFU4hw8QsbEIovPjcgq6909yckShZ9NCI62UA9UyRBW98981sPJqGRI8a3YnKR3ec-Txy7XHwFz1ZoXwdAviAaPkdVQIT5qaNVopF_Y6IOGZQycgIN1_diMOKfmwgZVnrWT7VPYJhc94qOwsosqSNrvIil1tPSSVB4Ir7Q1bCNmgS80P_WtOjbq_dUQ5hhFbhtN98XsoeVMPiAkG4hbbXSPb9rZD-pr-qZEr_96nG1DhiwmeN_PASigZAQ3XzJzDXHU"}}, {})

##Entrar
#lambda_handler({"resource": "/sign_in", "httpMethod": "POST", "headers": {"client_id": "20tfh1piiu8pja1khmjuve6ra0"}, "body": {"username": "lucaseliel.study@gmail.com", "password": "Abc@13"}}, {})

##Validar MFA login
#lambda_handler({"resource": "/validation_token", "httpMethod": "POST", "headers": {"client_id": "20tfh1piiu8pja1khmjuve6ra0", "authorization": "eyJraWQiOiJ6cmtkZlpkVWdxVnRmR2UzZWZUNU5RdU9vaXZjejF2aFwvN1wvYm5PQlNjVGM9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIxNTgwZDUxZC1lZTFjLTQwYWUtYTNmYi0wN2EwODY5N2M5ZGIiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9kSVJYOE5XVjIiLCJjbGllbnRfaWQiOiIyMHRmaDFwaWl1OHBqYTFraG1qdXZlNnJhMCIsIm9yaWdpbl9qdGkiOiIyYTQ0YzczMi0zZWRiLTQzNjYtOGRhZC00MmNkYjBjODQ1MDAiLCJldmVudF9pZCI6IjlhZDMwMTEyLTk2NTItNDE5ZS1iMWNkLTc5MGY3YzBiYmVlYiIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2NTE3OTA3OTgsImV4cCI6MTY1MTc5NDM5OCwiaWF0IjoxNjUxNzkwNzk4LCJqdGkiOiJkZGNlMDQyMC1hYmNkLTRkZmYtODI4Ny1kODM5NzIzNWNiOTYiLCJ1c2VybmFtZSI6IjE1ODBkNTFkLWVlMWMtNDBhZS1hM2ZiLTA3YTA4Njk3YzlkYiJ9.QvJNn6xIihyVRN0Plf8t9b8IZwDQ0UoKZpR92kXL4eAHNi1uXggRwWsRE-vMlkvQvW06QRcOTRJ8LEGyGnF5zbEsiJjTIGxywIs5bKTiB9HqhuDXh9mNwbN2B_wsZDLGVd_lwQZvGfix5yaU_K_ZRjYAcjTHdKyGpShqCt30eeqhTrVrCvQxUJeTGOCmO2zL96423E2f41UwB0aMf5wnFZmxNxkjNXCYJkEeQTv3En5XQwwhyZBwgL2un7aK1rJ7MKmWuFRrNFruudN68FhfOCyIE7xiWz_NS4IWIblOHUV1sYfYA3ixshQMJ_RlS5Pd0seRyM1g0Y7yJ_EBWAt6JQ"}}, {})
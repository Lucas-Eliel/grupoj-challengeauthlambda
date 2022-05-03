class ResponseUtils:

    @staticmethod
    def sucess(status, payload):
        return {
            "headers": {"Content-Type": "application/json"},
            "statusCode": status,
            "body": {
                "data": payload
            }
        }

    @staticmethod
    def error(status, message):
        payload = {
            "codigo": status,
            "mensagem": message
        }

        return {
            "headers": {"Content-Type": "application/json"},
            "statusCode": status,
            "body": {
                "testes": {
                    "data": payload
                }
            }
        }

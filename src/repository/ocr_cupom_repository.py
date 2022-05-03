import boto3

from src.exception.dynamodb_integration_exception import DynamodbIntegrationException

IS_ATIVO_AMBIENTE_LOCAL=False


def get_connection_dynamodb():
    if IS_ATIVO_AMBIENTE_LOCAL:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4569", region_name="sa-east-1", aws_access_key_id="admin", aws_secret_access_key="admin")
        return dynamodb.Table('ocr-cupom')
    else:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://dynamodb:4569", region_name="sa-east-1", aws_access_key_id="admin", aws_secret_access_key="admin")
        return dynamodb.Table('ocr-cupom')


class OcrCupomRepository:

    def __init__(self):
        self.connection = get_connection_dynamodb()

    def save(self, cupom):
        try:
            self.connection.put_item(Item=cupom)
        except Exception as error:
            raise DynamodbIntegrationException("Error ao criar registro do cupom no DynamoDB " + str(error))
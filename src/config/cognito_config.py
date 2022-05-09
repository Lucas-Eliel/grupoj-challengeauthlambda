import boto3


class CognitoConfig:

    def get_connection_cognito(self):
        return boto3.client('cognito-idp', region_name='us-east-1', aws_access_key_id='AKIARK3PD7LHNAHHOJNL', aws_secret_access_key='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')

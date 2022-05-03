import boto3


def get_connection_cognito():
    return boto3.client('cognito-idp', region_name='us-east-1', aws_access_key_id='AKIARK3PD7LHNAHHOJNL', aws_secret_access_key='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')


class MFARepository:

    def __init__(self):
        self.connection = get_connection_cognito()

    def obterQRCode(self):
        try:
            return self.connection.associate_software_token(
                Session='AYABeEUa5vl4iHDuWKi6MnZyG24AHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHiG0oCCDoro3IaeecGyxCZJOVZkUqttbPnF4J7Ar-5byAEK62QWQE17RGv2TMiuhS24AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMeMGqTJiG84L4wRy4AgEQgDsSXz9ZfU-90JpMdi0T2FV6CBeYUDeo1lfxil02oQnHNReCcF1vucZfNGJ1SnVVRTTf4n7qhtfGRG_w7gIAAAAADAAAEAAAAAAAAAAAAAAAAACVqwKIhYtQ0-i1bwusbYKM_____wAAAAEAAAAAAAAAAAAAAAEAAAEDZNzkyixbU1xmZ-QgcNOUI9GVc_68bcSOgzyN7BSMwhBMGhahShllCKacMzbVT_GDpsrGumyYkksnHS9JSllCbcBBoYJ81x7xWmCrGC7Z_QayYCIZ3BqLQEU-H62f6cfA03BPx6VKR-BEXCn6LITj2E4UZkqxxuMrvzDUYkGof8T3rsxpC_8O8lD5z_FWAmXO3VY11cJlFM65aYKjmpuTxpd8YXMJj6f-AA8wLnOPyVChr8ubhv-LUOh1X13x-V4egmyvCbx9BVoknw6wTSuenMhhI9dBXW4QnBX8WtOK_Xpu46RqbamfJ5Mpy-iiw6hsZjZWp15AY72f-EuHjSfalSvjJ31mcSbaLnYCeRXv1gonGt8',
            )
        except Exception as error:
            print(error)


    def validaToken(self):
        try:
            return self.connection.verify_software_token(
                UserCode='375646',
                Session='AYABeKSkPv7jdvslWrQt50WDOy4AHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHiG0oCCDoro3IaeecGyxCZJOVZkUqttbPnF4J7Ar-5byAF5VMjx36jPkTmG1ovLglA2AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMmwSaftVfE385ne0vAgEQgDu_jeNsqnCDIJLxkjizeqguPYJMRJ84W3l1ypmeQCbBURXKzDjnv9-qTkH0oPq4q_Iq7Xr6dFsMoEawpQIAAAAADAAAEAAAAAAAAAAAAAAAAADxhNetN9xtXorCq7NQTTa3_____wAAAAEAAAAAAAAAAAAAAAEAAAEYTE1y1tRQpmznZKA6ra6M1T4iR8LF7GUZeb_kg7TRJug5gIE2eCcLKf80VwYVDbCR6amOvV_bGNnJ6gIQoH5xryI2uP0GaufwOUJFYuXFEd-I0_2Q3i9VC71loZ_ckGprmtLh0aSfDvJM2mLON1fnSUF2m7oHJXAMczvQwIv9Tt9n8B9VUp6ZNkaVxfLY9Yfqlu4EwAzHzmXt4NJ-MVfkBgDGEoX8at-rN3CHohE5Wqa_1UzUIUhACH8JNINrvFcly4riwhzBDxAXDKcdVV2QH0luXP-G9JRv0r3kltdSsak1DNnKdA5AXBWx-aXQ2znO3MDr4tJ7jk_tU8ln19xRo7wMPl_Q9CPHe6SPM8bbhqHvDhueHs9MK2wupxjdUIxKG457E_GGNUY',
                FriendlyDeviceName='Iphone de Lucas'
            )
        except Exception as error:
            print(error)


if __name__ == '__main__':
    #resp = MFARepository().obterQRCode()
    resp = MFARepository().validaToken()

    print(resp)

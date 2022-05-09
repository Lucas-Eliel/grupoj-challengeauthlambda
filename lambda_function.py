from src.controller.challenge_auth_controller import ChallengeAuthController


def lambda_handler(event, context):
    return ChallengeAuthController(event).invoke()
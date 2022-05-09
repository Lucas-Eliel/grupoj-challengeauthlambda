#!/bin/bash

API_NAME=api
STAGE=test

echo -----------------------------------------------------------------
echo ------Criando a lambda do grupoj-challengeauthlambda-------------
echo -----------------------------------------------------------------

awslocal lambda create-function --function-name challengeauthlambdafunction \
    --code S3Bucket="__local__",S3Key="/lambda_folder" \
    --handler lambda_function.lambda_handler \
    --runtime python3.8 \
    --role All

[ $? == 0 ] || fail 1 "Failed: AWS / lambda / create-function"

echo -----------------------------------------------------------------
echo ------Criando a lambda do grupoj-challengeauthlambda-------------
echo -----------------------------------------------------------------

LAMBDA_CHALLENGE_AUTH_ARN=$(awslocal lambda list-functions --query "Functions[?FunctionName==\`challengeauthlambdafunction\`].FunctionArn" --output text)
echo LAMBDA_CHALLENGE_AUTH_ARN ${LAMBDA_CHALLENGE_AUTH_ARN}

echo -----------------------------------------------------------------
echo ---------------------Criando o API Gateway-----------------------
echo -----------------------------------------------------------------

awslocal apigateway create-rest-api --name ${API_NAME}

[ $? == 0 ] || fail 2 "Failed: AWS / apigateway / create-rest-api"

API_ID=$(awslocal apigateway get-rest-apis --query "items[?name==\`${API_NAME}\`].id" --output text)
echo API_ID ${API_ID}

PARENT_RESOURCE_ID=$(awslocal apigateway get-resources --rest-api-id ${API_ID} --query 'items[?path==`/`].id' --output text)
echo PARENT_RESOURCE_ID ${PARENT_RESOURCE_ID}

awslocal apigateway create-resource \
    --rest-api-id ${API_ID} \
    --parent-id ${PARENT_RESOURCE_ID} \
    --path-part "usuario"

awslocal apigateway create-resource \
    --rest-api-id ${API_ID} \
    --parent-id ${PARENT_RESOURCE_ID} \
    --path-part "usuario_confirmacao"

awslocal apigateway create-resource \
    --rest-api-id ${API_ID} \
    --parent-id ${PARENT_RESOURCE_ID} \
    --path-part "mfa_qr_code"

awslocal apigateway create-resource \
    --rest-api-id ${API_ID} \
    --parent-id ${PARENT_RESOURCE_ID} \
    --path-part "mfa_qr_code_confirmacao"

awslocal apigateway create-resource \
    --rest-api-id ${API_ID} \
    --parent-id ${PARENT_RESOURCE_ID} \
    --path-part "sign_in"

awslocal apigateway create-resource \
    --rest-api-id ${API_ID} \
    --parent-id ${PARENT_RESOURCE_ID} \
    --path-part "validate_mfa"

awslocal apigateway create-resource \
    --rest-api-id ${API_ID} \
    --parent-id ${PARENT_RESOURCE_ID} \
    --path-part "validation_token"

awslocal apigateway create-resource \
    --rest-api-id ${API_ID} \
    --parent-id ${PARENT_RESOURCE_ID} \
    --path-part "sign_out"

awslocal apigateway create-resource \
    --rest-api-id ${API_ID} \
    --parent-id ${PARENT_RESOURCE_ID} \
    --path-part "forgot_password"

awslocal apigateway create-resource \
    --rest-api-id ${API_ID} \
    --parent-id ${PARENT_RESOURCE_ID} \
    --path-part "confirmation_forgot_password"

echo ---------------------------------------------------------------------------------------------------
echo ---------------------Criando recurso do grupoj-challengeauthlambda API Gateway---------------------
echo ---------------------------------------------------------------------------------------------------

RESOURCE_ID_1=$(awslocal apigateway get-resources --rest-api-id ${API_ID} --query 'items[?path==`/usuario`].id' --output text)
echo RESOURCE_ID_1 ${RESOURCE_ID_1}

[ $? == 0 ] || fail 5 "Failed: AWS / apigateway / put-integration"

awslocal apigateway put-method \
    --rest-api-id ${API_ID} \
    --resource-id ${RESOURCE_ID_1} \
    --http-method POST \
    --authorization-type "NONE" \

[ $? == 0 ] || fail 6 "Failed: AWS / apigateway / put-method"

awslocal apigateway put-integration \
    --rest-api-id ${API_ID} \
    --resource-id ${RESOURCE_ID_1} \
    --http-method POST \
    --type AWS_PROXY \
    --integration-http-method POST \
    --uri arn:aws:apigateway:sa-east-1:lambda:path/2015-03-31/functions/${LAMBDA_CHALLENGE_AUTH_ARN}/invocations \
    --passthrough-behavior WHEN_NO_MATCH \


RESOURCE_ID_2=$(awslocal apigateway get-resources --rest-api-id ${API_ID} --query 'items[?path==`/usuario_confirmacao`].id' --output text)
echo RESOURCE_ID_2 ${RESOURCE_ID_2}

[ $? == 0 ] || fail 5 "Failed: AWS / apigateway / put-integration"

awslocal apigateway put-method \
    --rest-api-id ${API_ID} \
    --resource-id ${RESOURCE_ID_2} \
    --http-method POST \
    --authorization-type "NONE" \

[ $? == 0 ] || fail 6 "Failed: AWS / apigateway / put-method"

awslocal apigateway put-integration \
    --rest-api-id ${API_ID} \
    --resource-id ${RESOURCE_ID_2} \
    --http-method POST \
    --type AWS_PROXY \
    --integration-http-method POST \
    --uri arn:aws:apigateway:sa-east-1:lambda:path/2015-03-31/functions/${LAMBDA_CHALLENGE_AUTH_ARN}/invocations \
    --passthrough-behavior WHEN_NO_MATCH \


RESOURCE_ID_3=$(awslocal apigateway get-resources --rest-api-id ${API_ID} --query 'items[?path==`/mfa_qr_code`].id' --output text)
echo RESOURCE_ID_3 ${RESOURCE_ID_3}

[ $? == 0 ] || fail 5 "Failed: AWS / apigateway / put-integration"

awslocal apigateway put-method \
    --rest-api-id ${API_ID} \
    --resource-id ${RESOURCE_ID_3} \
    --http-method GET \
    --authorization-type "NONE" \

[ $? == 0 ] || fail 6 "Failed: AWS / apigateway / put-method"

awslocal apigateway put-integration \
    --rest-api-id ${API_ID} \
    --resource-id ${RESOURCE_ID_3} \
    --http-method GET \
    --type AWS_PROXY \
    --integration-http-method POST \
    --uri arn:aws:apigateway:sa-east-1:lambda:path/2015-03-31/functions/${LAMBDA_CHALLENGE_AUTH_ARN}/invocations \
    --passthrough-behavior WHEN_NO_MATCH \


RESOURCE_ID_4=$(awslocal apigateway get-resources --rest-api-id ${API_ID} --query 'items[?path==`/mfa_qr_code_confirmacao`].id' --output text)
echo RESOURCE_ID_4 ${RESOURCE_ID_4}

[ $? == 0 ] || fail 5 "Failed: AWS / apigateway / put-integration"

awslocal apigateway put-method \
    --rest-api-id ${API_ID} \
    --resource-id ${RESOURCE_ID_4} \
    --http-method POST \
    --authorization-type "NONE" \

[ $? == 0 ] || fail 6 "Failed: AWS / apigateway / put-method"

awslocal apigateway put-integration \
    --rest-api-id ${API_ID} \
    --resource-id ${RESOURCE_ID_4} \
    --http-method POST \
    --type AWS_PROXY \
    --integration-http-method POST \
    --uri arn:aws:apigateway:sa-east-1:lambda:path/2015-03-31/functions/${LAMBDA_CHALLENGE_AUTH_ARN}/invocations \
    --passthrough-behavior WHEN_NO_MATCH \


RESOURCE_ID_5=$(awslocal apigateway get-resources --rest-api-id ${API_ID} --query 'items[?path==`/sign_in`].id' --output text)
echo RESOURCE_ID_5 ${RESOURCE_ID_5}

[ $? == 0 ] || fail 5 "Failed: AWS / apigateway / put-integration"

awslocal apigateway put-method \
    --rest-api-id ${API_ID} \
    --resource-id ${RESOURCE_ID_5} \
    --http-method POST \
    --authorization-type "NONE" \

[ $? == 0 ] || fail 6 "Failed: AWS / apigateway / put-method"

awslocal apigateway put-integration \
    --rest-api-id ${API_ID} \
    --resource-id ${RESOURCE_ID_5} \
    --http-method POST \
    --type AWS_PROXY \
    --integration-http-method POST \
    --uri arn:aws:apigateway:sa-east-1:lambda:path/2015-03-31/functions/${LAMBDA_CHALLENGE_AUTH_ARN}/invocations \
    --passthrough-behavior WHEN_NO_MATCH \


RESOURCE_ID_6=$(awslocal apigateway get-resources --rest-api-id ${API_ID} --query 'items[?path==`/validate_mfa`].id' --output text)
echo RESOURCE_ID_6 ${RESOURCE_ID_6}

[ $? == 0 ] || fail 5 "Failed: AWS / apigateway / put-integration"

awslocal apigateway put-method \
    --rest-api-id ${API_ID} \
    --resource-id ${RESOURCE_ID_6} \
    --http-method POST \
    --authorization-type "NONE" \

[ $? == 0 ] || fail 6 "Failed: AWS / apigateway / put-method"validation_token

awslocal apigateway put-integration \
    --rest-api-id ${API_ID} \
    --resource-id ${RESOURCE_ID_6} \
    --http-method POST \
    --type AWS_PROXY \
    --integration-http-method POST \
    --uri arn:aws:apigateway:sa-east-1:lambda:path/2015-03-31/functions/${LAMBDA_CHALLENGE_AUTH_ARN}/invocations \
    --passthrough-behavior WHEN_NO_MATCH \


RESOURCE_ID_7=$(awslocal apigateway get-resources --rest-api-id ${API_ID} --query 'items[?path==`/validation_token`].id' --output text)
echo RESOURCE_ID_7 ${RESOURCE_ID_7}

[ $? == 0 ] || fail 5 "Failed: AWS / apigateway / put-integration"

awslocal apigateway put-method \
    --rest-api-id ${API_ID} \
    --resource-id ${RESOURCE_ID_7} \
    --http-method POST \
    --authorization-type "NONE" \

[ $? == 0 ] || fail 6 "Failed: AWS / apigateway / put-method"

awslocal apigateway put-integration \
    --rest-api-id ${API_ID} \
    --resource-id ${RESOURCE_ID_7} \
    --http-method POST \
    --type AWS_PROXY \
    --integration-http-method POST \
    --uri arn:aws:apigateway:sa-east-1:lambda:path/2015-03-31/functions/${LAMBDA_CHALLENGE_AUTH_ARN}/invocations \
    --passthrough-behavior WHEN_NO_MATCH \


RESOURCE_ID_8=$(awslocal apigateway get-resources --rest-api-id ${API_ID} --query 'items[?path==`/sign_out`].id' --output text)
echo RESOURCE_ID_8 ${RESOURCE_ID_8}

[ $? == 0 ] || fail 5 "Failed: AWS / apigateway / put-integration"

awslocal apigateway put-method \
    --rest-api-id ${API_ID} \
    --resource-id ${RESOURCE_ID_8} \
    --http-method POST \
    --authorization-type "NONE" \

[ $? == 0 ] || fail 6 "Failed: AWS / apigateway / put-method"

awslocal apigateway put-integration \
    --rest-api-id ${API_ID} \
    --resource-id ${RESOURCE_ID_8} \
    --http-method POST \
    --type AWS_PROXY \
    --integration-http-method POST \
    --uri arn:aws:apigateway:sa-east-1:lambda:path/2015-03-31/functions/${LAMBDA_CHALLENGE_AUTH_ARN}/invocations \
    --passthrough-behavior WHEN_NO_MATCH \


RESOURCE_ID_9=$(awslocal apigateway get-resources --rest-api-id ${API_ID} --query 'items[?path==`/forgot_password`].id' --output text)
echo RESOURCE_ID_9 ${RESOURCE_ID_9}

[ $? == 0 ] || fail 5 "Failed: AWS / apigateway / put-integration"

awslocal apigateway put-method \
    --rest-api-id ${API_ID} \
    --resource-id ${RESOURCE_ID_9} \
    --http-method POST \
    --authorization-type "NONE" \

[ $? == 0 ] || fail 6 "Failed: AWS / apigateway / put-method"

awslocal apigateway put-integration \
    --rest-api-id ${API_ID} \
    --resource-id ${RESOURCE_ID_9} \
    --http-method POST \
    --type AWS_PROXY \
    --integration-http-method POST \
    --uri arn:aws:apigateway:sa-east-1:lambda:path/2015-03-31/functions/${LAMBDA_CHALLENGE_AUTH_ARN}/invocations \
    --passthrough-behavior WHEN_NO_MATCH \


RESOURCE_ID_10=$(awslocal apigateway get-resources --rest-api-id ${API_ID} --query 'items[?path==`/confirmation_forgot_password`].id' --output text)
echo RESOURCE_ID_10 ${RESOURCE_ID_10}

[ $? == 0 ] || fail 5 "Failed: AWS / apigateway / put-integration"

awslocal apigateway put-method \
    --rest-api-id ${API_ID} \
    --resource-id ${RESOURCE_ID_10} \
    --http-method POST \
    --authorization-type "NONE" \

[ $? == 0 ] || fail 6 "Failed: AWS / apigateway / put-method"

awslocal apigateway put-integration \
    --rest-api-id ${API_ID} \
    --resource-id ${RESOURCE_ID_10} \
    --http-method POST \
    --type AWS_PROXY \
    --integration-http-method POST \
    --uri arn:aws:apigateway:sa-east-1:lambda:path/2015-03-31/functions/${LAMBDA_CHALLENGE_AUTH_ARN}/invocations \
    --passthrough-behavior WHEN_NO_MATCH \

[ $? == 0 ] || fail 7 "Failed: AWS / apigateway / put-integration"

awslocal apigateway create-deployment \
    --rest-api-id ${API_ID} \
    --stage-name ${STAGE} \

[ $? == 0 ] || fail 6 "Failed: AWS / apigateway / create-deployment"

ENDPOINT=http://localhost:4566/restapis/${API_ID}/${STAGE}/_user_request_/

echo "API available at: ${ENDPOINT}"

echo "{\"lambda_url\":\"${ENDPOINT}\"}" > /output/endpoint.json

echo Ambiente configurado com sucesso!
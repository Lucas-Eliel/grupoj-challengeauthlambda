#!/bin/bash

echo Encerrando a infraestrutura do projeto ocr cupom

rm -R  ../redis
rm -R  ../packaging

docker compose -f ./redis/docker-compose.yml down

docker compose -f ./dynamodb/docker-compose.yml down

docker compose -f ./localstack/docker-compose.yml down

docker network rm ocr-network
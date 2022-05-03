import redis
from datetime import timedelta

IS_ATIVO_AMBIENTE_LOCAL=False

def get_connection_redis():
    if IS_ATIVO_AMBIENTE_LOCAL:
        return redis.ConnectionPool(host='localhost', port=6379)
    else:
        return redis.ConnectionPool(host='my_redis', port=6379)


class OcrCupomRedis:

    def __init__(self):
        self.connection = get_connection_redis()

    def get(self, key):
        my_server = redis.Redis(connection_pool=self.connection)
        response = my_server.get(key)
        return response

    def save(self, key, value):
        my_server = redis.Redis(connection_pool=self.connection)
        my_server.set(key, value)
        my_server.expire(key, timedelta(seconds=60))
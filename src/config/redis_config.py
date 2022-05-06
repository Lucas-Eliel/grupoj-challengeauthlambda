import redis

IS_ATIVO_AMBIENTE_LOCAL=False


class RedisConfig:

    def get_connection_redis(self):
        if IS_ATIVO_AMBIENTE_LOCAL:
            return redis.ConnectionPool(host='localhost', port=6379)
        else:
            return redis.ConnectionPool(host='my_redis', port=6379)
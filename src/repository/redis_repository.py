from datetime import timedelta

from src.config.redis_config import RedisConfig
import redis


class RedisRepository:

    def __init__(self):
        self.connection = RedisConfig().get_connection_redis()

    def get(self, key):
        my_server = redis.Redis(connection_pool=self.connection)
        response = my_server.get(key)
        return response

    def save(self, key, value):
        my_server = redis.Redis(connection_pool=self.connection)
        my_server.set(key, value)
        my_server.expire(key, timedelta(seconds=1800))
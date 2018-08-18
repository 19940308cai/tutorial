import redis
from configparser import ConfigParser
configer = ConfigParser()
configer.read("./db.ini")
redisHandle=redis.Redis(host=configer.get("redis","host"), port=configer.get("redis","port"), decode_responses=True)

class RedisClient:

    @classmethod
    def redisPush(cls,key,value):
        return redisHandle.lpush(key,value)

    @classmethod
    def redisPull(cls,key):
        return redisHandle.lpop(key)







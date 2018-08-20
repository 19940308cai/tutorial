import redis

redisHandle=redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)

class RedisClient:

    @classmethod
    def redisPush(cls,key,value):
        return redisHandle.lpush(key,value)

    @classmethod
    def redisPull(cls,key):
        return redisHandle.lpop(key)







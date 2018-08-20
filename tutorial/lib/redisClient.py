import redis



class RedisClient:


    def __init__(self):
        self.redisClient = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)


    def redisPushQ(self,key,value):
        return self.redisClient.lpush(key,value)


    def redisPullQ(self,key):
        return self.redisClient.lpop(key)





if __name__ == '__main__':
    client = RedisClient()
    data = client.redisPushQ("caijiang",1)
    print(data)


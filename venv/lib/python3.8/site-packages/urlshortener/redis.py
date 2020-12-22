import redis
import configparser


class Redis:
    def __init__(self):
        self.redis_db = self.connect_to_redis()
        config = configparser.ConfigParser()
        config.read('db.ini')
        self.redis_host = config['redis']['host']
        self.redis_port = config['redis']['port']
        self.redis_pass = config['redis']['pass']

    def connect_to_redis(self):
        return redis.Redis(
                            host=self.redis_host,
                            port=self.redis_port,
                            password=None)

    def add_key_value(self, key, value):
        self.redis_db.set(key, value)

    def get_value_by_key(self, key):
        return self.redis_db.get(key)

    def does_key_exist(self, key):
        print(key)
        if(self.redis_db.exists(key)):
            return True
        return False

    def remove_key(self, key):
        self.redis_db.delete(key)

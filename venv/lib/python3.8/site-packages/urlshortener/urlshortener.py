import configparser

from Redis import Redis


class UrlShortener:
    def __init__(self):
        self.redis = Redis()
        if not self.redis.does_key_exist('id'):
            self.redis.add_key_value('id', '1')
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.short_url = config['config']['short_url']
        self.accepted_char = config['config']['accepted_char']

    def shorten_url(self, original_url):
        if (self.redis.does_key_exist(original_url)):
            url_id = int(self.redis.get_value_by_key(original_url))
            shorten_url = self.url_encoder(url_id)
        else:
            url_id = int(self.redis.get_value_by_key('id'))
            self.redis.add_key_value(original_url, url_id)
            shorten_url = self.url_encoder(url_id)
            url_id += 1
            self.redis.add_key_value('id', str(url_id))
        return self.short_url+shorten_url

    def url_encoder(self, id):
        characters = self.accepted_char
        base = len(characters)
        encoden_url = []
        while id > 0:
            val = id % base
            encoden_url.append(characters[val])
            id = (id // base)
        return "".join(encoden_url[::-1])

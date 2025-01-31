# utils/cache_utils.py
import redis
from config import Config
import json

class CacheManager:
    def __init__(self):
        self.redis = redis.from_url(Config.REDIS_URL)
        
    def get(self, key):
        val = self.redis.get(key)
        return json.loads(val) if val else None

    def set(self, key, value, ttl=3600):
        self.redis.setex(key, ttl, json.dumps(value))

    def clear_key(self, key):
        self.redis.delete(key)

# Usage in routes
cache = CacheManager()

@app.route('/api/words/<word>')
def get_word(word):
    cached = cache.get(f'word:{word}')
    if cached:
        return jsonify(cached)
    
    result = db.session.query(...).first()
    cache.set(f'word:{word}', result.to_dict())
    return jsonify(result.to_dict())
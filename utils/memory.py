import redis
import json

r = redis.Redis(host='localhost', port=8080, db=0)

def get_history(user_id):
    messages = r.lrange(f"chat:{user_id}", 0, -1)
    return [json.loads(m.decode()) for m in messages]

def add_to_history(user_id, role, message):
    r.rpush(f"chat:{user_id}", json.dumps({"role": role, "content": message}))
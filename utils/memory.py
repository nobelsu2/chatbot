import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

def getHistory(user_id):
    messages = r.lrange(f"chat:{user_id}", 0, -1)
    return [json.loads(m.decode()) for m in messages]

def addHistory(user_id, role, message):
    r.rpush(f"chat:{user_id}", json.dumps({"role": role, "content": message}))
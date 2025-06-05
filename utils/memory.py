import redis
import json
import streamlit as st

r = redis.Redis(
    host=st.secrets["redis"]["host"],
    port=st.secrets["redis"]["port"],
    password=st.secrets["redis"]["password"],
    ssl=False
)


def getHistory(user_id):
    messages = r.lrange(f"chat:{user_id}", 0, -1)
    return [json.loads(m.decode()) for m in messages]

def addHistory(user_id, role, message):
    r.rpush(f"chat:{user_id}", json.dumps({"role": role, "content": message}))
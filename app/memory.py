import redis
import json
from app.logger import logger

try:
    redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)
    redis_client.ping()
    REDIS_AVAILABLE = True
except Exception:
    logger.warning("Redis not available, using in-memory fallback")
    REDIS_AVAILABLE = False
    fallback_memory = {}

def get_history(user_id: str) -> list:
    if REDIS_AVAILABLE:
        data = redis_client.get(f"history:{user_id}")
        return json.loads(data) if data else []
    return fallback_memory.get(user_id, [])

def add_message(user_id: str, role: str, content: str):
    history = get_history(user_id)
    history.append({"role": role, "content": content})
    if len(history) > 10:
        history = history[-10:]

    if REDIS_AVAILABLE:
        redis_client.setex(f"history:{user_id}", 3600, json.dumps(history))
    else:
        fallback_memory[user_id] = history
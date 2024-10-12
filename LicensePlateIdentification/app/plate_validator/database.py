import redis
import os

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))

redis_client = redis.Redis(host=redis_host, port=redis_port, db=0)

def initialize_redis():
    """
    Initialize the Redis client and perform any required startup checks.
    """
    try:
        redis_client.ping()
        print("Connected to Redis successfully.")
    except redis.ConnectionError as e:
        print(f"Error connecting to Redis: {e}")
        # Handle connection errors or initialization failures

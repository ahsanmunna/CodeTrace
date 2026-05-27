import os
import redis
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

# Create Redis client
redis_client = redis.Redis.from_url(
    REDIS_URL,
    decode_responses=True
)

# Free tier configuration
FREE_TIER_LIMIT = 10          # requests
WINDOW_SECONDS = 60           # per minute


def is_rate_limited(api_key: str) -> bool:
    """
    Returns True if the API key has exceeded the free tier limit.
    Uses Redis atomic counters with expiration.
    """

    redis_key = f"rate_limit:{api_key}"

    try:
        # Increment request count
        current_count = redis_client.incr(redis_key)

        # Set expiration only on first request
        if current_count == 1:
            redis_client.expire(redis_key, WINDOW_SECONDS)

        # Check limit
        return current_count > FREE_TIER_LIMIT

    except redis.RedisError:
        # Fail open if Redis is unavailable
        # You can change this behavior if needed
        return False
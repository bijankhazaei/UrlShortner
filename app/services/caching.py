import aioredis
from app.core.config import settings

redis = aioredis.from_url(settings.redis_url, decode_responses=True)

async def cache_url(short_url: str, original_url: str, ttl: int = 3600):
    await redis.set(short_url, original_url, ex=ttl)

async def get_cached_url(short_url: str) -> str:
    return await redis.get(short_url)
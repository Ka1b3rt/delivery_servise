from app.core.config import settings

from redis.asyncio import Redis


def get_redis_client() -> Redis:
    client = Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        username=settings.REDIS_USER,
        password=settings.REDIS_PASSWORD,
        db=settings.REDIS_CACHE,
        decode_responses=True,
    )
    return client

from aio_pika import connect_robust
from aio_pika.abc import AbstractRobustConnection
from app.core.config import settings


async def get_rabbitmq_connection() -> AbstractRobustConnection:
    connection = await connect_robust(
        host=settings.RABBITMQ_HOST,
        port=settings.RABBITMQ_PORT,
        login=settings.RABBITMQ_USER,
        password=settings.RABBITMQ_PASSWORD,
        virtualhost=settings.RABBITMQ_VHOST,
    )
    return connection

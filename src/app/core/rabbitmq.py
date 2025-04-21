import json
from typing import Any, Callable

import aio_pika
from aio_pika import ExchangeType
from aio_pika.abc import AbstractChannel, AbstractConnection, AbstractQueue
from app.core.config import settings


class RabbitMQ:
    def __init__(self):
        self.connection: AbstractConnection | None = None
        self.channel: AbstractChannel | None = None
        self.exchange: aio_pika.Exchange | None = None
        self.queue: AbstractQueue | None = None

    async def connect(self):
        self.connection = await aio_pika.connect_robust(
            f"amqp://{settings.RABBITMQ_USER}:{settings.RABBITMQ_PASSWORD}@{settings.RABBITMQ_HOST}:{settings.RABBITMQ_PORT}/"
        )
        self.channel = await self.connection.channel()
        self.exchange = await self.channel.declare_exchange(
            "delivery_exchange", ExchangeType.DIRECT, durable=True
        )
        self.queue = await self.channel.declare_queue("delivery_queue", durable=True)
        await self.queue.bind(self.exchange, "delivery")

    async def publish(self, message: dict[str, Any], routing_key: str = "delivery"):
        if not self.connection:
            await self.connect()
        await self.exchange.publish(
            aio_pika.Message(
                body=json.dumps(message).encode(),
                delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
            ),
            routing_key=routing_key,
        )

    async def consume(self, callback: Callable):
        if not self.connection:
            await self.connect()
        await self.queue.consume(callback)

    async def close(self):
        if self.connection:
            await self.connection.close()


rabbitmq = RabbitMQ()

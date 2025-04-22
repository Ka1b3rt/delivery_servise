import asyncio
import json
from datetime import datetime

from aio_pika import Message
from aio_pika.abc import AbstractRobustConnection

from app.core.rabbitmq import get_rabbitmq_connection
from app.external.exchange_rate import get_usd_to_rub_rate
from app.repository.crud.parcel import ParcelCRUDRepository


async def process_message(message: Message):
    try:
        rate: float = await get_usd_to_rub_rate()
        await ParcelCRUDRepository.set_delivery_price(rate)
        await message.ack()
    except Exception as e:
        await message.nack(requeue=True)


async def main():
    connection: AbstractRobustConnection = await get_rabbitmq_connection()
    channel = await connection.channel()
    await channel.set_qos(prefetch_count=1)

    queue = await channel.declare_queue(
        "update_exchange_rate",
        durable=True,
    )

    exchange = await channel.declare_exchange(
        "delivery_service",
        type="direct",
        durable=True,
    )

    await queue.bind(exchange, "update_exchange_rate")

    async def schedule_task():
        while True:
            message = Message(
                body=json.dumps({"timestamp": datetime.now().isoformat()}).encode(),
                delivery_mode=2,  
            )
            await exchange.publish(
                message,
                routing_key="update_exchange_rate",
            )
            await asyncio.sleep(300) 

    await asyncio.gather(
        queue.consume(process_message),
        schedule_task(),
    )


if __name__ == "__main__":
    asyncio.run(main()) 
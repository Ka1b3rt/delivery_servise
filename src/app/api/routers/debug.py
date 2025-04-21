from datetime import datetime
import json

from fastapi import APIRouter
from aio_pika import Message

from app.core.rabbitmq import get_rabbitmq_connection

router = APIRouter()

@router.get("/update_rate")
async def update_exchange_rate():
    connection = await get_rabbitmq_connection()
    channel = await connection.channel()
    exchange = await channel.get_exchange("delivery_service")
    
    message = Message(
        body=json.dumps({"timestamp": datetime.now().isoformat()}).encode(),
        delivery_mode=2,  # persistent
    )
    
    await exchange.publish(
        message,
        routing_key="update_exchange_rate",
    )
    
    return {"status": "message sent"}

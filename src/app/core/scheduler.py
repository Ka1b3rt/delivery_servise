import asyncio
from datetime import datetime

from app.core.rabbitmq import rabbitmq
from app.external.exchange_rate import ExchangeRate
from app.repository.crud.parcel import ParcelCRUDRepository


async def schedule_delivery_cost_update():
    while True:
        try:
            rate: float = ExchangeRate.get_USD_to_RUB()
            await ParcelCRUDRepository.set_delivery_price(rate)
            print(f"Exchange rate = {rate} at {datetime.now()}")
        except Exception as e:
            print(f"Error updating delivery cost: {e}")

        await asyncio.sleep(300)  # 5 minutes


async def start_scheduler():
    await rabbitmq.connect()
    asyncio.create_task(schedule_delivery_cost_update())

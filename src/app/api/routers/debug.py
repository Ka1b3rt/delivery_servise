from app.external.exchange_rate import ExchangeRate
from app.repository.crud.parcel import ParcelCRUDRepository
from fastapi import APIRouter

router = APIRouter()


@router.get("/update_rate")
async def update_exchange_rate():
    rate: float = ExchangeRate.get_USD_to_RUB()
    await ParcelCRUDRepository.set_delivery_price(rate)
    return {"rate": rate}

import httpx
from typing import Optional


class ExchangeRate:
    URL = "https://www.cbr-xml-daily.ru/daily_json.js"
    _cached_rate: Optional[float] = None
    _last_update: Optional[float] = None
    CACHE_TTL = 300  # 5 минут

    @staticmethod
    async def _fetch_data() -> dict:
        async with httpx.AsyncClient() as client:
            try:
                resp = await client.get(ExchangeRate.URL)
                resp.raise_for_status()
                return resp.json()
            except httpx.RequestError as e:
                print(f"Error fetching exchange rate: {e}")
                return None

    @staticmethod
    async def get_USD_to_RUB() -> float:
        import time
        current_time = time.time()

        # Если есть кэшированное значение и оно не устарело, возвращаем его
        if (ExchangeRate._cached_rate is not None and 
            ExchangeRate._last_update is not None and 
            current_time - ExchangeRate._last_update < ExchangeRate.CACHE_TTL):
            return ExchangeRate._cached_rate

        # Получаем новые данные
        data = await ExchangeRate._fetch_data()
        if data is None:
            # Если не удалось получить новые данные, возвращаем кэшированное значение
            if ExchangeRate._cached_rate is not None:
                return ExchangeRate._cached_rate
            raise ValueError("Failed to fetch exchange rate and no cached value available")

        # Обновляем кэш
        ExchangeRate._cached_rate = data['Valute']['USD']['Value']
        ExchangeRate._last_update = current_time
        return ExchangeRate._cached_rate

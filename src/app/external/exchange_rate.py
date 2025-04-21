import httpx


class ExchangeRate:
    URL = "https://www.cbr-xml-daily.ru/daily_json.js"

    @staticmethod
    def _fetch_data() -> dict:
        with httpx.Client() as client:
            resp = client.get(ExchangeRate.URL)
            resp.raise_for_status()
            return resp.json()

    @staticmethod
    def get_USD_to_RUB() -> float:
        data = ExchangeRate._fetch_data()
        return data['Valute']['USD']['Value']

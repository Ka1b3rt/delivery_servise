import pytest
from httpx import Client

API_URL = "http://127.0.0.1:3000"


@pytest.fixture
def http_client():
    with Client() as client:
        yield client


class TestApi:
    def setup_method(self):
        self.parcel = {"name": "FuckMachine", "weight": 9, "type_id": 2, "cost": 1000}

    def add_parcel(self, http_client):
        route = "/parcel"

        resp = http_client.request(method="POST", url=API_URL + route, json=self.parcel)
        return resp

    def get_parcels(self, http_client):
        route = "/parcel"

        resp = http_client.request(
            method="GET",
            url=API_URL + route,
        )
        return resp

    def test_add_parcel(self, http_client):
        resp = self.add_parcel(http_client)

        assert resp.status_code == 200

        assert len(resp.json()) == 1
        assert "id" in resp.json().keys()

    def test_get_parcels(self, http_client):
        for _ in range(3):
            self.add_parcel(http_client)

        resp = self.get_parcels(http_client)

        assert resp.status_code == 200

        # Количество посылок в списке ответа
        assert len(resp.json()) == 3

        parcel: dict = resp.json().pop()
        # Количество полей в посылке
        assert len(parcel) == 9
        # На выходе то-же что и на входе
        assert all(p in parcel.items() for p in self.parcel.items())

    def test_get_parcel_types(self, http_client):
        route = "/parcel_types"
        resp = http_client.request(
            method="GET",
            url=API_URL + route,
        )

        expected_body = [
            {"id": 1, "type": "wear"},
            {"id": 2, "type": "electronics"},
            {"id": 3, "type": "other"},
        ]

        assert resp.status_code == 200
        assert len(resp.json()) == 3
        assert resp.json() == expected_body

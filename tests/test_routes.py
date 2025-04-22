import uuid
from datetime import datetime
from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.models.parcel import TypeType
from app.schemas.schemas import AddParcel

client = TestClient(app)


@pytest.fixture
def mock_uuid():
    return uuid.UUID("12345678-1234-5678-1234-567812345678")


@pytest.fixture
def mock_parcels():
    return [
        {
            "id": 1,
            "name": "Test Parcel 1",
            "weight": 1.5,
            "type_id": 1,
            "cost": 100.00,
            "user_id": "12345678-1234-5678-1234-567812345678",
            "delivery_price": 10.00,
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "id": 2,
            "name": "Test Parcel 2",
            "weight": 2.5,
            "type_id": 2,
            "cost": 200.00,
            "user_id": "12345678-1234-5678-1234-567812345678",
            "delivery_price": 20.00,
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]


@pytest.fixture
def mock_parcel_types():
    return [
        {"id": 1, "type": TypeType.CLOTHING},
        {"id": 2, "type": TypeType.ELECTRONICS},
        {"id": 3, "type": TypeType.OTHER},
    ]


@patch("app.api.routes.get_current_user_id")
@patch("app.repository.crud.parcel.ParcelCRUDRepository.get_all")
async def test_get_parcels(mock_get_all, mock_get_user_id, mock_parcels, mock_uuid):
    mock_get_user_id.return_value = mock_uuid
    mock_get_all.return_value = mock_parcels

    response = client.get("/parcel")
    assert response.status_code == 200
    assert len(response.json()) == len(mock_parcels)
    assert response.json()[0]["name"] == mock_parcels[0]["name"]
    assert response.json()[1]["name"] == mock_parcels[1]["name"]
    mock_get_user_id.assert_called_once()
    mock_get_all.assert_called_once_with(mock_uuid)


@patch("app.api.routes.get_current_user_id")
@patch("app.repository.crud.parcel.ParcelCRUDRepository.add")
async def test_add_parcel(mock_add, mock_get_user_id, mock_uuid):
    test_parcel = {
        "name": "New Parcel",
        "weight": 1.5,
        "type_id": 1,
        "cost": 100.00,
    }
    mock_get_user_id.return_value = mock_uuid
    mock_add.return_value = {"id": 1}

    response = client.post("/parcel", json=test_parcel)

    assert response.status_code == 201
    assert response.json() == {"id": 1}

    mock_get_user_id.assert_called_once()
    mock_add.assert_called_once_with(
        AddParcel(**test_parcel),
        mock_uuid,
    )


@patch("app.repository.crud.parcel.ParcelCRUDRepository.get_types")
async def test_get_parcel_types(mock_get_types, mock_parcel_types):
    mock_get_types.return_value = mock_parcel_types

    response = client.get("/parcel_types")

    assert response.status_code == 200
    assert len(response.json()) == len(mock_parcel_types)
    assert response.json()[0]["type"] == mock_parcel_types[0]["type"]
    assert response.json()[1]["type"] == mock_parcel_types[1]["type"]
    assert response.json()[2]["type"] == mock_parcel_types[2]["type"]

    mock_get_types.assert_called_once() 
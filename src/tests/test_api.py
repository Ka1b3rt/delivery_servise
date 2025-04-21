# import pytest
# import pytest_asyncio
# from httpx import AsyncClient
# import os
#
# from app.repository.crud.parcel import ParcelCRUDRepository
# from app.repository.crud.user import UserCRUDRepository
# from app.core.database import async_db
# from app.schemas.schemas import AddParcel
#
# import sys, asyncio
#
# @pytest_asyncio.fixture
# async def async_session():
#     async with async_db.session_factory() as session:
#         yield session
#
#
# @pytest.mark.asyncio
# async def test_parcel_add(async_session):
#     p = {
#         "name": "FuckMachine",
#         "weight": 9,
#         "type_id": 2,
#         "cost": 1000
#     }
#     parcel_repo = ParcelCRUDRepository(async_session)
#     user_repo = UserCRUDRepository(async_session)
#
#     user = await user_repo.add_user_session()
#     user_session = user.session_id
#     parcel_resp = await parcel_repo.create_parcel(
#         AddParcel.model_validate(p), user
#     )
#
#     print(parcel_resp, user_session)
#
# @pytest.mark.asyncio
# async def test_2(async_session):
#     parcel_repo = ParcelCRUDRepository(async_session)
#     user_repo = UserCRUDRepository(async_session)
#     user = await user_repo.add_user_session()
#
#     print(user.session_id)
#

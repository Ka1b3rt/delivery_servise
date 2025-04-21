from fastapi import FastAPI

from app.api.middleware import UserSessionMiddleware
from app.api.routers import debug, parcels


def get_app():
    app = FastAPI()
    app.include_router(parcels.router, tags=["parcels"])
    app.include_router(debug.router, tags=["debug"])
    app.add_middleware(UserSessionMiddleware)
    return app

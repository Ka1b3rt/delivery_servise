from app.api.middleware import UserSessionMiddleware
from app.api.routers import debug, parcels
from app.core.scheduler import start_scheduler
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def get_app():
    app = FastAPI()

    # Настройки CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # В продакшене заменить на конкретные домены
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(parcels.router, tags=["parcels"])
    app.include_router(debug.router, tags=["debug"])
    app.add_middleware(UserSessionMiddleware)

    @app.on_event("startup")
    async def startup_event():
        await start_scheduler()

    return app

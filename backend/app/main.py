from fastapi import FastAPI

from app.api.router import api_router
from app.api.routes.redirect import router as redirect_router
from app.core.config import settings


def create_application() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        debug=settings.debug,
    )
    app.include_router(api_router, prefix=settings.api_v1_prefix)
    app.include_router(redirect_router, tags=["redirect"])
    return app


app = create_application()


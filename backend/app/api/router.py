from fastapi import APIRouter

from app.api.routes.health import router as health_router
from app.api.routes.urls import router as urls_router

api_router = APIRouter()
api_router.include_router(health_router, tags=["health"])
api_router.include_router(urls_router, prefix="/urls", tags=["urls"])


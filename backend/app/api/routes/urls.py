from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.db.base import get_db
from app.schemas.url import ShortenURLRequest, ShortenURLResponse, URLListResponse
from app.services.url_service import URLService

router = APIRouter()


@router.get(
    "/",
    response_model=URLListResponse,
    summary="Get all shortened URLs",
)
async def get_urls(db: AsyncSession = Depends(get_db)) -> URLListResponse:
    urls = await URLService().get_all(db)
    return URLListResponse(urls=[
        ShortenURLResponse(
            id=url.id,
            original_url=url.original_url,
            short_code=url.short_code,
            short_url=f"{settings.base_url}/{url.short_code}",
        )
        for url in urls
    ])


@router.post(
    "/shorten",
    response_model=ShortenURLResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a shortened URL",
)
async def shorten_url(
    payload: ShortenURLRequest,
    db: AsyncSession = Depends(get_db),
) -> ShortenURLResponse:
    return await URLService().shorten(payload, db)

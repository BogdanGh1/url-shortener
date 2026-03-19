from fastapi import APIRouter, Depends, HTTPException, status
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.db.base import get_db
from app.db.cache import get_cache
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
    cache: Redis = Depends(get_cache),
) -> ShortenURLResponse:
    return await URLService().shorten(payload, db, cache)


@router.delete(
    "/{short_code}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a shortened URL",
)
async def delete_url(
    short_code: str,
    db: AsyncSession = Depends(get_db),
    cache: Redis = Depends(get_cache),
) -> None:
    deleted = await URLService().delete_by_short_code(short_code, db, cache)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Short code not found")

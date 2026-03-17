from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.base import get_db
from app.schemas.url import ShortenURLRequest, ShortenURLResponse
from app.services.url_service import URLService

router = APIRouter()


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

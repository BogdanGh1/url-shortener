from fastapi import APIRouter, status

from app.schemas.url import ShortenURLRequest, ShortenURLResponse
from app.services.url_service import URLService

router = APIRouter()


@router.post(
    "/shorten",
    response_model=ShortenURLResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a shortened URL",
)
async def shorten_url(payload: ShortenURLRequest) -> ShortenURLResponse:
    return URLService().shorten(payload)


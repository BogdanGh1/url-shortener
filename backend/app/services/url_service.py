import secrets
import string

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.models.url import URL
from app.schemas.url import ShortenURLRequest, ShortenURLResponse

_ALPHABET = string.ascii_letters + string.digits


class URLService:
    async def shorten(self, payload: ShortenURLRequest, db: AsyncSession) -> ShortenURLResponse:
        short_code = "".join(secrets.choice(_ALPHABET) for _ in range(settings.short_code_length))
        url = URL(original_url=str(payload.original_url), short_code=short_code)
        db.add(url)
        await db.commit()
        await db.refresh(url)
        return ShortenURLResponse(
            id=url.id,
            original_url=url.original_url,
            short_code=url.short_code,
            short_url=f"{settings.base_url}/{url.short_code}",
        )

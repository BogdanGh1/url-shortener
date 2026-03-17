import secrets
import string

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.models.url import URL
from app.schemas.url import ShortenURLRequest, ShortenURLResponse

_ALPHABET = string.ascii_letters + string.digits


class URLService:
    async def get_all(self, db: AsyncSession) -> list[URL]:
        result = await db.execute(select(URL))
        return list(result.scalars().all())

    async def delete_by_short_code(self, short_code: str, db: AsyncSession) -> bool:
        url = await self.get_by_short_code(short_code, db)
        if url is None:
            return False
        await db.delete(url)
        await db.commit()
        return True

    async def get_by_short_code(self, short_code: str, db: AsyncSession) -> URL | None:
        result = await db.execute(select(URL).where(URL.short_code == short_code))
        return result.scalar_one_or_none()

    async def shorten(self, payload: ShortenURLRequest, db: AsyncSession) -> ShortenURLResponse:
        original_url = str(payload.original_url)
        existing = await db.execute(select(URL).where(URL.original_url == original_url))
        url = existing.scalar_one_or_none()

        if url is None:
            short_code = "".join(secrets.choice(_ALPHABET) for _ in range(settings.short_code_length))
            url = URL(original_url=original_url, short_code=short_code)
            db.add(url)
            await db.commit()
            await db.refresh(url)
        return ShortenURLResponse(
            id=url.id,
            original_url=url.original_url,
            short_code=url.short_code,
            short_url=f"{settings.base_url}/{url.short_code}",
        )

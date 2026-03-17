import secrets
import string

from app.core.config import settings
from app.schemas.url import ShortenURLRequest, ShortenURLResponse

_ALPHABET = string.ascii_letters + string.digits


class URLService:
    def shorten(self, payload: ShortenURLRequest) -> ShortenURLResponse:
        short_code = "".join(secrets.choice(_ALPHABET) for _ in range(settings.short_code_length))
        return ShortenURLResponse(
            original_url=payload.original_url,
            short_code=short_code,
            short_url=f"{settings.base_url}/{short_code}",
        )

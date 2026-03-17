import secrets
import string

from app.core.config import settings
from app.schemas.url import ShortenURLRequest, ShortenURLResponse

_ALPHABET = string.ascii_letters + string.digits
_CODE_LENGTH = 7


class URLService:
    def shorten(self, payload: ShortenURLRequest) -> ShortenURLResponse:
        short_code = "".join(secrets.choice(_ALPHABET) for _ in range(_CODE_LENGTH))
        return ShortenURLResponse(
            original_url=payload.original_url,
            short_code=short_code,
            short_url=f"{settings.base_url}/{short_code}",
        )

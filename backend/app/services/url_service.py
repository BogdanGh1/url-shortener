from app.schemas.url import ShortenURLRequest, ShortenURLResponse


class URLService:
    def shorten(self, payload: ShortenURLRequest) -> ShortenURLResponse:
        short_code = "abc123"
        return ShortenURLResponse(
            original_url=payload.original_url,
            short_code=short_code,
            short_url=f"http://localhost:8000/{short_code}",
        )

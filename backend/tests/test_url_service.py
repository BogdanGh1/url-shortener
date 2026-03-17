import pytest

from app.schemas.url import ShortenURLRequest
from app.services.url_service import URLService, _ALPHABET
from app.core.config import settings


@pytest.mark.asyncio
async def test_shorten_returns_correct_fields(db_session):
    payload = ShortenURLRequest(original_url="https://example.com")
    result = await URLService().shorten(payload, db_session)

    assert result.id is not None
    assert result.short_code != ""
    assert result.original_url == "https://example.com/"
    assert result.short_url == f"{settings.base_url}/{result.short_code}"


@pytest.mark.asyncio
async def test_shorten_code_length(db_session):
    payload = ShortenURLRequest(original_url="https://example.com")
    result = await URLService().shorten(payload, db_session)

    assert len(result.short_code) == settings.short_code_length


@pytest.mark.asyncio
async def test_shorten_code_uses_valid_alphabet(db_session):
    payload = ShortenURLRequest(original_url="https://example.com")
    result = await URLService().shorten(payload, db_session)

    assert all(c in _ALPHABET for c in result.short_code)


@pytest.mark.asyncio
async def test_shorten_generates_unique_codes(db_session):
    payload = ShortenURLRequest(original_url="https://example.com")
    results = [await URLService().shorten(payload, db_session) for _ in range(5)]
    codes = [r.short_code for r in results]

    assert len(set(codes)) == 5

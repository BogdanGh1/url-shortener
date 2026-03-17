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
async def test_shorten_same_url_returns_same_code(db_session):
    payload = ShortenURLRequest(original_url="https://same-url.com")
    result1 = await URLService().shorten(payload, db_session)
    result2 = await URLService().shorten(payload, db_session)

    assert result1.short_code == result2.short_code
    assert result1.id == result2.id


@pytest.mark.asyncio
async def test_shorten_different_urls_return_different_codes(db_session):
    result1 = await URLService().shorten(ShortenURLRequest(original_url="https://foo.com"), db_session)
    result2 = await URLService().shorten(ShortenURLRequest(original_url="https://bar.com"), db_session)

    assert result1.short_code != result2.short_code

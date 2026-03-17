import pytest


@pytest.mark.asyncio
async def test_redirect_valid_short_code(client):
    create = await client.post("/api/v1/urls/shorten", json={"original_url": "https://example.com"})
    short_code = create.json()["short_code"]

    response = await client.get(f"/{short_code}", follow_redirects=False)
    assert response.status_code == 302
    assert response.headers["location"] == "https://example.com/"


@pytest.mark.asyncio
async def test_redirect_unknown_short_code(client):
    response = await client.get("/nonexistent", follow_redirects=False)
    assert response.status_code == 404

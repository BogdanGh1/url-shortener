import pytest


@pytest.mark.asyncio
async def test_shorten_url_returns_201(client):
    response = await client.post("/api/v1/urls/shorten", json={"original_url": "https://example.com"})
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_shorten_url_response_shape(client):
    response = await client.post("/api/v1/urls/shorten", json={"original_url": "https://example.com"})
    data = response.json()

    assert "id" in data
    assert "short_code" in data
    assert "short_url" in data
    assert "original_url" in data


@pytest.mark.asyncio
async def test_shorten_url_invalid_url(client):
    response = await client.post("/api/v1/urls/shorten", json={"original_url": "not-a-url"})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_shorten_url_missing_body(client):
    response = await client.post("/api/v1/urls/shorten", json={})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_get_all_urls_returns_200(client):
    response = await client.get("/api/v1/urls/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_all_urls_response_shape(client):
    response = await client.get("/api/v1/urls/")
    data = response.json()
    assert "urls" in data
    assert isinstance(data["urls"], list)


@pytest.mark.asyncio
async def test_get_all_urls_contains_created(client):
    await client.post("/api/v1/urls/shorten", json={"original_url": "https://example.com"})
    response = await client.get("/api/v1/urls/")
    urls = response.json()["urls"]
    assert len(urls) > 0
    assert all("id" in u and "short_code" in u and "short_url" in u for u in urls)

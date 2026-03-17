from pydantic import BaseModel, HttpUrl


class ShortenURLRequest(BaseModel):
    original_url: HttpUrl


class ShortenURLResponse(BaseModel):
    original_url: HttpUrl
    short_code: str
    short_url: str


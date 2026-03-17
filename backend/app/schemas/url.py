from pydantic import BaseModel, HttpUrl


class ShortenURLRequest(BaseModel):
    original_url: HttpUrl


class ShortenURLResponse(BaseModel):
    id: int
    original_url: str
    short_code: str
    short_url: str

    model_config = {"from_attributes": True}

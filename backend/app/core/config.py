from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "URL Shortener API"
    app_env: str = "development"
    debug: bool = True
    api_v1_prefix: str = "/api/v1"
    base_url: str = "http://localhost:8000"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()


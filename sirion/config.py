from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    api_id: int | None = None
    api_hash: str | None = None
    bot_token: str | None = None
    log_group_id: int | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache()
def get_settings() -> Settings:
    """Return cached settings instance."""
    return Settings()

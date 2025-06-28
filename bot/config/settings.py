from functools import lru_cache
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    api_id: int = Field(..., env="API_ID")
    api_hash: str = Field(..., env="API_HASH")
    bot_token: str = Field(..., env="BOT_TOKEN")
    log_group_id: int | None = Field(None, env="LOG_GROUP_ID")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache()
def get_settings() -> Settings:
    """Return cached settings instance."""
    return Settings()

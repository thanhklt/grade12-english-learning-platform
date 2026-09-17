from functools import lru_cache
from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    app_env: Literal["local", "test", "staging", "production"] = "local"
    database_url: SecretStr
    db_pool_size: int = 5
    db_max_overflow: int = 2


@lru_cache
def get_settings() -> Settings:
    return Settings()

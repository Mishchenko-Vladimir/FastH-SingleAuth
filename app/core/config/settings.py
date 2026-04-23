from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

from .app import SiteConfig, RunConfig, GunicornConfig
from .auth import AdminConfig
from .cache import CacheConfig, RedisConfig
from .db import DataBaseConfig
from .logging import LoggingConfig
from .view_prefix import ViewPrefix


# ...\fastapi-boilerplate\app\
BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    """Настройка приложения"""

    model_config = SettingsConfigDict(
        env_file=(BASE_DIR / ".env.template", BASE_DIR / ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    site: SiteConfig
    run: RunConfig = RunConfig()
    gunicorn: GunicornConfig = GunicornConfig()
    logging: LoggingConfig = LoggingConfig()
    view: ViewPrefix = ViewPrefix()
    db: DataBaseConfig
    admin: AdminConfig
    redis: RedisConfig = RedisConfig()
    cache: CacheConfig


settings = Settings()  # type: ignore

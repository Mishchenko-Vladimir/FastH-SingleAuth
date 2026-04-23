from typing import Literal
from pydantic import BaseModel


class SiteConfig(BaseModel):
    """Конфигурация сайта — домен, протокол, название, базовые URL"""

    site_name: str
    domain: str
    protocol: str = "https"
    environment: Literal["development", "testing", "staging", "production"] = (
        "development"
    )

    # Список разрешенных доменов для кросс-доменных запросов (сайты с которых можно отправлять запросы на наш API)
    allowed_origins: list[str] = [
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:1080",
        "http://localhost:1025",
    ]

    @property
    def base_url(self) -> str:
        return f"{self.protocol}://{self.domain}"


class RunConfig(BaseModel):
    """Конфигурация запуска"""

    host: str = "127.0.0.1"
    port: int = 8000


class GunicornConfig(BaseModel):
    """Конфигурация запуска через gunicorn"""

    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 1
    timeout: int = 900

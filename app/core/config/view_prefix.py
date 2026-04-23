from pydantic import BaseModel


class ViewPrefix(BaseModel):
    """Конфигурация префикса для страниц"""

    home: str = ""
    page_missing: str = "/page-missing"

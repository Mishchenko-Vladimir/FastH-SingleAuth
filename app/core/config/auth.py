from pydantic import BaseModel, SecretStr


class AdminConfig(BaseModel):
    """Конфигурация администратора"""

    admin_panel_url: str = "/admin-panel"

    admin_email: str
    admin_password: SecretStr
    admin_secret_key: SecretStr

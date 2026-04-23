import logging
import secrets

from fastapi import Request
from sqladmin.authentication import AuthenticationBackend
from starlette.responses import RedirectResponse

from core.config import settings

log = logging.getLogger(__name__)


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username = form.get("username")
        password = form.get("password")

        is_valid_user = secrets.compare_digest(
            username or "",
            settings.admin.admin_email,
        )
        is_valid_pass = secrets.compare_digest(
            password or "",
            settings.admin.admin_password.get_secret_value(),
        )

        if is_valid_user and is_valid_pass:
            request.session.update({"authenticated": True})
            return True

        return False

    async def logout(self, request: Request) -> RedirectResponse:
        request.session.clear()
        return RedirectResponse(url="/")

    async def authenticate(self, request: Request) -> bool:
        if request.session.get("authenticated") is True:
            return True
        return False

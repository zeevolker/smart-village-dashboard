from typing import Annotated

from fastapi import Cookie, Depends
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login",
    auto_error=False,
)


def get_token(
    bearer_token: Annotated[
        str | None,
        Depends(oauth2_scheme),
    ] = None,
    cookie_token: Annotated[
        str | None,
        Cookie(alias=settings.COOKIE_NAME),
    ] = None,
) -> str | None:
    """
    Resolve access token from multiple transports.

    Priority:
    1. Authorization Bearer Token
    2. HttpOnly Cookie
    """

    if bearer_token:
        return bearer_token

    if cookie_token:
        return cookie_token

    return None
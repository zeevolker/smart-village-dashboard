from fastapi import Response

from app.core.config import settings


def set_auth_cookie(
    response: Response,
    token: str,
) -> None:
    """
    Set authentication cookie.
    """

    response.set_cookie(
        key=settings.COOKIE_NAME,
        value=token,
        httponly=True,
        secure=settings.COOKIE_SECURE,
        samesite=settings.COOKIE_SAMESITE,
        path=settings.COOKIE_PATH,
        max_age=settings.COOKIE_MAX_AGE,
    )


def clear_auth_cookie(
    response: Response,
) -> None:
    """
    Clear authentication cookie.
    """

    response.delete_cookie(
        key=settings.COOKIE_NAME,
        path=settings.COOKIE_PATH,
    )
from datetime import UTC, datetime, timedelta
from typing import Any

from jose import jwt

from app.core.config import settings

ALGORITHM = settings.ALGORITHM
SECRET_KEY = settings.SECRET_KEY


def create_access_token(
    subject: str,
    expires_delta: timedelta,
) -> str:

    expire = datetime.now(UTC) + expires_delta

    payload: dict[str, Any] = {
        "sub": subject,
        "exp": expire,
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )

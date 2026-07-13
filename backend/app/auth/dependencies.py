from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.jwt import decode_token
from app.auth.token import get_token
from app.database.dependencies import get_db
from app.repositories.user_repository import UserRepository

def get_current_user(
    db: Session = Depends(get_db),
    token: str | None = Depends(get_token),
):
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication credentials were not provided.",
        )
        
    try:
        payload = decode_token(token)

        email = payload["sub"]

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token.",
        ) from exc

    repository = UserRepository(db)

    user = repository.get_by_email(email)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found.",
        )

    return user

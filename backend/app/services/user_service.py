from __future__ import annotations

from datetime import timedelta

from app.core.config import settings

from sqlalchemy.orm import Session

from app.auth.hashing import hash_password, verify_password
from app.auth.jwt import create_access_token
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.core.exceptions import (
    ConflictException,
    UnauthorizedException,
)


class UserService:
    """
    Service for User.
    """

    def __init__(
        self,
        db: Session,
    ) -> None:
        self.repository = UserRepository(db)

    def create_user(
        self,
        user_data: UserCreate,
    ) -> User:
        """
        Create new user.
        """

        existing_user = self.repository.get_by_email(
            user_data.email,
        )

        if existing_user:
            raise ConflictException(
                "Email is already registered.",
            )

        return self.repository.create(
            full_name=user_data.full_name,
            email=user_data.email,
            password_hash=hash_password(
                user_data.password,
            ),
            role=user_data.role,
            is_active=True,
        )

    def get_users(
        self,
    ) -> list[User]:
        """
        Get all users.
        """

        return self.repository.list_all()

    def get_user(
        self,
        user_id: str,
    ) -> User | None:
        """
        Get user by id.
        """

        return self.repository.get_by_id(
            user_id,
        )

    def login(
        self,
        email: str,
        password: str,
    ) -> str:
        """
        Authenticate user.
        """

        user = self.repository.get_by_email(
            email,
        )

        if user is None:
            raise UnauthorizedException(
                "Invalid email or password.",
            )

        if not verify_password(
            password,
            user.password_hash,
        ):
            raise UnauthorizedException(
                "Invalid email or password.",
            )

        return create_access_token(
            subject=user.email,
            expires_delta=timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
            ),
        )
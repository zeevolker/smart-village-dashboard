from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.base_repository import BaseRepository


class UserRepository(
    BaseRepository[User],
):
    """
    Repository for User.
    """

    model = User

    def __init__(
        self,
        db: Session,
    ) -> None:
        super().__init__(
            db,
        )

    def get_by_email(
        self,
        email: str,
    ) -> User | None:
        """
        Get user by email.
        """

        stmt = (
            select(
                User,
            )
            .where(
                User.email == email,
            )
        )

        return self.db.scalar(
            stmt,
        )
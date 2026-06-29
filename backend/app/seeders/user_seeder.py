from __future__ import annotations

from sqlalchemy.orm import Session

from app.auth.hashing import hash_password
from app.enums.user_role import UserRole
from app.models.user import User


class UserSeeder:
    """
    Seeder for default users.
    """

    def __init__(
        self,
        db: Session,
    ) -> None:
        self.db = db

    def run(self) -> None:
        """
        Seed default super admin.
        """

        exists = (
            self.db.query(User)
            .filter(
                User.email == "admin@smartvillage.dev",
            )
            .first()
        )

        if exists:
            print("✓ Super Admin already exists.")
            return

        user = User(
            full_name="Super Administrator",
            email="admin@smartvillage.dev",
            password_hash=hash_password(
                "Admin123!",
            ),
            role=UserRole.SUPER_ADMIN,
            is_active=True,
        )

        self.db.add(
            user,
        )

        self.db.commit()

        print(
            "✓ Super Admin created.",
        )
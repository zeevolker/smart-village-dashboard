from datetime import timedelta

from sqlalchemy.orm import Session

from app.auth.hashing import hash_password, verify_password
from app.auth.jwt import create_access_token
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def create_user(self, user_data: UserCreate) -> User:
        """
        Membuat user baru.
        Password hashing akan ditambahkan pada sprint berikutnya.
        """

        existing_user = self.repository.get_by_email(user_data.email)

        if existing_user:
            raise ValueError("Email is already registered.")

        user = User(
            full_name=user_data.full_name,
            email=user_data.email,
            password_hash=hash_password(user_data.password),
        )

        return self.repository.create(user)

    def get_users(self) -> list[User]:
        return self.repository.get_all()

    def get_user(self, user_id):
        return self.repository.get_by_id(user_id)

    def login(
        self,
        email: str,
        password: str,
    ) -> str:

        user = self.repository.get_by_email(email)

        if not user:
            raise ValueError("Invalid email or password.")

        if not verify_password(
            password,
            user.password_hash,
        ):
            raise ValueError("Invalid email or password.")

        return create_access_token(
            subject=user.email,
            expires_delta=timedelta(minutes=60),
        )

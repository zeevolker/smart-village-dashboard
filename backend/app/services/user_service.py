from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate

from app.auth.hashing import hash_password


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
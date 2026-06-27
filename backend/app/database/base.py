from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class untuk semua model SQLAlchemy.
    """
    pass


# Import semua model DI BAGIAN BAWAH
from app.models.user import User
from app.models.province import Province
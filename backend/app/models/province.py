import uuid

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import BaseModel

from sqlalchemy.orm import relationship


class Province(BaseModel):
    __tablename__ = "provinces"

    code: Mapped[str] = mapped_column(
        String(2),
        unique=True,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )
    
    regencies = relationship(
        "Regency",
        back_populates="province",
        cascade="all, delete-orphan",
    )
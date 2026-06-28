from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel

if TYPE_CHECKING:
    from app.models.regency import Regency


class Province(BaseModel):
    __tablename__ = "provinces"

    code: Mapped[str] = mapped_column(
        String(2),
        unique=True,
        nullable=False,
    )

    bps_code: Mapped[str] = mapped_column(
        String(2),
        unique=True,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    regencies: Mapped[list["Regency"]] = relationship(
        back_populates="province",
        cascade="all, delete-orphan",
    )
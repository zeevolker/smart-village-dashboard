from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel

if TYPE_CHECKING:
    from app.models.citizen import Citizen
    from app.models.district import District


class Village(BaseModel):
    __tablename__ = "villages"

    code: Mapped[str] = mapped_column(
        String(13),
        unique=True,
        nullable=False,
    )

    bps_code: Mapped[str] = mapped_column(
        String(10),
        unique=True,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    district_id: Mapped[str] = mapped_column(
        ForeignKey("districts.id"),
        nullable=False,
    )

    district: Mapped[District] = relationship(
        back_populates="villages",
    )

    citizens: Mapped[list[Citizen]] = relationship(
        back_populates="village",
        cascade="all, delete-orphan",
    )

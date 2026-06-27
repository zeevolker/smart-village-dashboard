from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel

if TYPE_CHECKING:
    from app.models.province import Province
    from app.models.district import District


class Regency(BaseModel):
    __tablename__ = "regencies"

    code: Mapped[str] = mapped_column(
        String(5),
        unique=True,
        nullable=False,
    )

    bps_code: Mapped[str] = mapped_column(
        String(4),
        unique=True,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    province_id: Mapped[str] = mapped_column(
        ForeignKey("provinces.id"),
        nullable=False,
    )

    province: Mapped["Province"] = relationship(
        back_populates="regencies",
    )

    districts: Mapped[list["District"]] = relationship(
        back_populates="regency",
        cascade="all, delete-orphan",
    )
from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel

if TYPE_CHECKING:
    from app.models.village import Village


class Citizen(BaseModel):
    __tablename__ = "citizens"

    nik: Mapped[str] = mapped_column(
        String(16),
        unique=True,
        nullable=False,
        index=True,
    )

    full_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    village_id: Mapped[str] = mapped_column(
        ForeignKey("villages.id"),
        nullable=False,
    )

    village: Mapped[Village] = relationship(
        back_populates="citizens",
    )

from __future__ import annotations

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel


class Household(BaseModel):
    """
    Household model.
    """

    __tablename__ = "households"

    kk_number: Mapped[str] = mapped_column(
        String(16),
        unique=True,
        nullable=False,
        index=True,
    )

    address: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    rt: Mapped[str] = mapped_column(
        String(3),
        nullable=False,
    )

    rw: Mapped[str] = mapped_column(
        String(3),
        nullable=False,
    )

    postal_code: Mapped[str] = mapped_column(
        String(5),
        nullable=False,
    )

    village_id: Mapped[str] = mapped_column(
        ForeignKey(
            "villages.id",
            ondelete="RESTRICT",
        ),
        nullable=False,
    )

    village = relationship(
        "Village",
        back_populates="households",
    )

    citizens = relationship(
        "Citizen",
        back_populates="household",
        cascade="all, delete-orphan",
    )
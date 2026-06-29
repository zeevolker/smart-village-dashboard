from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.enums.gender import Gender
from app.enums.marital_status import MaritalStatus
from app.enums.relationship import RelationshipType
from app.enums.religion import Religion
from app.models.base_model import BaseModel

if TYPE_CHECKING:
    from app.models.household import Household
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

    gender: Mapped[Gender] = mapped_column(
        Enum(Gender),
        nullable=False,
    )

    birth_place: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    birth_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    religion: Mapped[Religion] = mapped_column(
        Enum(Religion),
        nullable=False,
    )

    marital_status: Mapped[MaritalStatus] = mapped_column(
        Enum(MaritalStatus),
        nullable=False,
    )

    occupation: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    phone_number: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    address: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    village_id: Mapped[str] = mapped_column(
        ForeignKey("villages.id"),
        nullable=False,
    )

    village: Mapped["Village"] = relationship(
        back_populates="citizens",
    )

    household_id: Mapped[str | None] = mapped_column(
        ForeignKey(
            "households.id",
            ondelete="SET NULL",
        ),
        nullable=True,
    )

    household: Mapped["Household | None"] = relationship(
        back_populates="citizens",
    )

    relationship_to_head: Mapped[RelationshipType | None] = mapped_column(
        Enum(
            RelationshipType,
            name="relationship_type",
        ),
        nullable=True,
    )
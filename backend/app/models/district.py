import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel

if TYPE_CHECKING:
    from app.models.regency import Regency
    from app.models.village import Village


class District(BaseModel):
    __tablename__ = "districts"

    code: Mapped[str] = mapped_column(
        String(7),
        unique=True,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    regency_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("regencies.id"),
        nullable=False,
    )

    regency: Mapped["Regency"] = relationship(
        back_populates="districts",
    )
    
    villages: Mapped[list["Village"]] = relationship(
        back_populates="district",
        cascade="all, delete-orphan",
    )
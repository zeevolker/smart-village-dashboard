from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel


class Regency(BaseModel):
    __tablename__ = "regencies"

    code: Mapped[str] = mapped_column(
        String(4),
        unique=True,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    province_id = mapped_column(
        ForeignKey("provinces.id"),
        nullable=False,
    )

    province = relationship(
        "Province",
        back_populates="regencies",
    )
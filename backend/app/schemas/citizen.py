from __future__ import annotations

from datetime import date
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from app.enums.gender import Gender
from app.enums.marital_status import MaritalStatus
from app.enums.religion import Religion


class CitizenBase(BaseModel):
    """
    Base schema untuk Citizen.
    """

    nik: str = Field(
        min_length=16,
        max_length=16,
        examples=["3201010101010001"],
    )

    full_name: str = Field(
        max_length=150,
        examples=["Budi Santoso"],
    )

    gender: Gender

    birth_place: str = Field(
        max_length=100,
        examples=["Bogor"],
    )

    birth_date: date

    religion: Religion

    marital_status: MaritalStatus

    occupation: str = Field(
        max_length=100,
        examples=["Petani"],
    )

    phone_number: str | None = Field(
        default=None,
        max_length=20,
        examples=["081234567890"],
    )

    address: str = Field(
        max_length=255,
        examples=["Jl. Raya No. 10"],
    )

    village_id: UUID


class CitizenCreate(CitizenBase):
    """
    Request schema untuk membuat Citizen.
    """

    pass


class CitizenUpdate(BaseModel):
    """
    Request schema untuk update Citizen.
    """

    full_name: str | None = Field(
        default=None,
        max_length=150,
    )

    gender: Gender | None = None

    birth_place: str | None = Field(
        default=None,
        max_length=100,
    )

    birth_date: date | None = None

    religion: Religion | None = None

    marital_status: MaritalStatus | None = None

    occupation: str | None = Field(
        default=None,
        max_length=100,
    )

    phone_number: str | None = Field(
        default=None,
        max_length=20,
    )

    address: str | None = Field(
        default=None,
        max_length=255,
    )

    village_id: UUID | None = None


class CitizenResponse(CitizenBase):
    """
    Response schema.
    """

    id: UUID

    model_config = ConfigDict(
        from_attributes=True,
    )
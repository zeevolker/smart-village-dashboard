from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


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

    village_id: UUID | None = None


class CitizenResponse(CitizenBase):
    """
    Response schema.
    """

    id: UUID

    model_config = ConfigDict(
        from_attributes=True,
    )
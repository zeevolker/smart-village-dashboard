from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class HouseholdBase(BaseModel):
    """
    Base Household schema.
    """

    kk_number: str = Field(
        min_length=16,
        max_length=16,
    )

    address: str = Field(
        max_length=255,
    )

    rt: str = Field(
        min_length=3,
        max_length=3,
    )

    rw: str = Field(
        min_length=3,
        max_length=3,
    )

    postal_code: str = Field(
        min_length=5,
        max_length=5,
    )

    village_id: UUID


class HouseholdCreate(
    HouseholdBase,
):
    """
    Create Household.
    """

    pass


class HouseholdUpdate(
    BaseModel,
):
    """
    Update Household.
    """

    kk_number: str | None = Field(
        default=None,
        min_length=16,
        max_length=16,
    )

    address: str | None = Field(
        default=None,
        max_length=255,
    )

    rt: str | None = Field(
        default=None,
        min_length=3,
        max_length=3,
    )

    rw: str | None = Field(
        default=None,
        min_length=3,
        max_length=3,
    )

    postal_code: str | None = Field(
        default=None,
        min_length=5,
        max_length=5,
    )

    village_id: UUID | None = None


class HouseholdResponse(
    HouseholdBase,
):
    """
    Household response.
    """

    id: UUID

    model_config = ConfigDict(
        from_attributes=True,
    )
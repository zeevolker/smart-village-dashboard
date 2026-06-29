from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel, ConfigDict


class TerritoryBase(BaseModel):
    """
    Base response schema untuk seluruh data wilayah.
    """

    id: UUID
    code: str
    bps_code: str
    name: str

    model_config = ConfigDict(
        from_attributes=True,
    )


class ProvinceResponse(TerritoryBase):
    """
    Province response.
    """

    pass


class RegencyResponse(TerritoryBase):
    """
    Regency response.
    """

    province_id: UUID


class DistrictResponse(TerritoryBase):
    """
    District response.
    """

    regency_id: UUID


class VillageResponse(TerritoryBase):
    """
    Village response.
    """

    district_id: UUID
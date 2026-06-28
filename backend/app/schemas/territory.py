from pydantic import BaseModel, ConfigDict


class TerritoryBase(BaseModel):
    id: str
    code: str
    bps_code: str
    name: str

    model_config = ConfigDict(
        from_attributes=True,
    )


class ProvinceResponse(TerritoryBase):
    pass


class RegencyResponse(TerritoryBase):
    province_id: str


class DistrictResponse(TerritoryBase):
    regency_id: str


class VillageResponse(TerritoryBase):
    district_id: str
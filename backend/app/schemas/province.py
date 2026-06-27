from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ProvinceBase(BaseModel):
    code: str
    name: str


class ProvinceCreate(ProvinceBase):
    pass


class ProvinceUpdate(BaseModel):
    code: str | None = None
    name: str | None = None


class ProvinceResponse(ProvinceBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True)
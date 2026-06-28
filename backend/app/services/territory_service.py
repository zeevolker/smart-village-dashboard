from sqlalchemy import select
from sqlalchemy.orm import Session

from app.repositories.district_repository import DistrictRepository
from app.repositories.province_repository import ProvinceRepository
from app.repositories.regency_repository import RegencyRepository
from app.repositories.village_repository import VillageRepository
from app.schemas.pagination import PaginationResult
from app.services.base_service import BaseService


class TerritoryService(BaseService):
    def __init__(
        self,
        db: Session,
    ):
        self.provinces = ProvinceRepository(db)
        self.regencies = RegencyRepository(db)
        self.districts = DistrictRepository(db)
        self.villages = VillageRepository(db)

        super().__init__(self.provinces)

    def get_provinces(
        self,
        page: int,
        size: int,
    ) -> PaginationResult:

        stmt = select(self.provinces.model).order_by(self.provinces.model.name)

        rows, total, pages = self.provinces.list_paginated(
            stmt,
            page=page,
            size=size,
        )

        return PaginationResult(
            items=rows,
            page=page,
            size=size,
            total=total,
            pages=pages,
        )

    def get_regencies(
        self,
        province_id: str,
    ):
        return self.regencies.get_by_province(province_id)

    def get_districts(
        self,
        regency_id: str,
    ):
        return self.districts.get_by_regency(regency_id)

    def get_villages(
        self,
        district_id: str,
    ):
        return self.villages.get_by_district(district_id)

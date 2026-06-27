from uuid import UUID

from sqlalchemy.orm import Session

from app.models.province import Province
from app.repositories.province_repository import ProvinceRepository
from app.schemas.province import ProvinceCreate, ProvinceUpdate


class ProvinceService:
    def __init__(self, db: Session):
        self.repository = ProvinceRepository(db)

    def create_province(
        self,
        province_data: ProvinceCreate,
    ) -> Province:

        if self.repository.get_by_code(province_data.code):
            raise ValueError("Province code already exists.")

        if self.repository.get_by_name(province_data.name):
            raise ValueError("Province name already exists.")

        province = Province(
            code=province_data.code,
            name=province_data.name,
        )

        return self.repository.create(province)

    def get_provinces(self) -> list[Province]:
        return self.repository.get_all()

    def get_province(
        self,
        province_id: UUID,
    ) -> Province | None:
        return self.repository.get_by_id(province_id)
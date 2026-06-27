from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.province import Province
from app.repositories.base_repository import BaseRepository


class ProvinceRepository(BaseRepository[Province]):
    def __init__(self, db: Session):
        super().__init__(db, Province)

    def get_by_code(self, code: str) -> Province | None:
        stmt = select(Province).where(Province.code == code)
        result = self.db.execute(stmt)

        return result.scalar_one_or_none()

    def get_by_name(self, name: str) -> Province | None:
        stmt = select(Province).where(Province.name == name)
        result = self.db.execute(stmt)

        return result.scalar_one_or_none()
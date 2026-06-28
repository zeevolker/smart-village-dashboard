from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.district import District


class DistrictRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_regency(
        self,
        regency_id: str,
    ) -> list[District]:

        stmt = (
            select(District)
            .where(
                District.regency_id == regency_id
            )
            .order_by(
                District.name
            )
        )

        return list(
            self.db.scalars(stmt)
        )
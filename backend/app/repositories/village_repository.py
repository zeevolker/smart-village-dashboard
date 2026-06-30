from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.village import Village


class VillageRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_district(
        self,
        district_id: str,
    ) -> list[Village]:

        stmt = (
            select(Village)
            .where(Village.district_id == district_id)
            .order_by(Village.name)
        )

        return list(self.db.scalars(stmt))
    
    def get_all(self) -> list[Village]:
        """
        Get all villages ordered by code.
        """

        stmt = (
            select(Village)
            .order_by(Village.code)
        )

        return list(
            self.db.scalars(stmt)
        )

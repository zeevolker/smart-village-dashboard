from sqlalchemy import select

from app.models.regency import Regency
from app.repositories.base_repository import BaseRepository


class RegencyRepository(
    BaseRepository[Regency]
):
    model = Regency

    def get_by_province(
        self,
        province_id: str,
    ):

        stmt = (
            select(Regency)
            .where(
                Regency.province_id == province_id
            )
            .order_by(
                Regency.name
            )
        )

        return list(
            self.db.scalars(stmt)
        )
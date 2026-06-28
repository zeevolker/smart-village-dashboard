from __future__ import annotations

from sqlalchemy import or_, select

from app.models.citizen import Citizen
from app.repositories.base_repository import BaseRepository


class CitizenRepository(BaseRepository[Citizen]):
    """
    Repository untuk data Citizen.
    """

    model = Citizen

    def search(
        self,
        keyword: str,
        *,
        page: int = 1,
        size: int = 20,
    ):
        """
        Cari citizen berdasarkan NIK atau nama.
        """

        stmt = (
            select(Citizen)
            .where(
                or_(
                    Citizen.nik.ilike(f"%{keyword}%"),
                    Citizen.full_name.ilike(f"%{keyword}%"),
                )
            )
            .order_by(Citizen.full_name)
        )

        return self.list_paginated(
            stmt,
            page=page,
            size=size,
        )

    def get_by_nik(
        self,
        nik: str,
    ) -> Citizen | None:
        """
        Ambil citizen berdasarkan NIK.
        """

        stmt = select(Citizen).where(Citizen.nik == nik)

        return self.db.scalar(stmt)

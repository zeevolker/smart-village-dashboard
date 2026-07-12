from __future__ import annotations

from sqlalchemy import or_, select

from app.models.citizen import Citizen
from app.repositories.base_repository import BaseRepository

from app.enums.gender import Gender
from app.enums.religion import Religion
from app.enums.marital_status import MaritalStatus


class CitizenRepository(BaseRepository[Citizen]):
    """
    Repository untuk data Citizen.
    """

    model = Citizen

    def search(
        self,
        keyword: str | None = None,
        gender: Gender | None = None,
        religion: Religion | None = None,
        marital_status: MaritalStatus | None = None,
        *,
        page: int = 1,
        size: int = 20,
    ) -> tuple[list[Citizen], int, int]:
        """
        Cari citizen berdasarkan NIK atau nama.
        """

        keyword = keyword.strip() if keyword else None

        stmt = select(Citizen)

        if keyword:
            stmt = stmt.where(
                or_(
                    Citizen.nik.ilike(f"%{keyword}%"),
                    Citizen.full_name.ilike(f"%{keyword}%"),
                )
            )
            
        if gender:
            stmt = stmt.where(
                Citizen.gender == gender,
            )

        if religion:
            stmt = stmt.where(
                Citizen.religion == religion,
            )

        if marital_status:
            stmt = stmt.where(
                Citizen.marital_status == marital_status,
            )

        stmt = stmt.order_by(Citizen.full_name)

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

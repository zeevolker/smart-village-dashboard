from __future__ import annotations

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.household import Household
from app.repositories.base_repository import BaseRepository


class HouseholdRepository(
    BaseRepository[Household],
):
    """
    Repository for Household.
    """

    model = Household

    def __init__(
        self,
        db: Session,
    ) -> None:
        super().__init__(
            db,
        )

    def get_by_kk_number(
        self,
        kk_number: str,
    ) -> Household | None:
        """
        Get household by KK number.
        """

        stmt = (
            select(
                Household,
            )
            .where(
                Household.kk_number == kk_number,
            )
        )

        return self.db.scalar(
            stmt,
        )
        
    def search(
        self,
        keyword: str,
        page: int,
        size: int,
    ) -> tuple[
        list[Household],
        int,
        int,
    ]:
        """
        Search households by KK number.
        """

        stmt = select(
            Household,
        )

        if keyword:
            stmt = stmt.where(
                func.lower(
                    Household.kk_number,
                ).contains(
                    keyword.lower(),
                )
            )

        return self.list_paginated(
            stmt,
            page=page,
            size=size,
        )
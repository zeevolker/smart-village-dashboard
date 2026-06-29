from __future__ import annotations

from sqlalchemy.orm import Session

from app.core.exceptions import (
    ConflictException,
    NotFoundException,
)
from app.models.household import Household
from app.repositories.household_repository import HouseholdRepository
from app.schemas.household import (
    HouseholdCreate,
    HouseholdUpdate,
)
from app.schemas.pagination import PaginationResult
from app.services.base_service import BaseService


class HouseholdService(
    BaseService[
        Household,
        HouseholdRepository,
    ]
):
    """
    Business logic for Household.
    """

    def __init__(
        self,
        db: Session,
    ) -> None:
        repository = HouseholdRepository(
            db,
        )

        super().__init__(
            repository,
        )

    # -----------------------------
    # Query
    # -----------------------------

    def get(
        self,
        household_id: str,
    ) -> Household:

        household = self.repository.get_by_id(
            household_id,
        )

        if household is None:
            raise NotFoundException(
                "Household not found.",
            )

        return household

    def list(
        self,
        page: int,
        size: int,
    ) -> PaginationResult[Household]:

        rows, total, pages = self.repository.list_paginated(
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

    # -----------------------------
    # Command
    # -----------------------------

    def create(
        self,
        payload: HouseholdCreate,
    ) -> Household:

        exists = self.repository.get_by_kk_number(
            payload.kk_number,
        )

        if exists:
            raise ConflictException(
                "KK number already exists.",
            )

        return self.repository.create(
            **payload.model_dump(),
        )

    def update(
        self,
        household_id: str,
        payload: HouseholdUpdate,
    ) -> Household:

        household = self.get(
            household_id,
        )

        data = payload.model_dump(
            exclude_unset=True,
            exclude_none=True,
        )

        if (
            "kk_number" in data
            and data["kk_number"] != household.kk_number
        ):
            exists = self.repository.get_by_kk_number(
                data["kk_number"],
            )

            if exists:
                raise ConflictException(
                    "KK number already exists.",
                )

        return self.repository.update(
            household,
            **data,
        )

    def delete(
        self,
        household_id: str,
    ) -> None:

        household = self.get(
            household_id,
        )

        self.repository.delete(
            household,
        )
        
    def search(
        self,
        keyword: str,
        page: int,
        size: int,
    ) -> PaginationResult[Household]:
        """
        Search households by KK number.
        """

        rows, total, pages = self.repository.search(
            keyword=keyword,
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
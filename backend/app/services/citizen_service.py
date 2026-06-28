from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.exceptions import (
    ConflictException,
    NotFoundException,
)

from app.models.citizen import Citizen

from app.repositories.citizen_repository import CitizenRepository

from app.schemas.citizen import (
    CitizenCreate,
    CitizenUpdate,
)

from app.services.base_service import BaseService


class CitizenService(
    BaseService[
        Citizen,
        CitizenRepository,
    ]
):
    """
    Business logic Citizen.
    """

    def __init__(
        self,
        db: Session,
    ):
        repository = CitizenRepository(db)

        super().__init__(repository)

    # -----------------------------
    # Query
    # -----------------------------

    def get(
        self,
        citizen_id: str,
    ) -> Citizen:

        citizen = self.repository.get_by_id(
            citizen_id
        )

        if citizen is None:
            raise NotFoundException(
                "Citizen not found."
            )

        return citizen

    def search(
        self,
        keyword: str,
        page: int,
        size: int,
    ):

        return self.repository.search(
            keyword,
            page=page,
            size=size,
        )

    # -----------------------------
    # Command
    # -----------------------------

    def create(
        self,
        payload: CitizenCreate,
    ) -> Citizen:

        exists = self.repository.get_by_nik(
            payload.nik,
        )

        if exists:
            raise ConflictException(
                "NIK already exists."
            )

        return self.repository.create(
            **payload.model_dump(),
        )

    def update(
        self,
        citizen_id: str,
        payload: CitizenUpdate,
    ) -> Citizen:

        citizen = self.get(
            citizen_id,
        )

        data = payload.model_dump(
            exclude_unset=True,
            exclude_none=True,
        )

        return self.repository.update(
            citizen,
            **data,
        )

    def delete(
        self,
        citizen_id: str,
    ) -> None:

        citizen = self.get(
            citizen_id,
        )

        self.repository.delete(
            citizen,
        )
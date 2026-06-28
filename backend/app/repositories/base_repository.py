from __future__ import annotations

from math import ceil
from typing import Generic, TypeVar, Any

from sqlalchemy import Select, func, select
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):

    model: type[ModelType]

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def query(self) -> Select:
        return select(self.model)

    def get_by_id(
        self,
        id_: str,
    ) -> ModelType | None:

        stmt = (
            self.query()
            .where(
                self.model.id == id_
            )
        )

        return self.db.scalar(stmt)

    def count(self) -> int:

        stmt = (
            select(func.count())
            .select_from(self.model)
        )

        return self.db.scalar(stmt) or 0

    def list_all(
        self,
        stmt: Select | None = None,
    ) -> list[ModelType]:

        if stmt is None:
            stmt = self.query()

        return list(
            self.db.scalars(stmt)
        )

    def list_paginated(
        self,
        stmt: Select | None = None,
        *,
        page: int = 1,
        size: int = 20,
    ) -> tuple[list[ModelType], int, int]:

        if stmt is None:
            stmt = self.query()

        page = max(page, 1)
        size = max(size, 1)

        total = (
            self.db.scalar(
                select(func.count())
                .select_from(stmt.subquery())
            )
            or 0
        )

        rows = list(
            self.db.scalars(
                stmt.offset(
                    (page - 1) * size
                ).limit(size)
            )
        )

        pages = (
            ceil(total / size)
            if total
            else 0
        )

        return (
            rows,
            total,
            pages,
        )
        
    def create(
        self,
        **data: Any,
    ) -> ModelType:
        """
        Membuat data baru.
        """

        instance = self.model(
            **data,
        )

        self.db.add(instance)

        self.db.commit()

        self.db.refresh(instance)

        return instance
    
    def update(
        self,
        instance: ModelType,
        **data: Any,
    ) -> ModelType:
        """
        Memperbarui data.
        """

        for field, value in data.items():

            setattr(
                instance,
                field,
                value,
            )

        self.db.commit()

        self.db.refresh(instance)

        return instance
    
    def delete(
        self,
        instance: ModelType,
    ) -> None:
        """
        Menghapus data.
        """

        self.db.delete(instance)

        self.db.commit()
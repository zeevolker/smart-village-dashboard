from __future__ import annotations

from typing import Generic, TypeVar

ModelType = TypeVar("ModelType")
RepositoryType = TypeVar("RepositoryType")


class BaseService(
    Generic[
        ModelType,
        RepositoryType,
    ]
):
    """
    Base service untuk seluruh module.
    """

    def __init__(
        self,
        repository: RepositoryType,
    ) -> None:
        self.repository = repository

    def list_all(
        self,
    ) -> list[ModelType]:
        """
        Mengambil seluruh data.
        """

        return self.repository.list_all()

    def get_by_id(
        self,
        id_: str,
    ) -> ModelType | None:
        """
        Mengambil data berdasarkan id.
        """

        return self.repository.get_by_id(id_)

    def count(
        self,
    ) -> int:
        """
        Menghitung total data.
        """

        return self.repository.count()
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
    ):
        self.repository = repository

    def get_all(self):

        return self.repository.get_all()

    def get_by_id(
        self,
        id_: str,
    ):

        return self.repository.get_by_id(id_)

    def count(self):

        return self.repository.count()

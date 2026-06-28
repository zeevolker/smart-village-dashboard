from __future__ import annotations

from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PaginationParams(BaseModel):
    """
    Query parameters untuk pagination.
    """

    page: int = Field(
        default=1,
        ge=1,
    )

    size: int = Field(
        default=20,
        ge=1,
        le=100,
    )


class PaginationResult(
    BaseModel,
    Generic[T],
):
    """
    Standard paginated response.
    """

    items: list[T]

    page: int

    size: int

    total: int

    pages: int

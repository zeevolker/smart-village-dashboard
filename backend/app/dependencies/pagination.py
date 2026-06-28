from fastapi import Query

from app.schemas.pagination import PaginationParams


def get_pagination() -> PaginationParams:
    """
    Dependency untuk pagination.
    """

    return PaginationParams(
        page=Query(
            default=1,
            ge=1,
        ),
        size=Query(
            default=20,
            ge=1,
            le=100,
        ),
    )

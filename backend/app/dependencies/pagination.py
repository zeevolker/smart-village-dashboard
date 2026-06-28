from fastapi import Query

from app.schemas.pagination import PaginationParams


def get_pagination(
    page: int = Query(
        default=1,
        ge=1,
        description="Page number",
    ),
    size: int = Query(
        default=20,
        ge=1,
        le=100,
        description="Items per page",
    ),
) -> PaginationParams:
    """
    Dependency untuk pagination.
    """

    return PaginationParams(
        page=page,
        size=size,
    )
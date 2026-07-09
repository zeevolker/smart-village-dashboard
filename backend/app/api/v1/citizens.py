from fastapi import APIRouter, Depends, Path, Query

from app.dependencies.citizen import get_citizen_service
from app.dependencies.pagination import get_pagination
from app.schemas.citizen import (
    CitizenCreate,
    CitizenResponse,
    CitizenUpdate,
)
from app.schemas.pagination import (
    PaginationParams,
    PaginationResult,
)
from app.schemas.response import (
    ApiResponse,
    success_response,
)
from app.services.citizen_service import CitizenService

router = APIRouter(
    prefix="/citizens",
    tags=["Citizens"],
)


@router.get(
    "",
    response_model=ApiResponse[PaginationResult[CitizenResponse]],
    summary="List citizens with pagination",
)
def get_citizens(
    pagination: PaginationParams = Depends(get_pagination),
    q: str | None = Query(
        default=None,
        description="Search by NIK or full name",
    ),
    service: CitizenService = Depends(get_citizen_service),
):
    return success_response(
        service.search(
            keyword=q,
            page=pagination.page,
            size=pagination.size,
        )
    )


@router.get(
    "/{citizen_id}",
    response_model=ApiResponse[CitizenResponse],
    summary="Get citizen",
)
def get_citizen(
    citizen_id: str = Path(
        ...,
        description="Citizen ID",
    ),
    service: CitizenService = Depends(get_citizen_service),
):
    return success_response(
        service.get(
            citizen_id,
        )
    )


@router.post(
    "",
    response_model=ApiResponse[CitizenResponse],
    summary="Create citizen",
)
def create_citizen(
    payload: CitizenCreate,
    service: CitizenService = Depends(get_citizen_service),
):
    return success_response(
        service.create(
            payload,
        ),
        message="Citizen created.",
    )


@router.put(
    "/{citizen_id}",
    response_model=ApiResponse[CitizenResponse],
    summary="Update citizen",
)
def update_citizen(
    payload: CitizenUpdate,
    citizen_id: str = Path(
        ...,
        description="Citizen ID",
    ),
    service: CitizenService = Depends(get_citizen_service),
):
    return success_response(
        service.update(
            citizen_id,
            payload,
        ),
        message="Citizen updated.",
    )


@router.delete(
    "/{citizen_id}",
    response_model=ApiResponse[None],
    summary="Delete citizen",
)
def delete_citizen(
    citizen_id: str = Path(
        ...,
        description="Citizen ID",
    ),
    service: CitizenService = Depends(get_citizen_service),
):
    service.delete(
        citizen_id,
    )

    return success_response(
        None,
        message="Citizen deleted.",
    )

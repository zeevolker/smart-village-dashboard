from fastapi import APIRouter, Depends, Path

from app.dependencies.citizen import get_citizen_service
from app.schemas.citizen import (
    CitizenCreate,
    CitizenResponse,
    CitizenUpdate,
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
    response_model=ApiResponse[list[CitizenResponse]],
    summary="List citizens",
)
def get_citizens(
    service: CitizenService = Depends(
        get_citizen_service,
    ),
):
    return success_response(
        service.get_all(),
    )


@router.get(
    "/{citizen_id}",
    response_model=ApiResponse[CitizenResponse],
    summary="Get citizen",
)
def get_citizen(
    citizen_id: str = Path(...),
    service: CitizenService = Depends(
        get_citizen_service,
    ),
):
    return success_response(
        service.get_by_id(
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
    service: CitizenService = Depends(
        get_citizen_service,
    ),
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
    citizen_id: str,
    payload: CitizenUpdate,
    service: CitizenService = Depends(
        get_citizen_service,
    ),
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
    citizen_id: str,
    service: CitizenService = Depends(
        get_citizen_service,
    ),
):
    service.delete(
        citizen_id,
    )

    return success_response(
        None,
        message="Citizen deleted.",
    )

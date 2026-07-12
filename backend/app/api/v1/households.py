from fastapi import APIRouter, Depends, Path, Query

from app.dependencies.household import get_household_service
from app.dependencies.pagination import get_pagination
from app.schemas.household import (
    HouseholdCreate,
    HouseholdResponse,
    HouseholdUpdate,
)
from app.schemas.pagination import (
    PaginationParams,
    PaginationResult,
)
from app.schemas.response import (
    ApiResponse,
    success_response,
)
from app.services.household_service import HouseholdService

router = APIRouter(
    prefix="/households",
    tags=["Households"],
)


@router.get(
    "",
    response_model=ApiResponse[
        PaginationResult[HouseholdResponse]
    ],
    summary="List households with pagination",
)
def get_households(
    pagination: PaginationParams = Depends(
        get_pagination,
    ),
    q: str = Query(
        default="",
        description="Search by KK number",
    ),
    service: HouseholdService = Depends(
        get_household_service,
    ),
):
    return success_response(
        service.search(
            keyword=q,
            page=pagination.page,
            size=pagination.size,
        )
    )


@router.get(
    "/{household_id}",
    response_model=ApiResponse[
        HouseholdResponse
    ],
    summary="Get household",
)
def get_household(
    household_id: str = Path(
        ...,
        description="Household ID",
    ),
    service: HouseholdService = Depends(
        get_household_service,
    ),
):
    return success_response(
        service.get(
            household_id,
        )
    )


@router.post(
    "",
    response_model=ApiResponse[
        HouseholdResponse
    ],
    summary="Create household",
)
def create_household(
    payload: HouseholdCreate,
    service: HouseholdService = Depends(
        get_household_service,
    ),
):
    return success_response(
        service.create(
            payload,
        ),
        message="Household created.",
    )


@router.put(
    "/{household_id}",
    response_model=ApiResponse[
        HouseholdResponse
    ],
    summary="Update household",
)
def update_household(
    payload: HouseholdUpdate,
    household_id: str = Path(
        ...,
        description="Household ID",
    ),
    service: HouseholdService = Depends(
        get_household_service,
    ),
):
    return success_response(
        service.update(
            household_id,
            payload,
        ),
        message="Household updated.",
    )


@router.delete(
    "/{household_id}",
    response_model=ApiResponse[None],
    summary="Delete household",
)
def delete_household(
    household_id: str = Path(
        ...,
        description="Household ID",
    ),
    service: HouseholdService = Depends(
        get_household_service,
    ),
):
    service.delete(
        household_id,
    )

    return success_response(
        None,
        message="Household deleted.",
    )
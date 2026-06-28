from fastapi import APIRouter, Depends

from app.dependencies.pagination import get_pagination
from app.dependencies.territory import get_territory_service
from app.schemas.pagination import (
    PaginationParams,
    PaginationResult,
)
from app.schemas.response import (
    ApiResponse,
    success_response,
)
from app.schemas.territory import (
    DistrictResponse,
    ProvinceResponse,
    RegencyResponse,
    VillageResponse,
)
from app.services.territory_service import TerritoryService

router = APIRouter(
    prefix="/territories",
    tags=["Territories"],
)


@router.get(
    "/provinces",
    response_model=ApiResponse[PaginationResult[ProvinceResponse]],
    summary="List provinces",
)
def get_provinces(
    pagination: PaginationParams = Depends(
        get_pagination,
    ),
    service: TerritoryService = Depends(
        get_territory_service,
    ),
):
    return success_response(
        service.get_provinces(
            pagination.page,
            pagination.size,
        )
    )


@router.get(
    "/provinces/{province_id}/regencies",
    response_model=ApiResponse[list[RegencyResponse]],
    summary="List regencies by province",
)
def get_regencies(
    province_id: str,
    service: TerritoryService = Depends(
        get_territory_service,
    ),
):
    return success_response(
        service.get_regencies(
            province_id,
        )
    )


@router.get(
    "/regencies/{regency_id}/districts",
    response_model=ApiResponse[list[DistrictResponse]],
    summary="List districts by regency",
)
def get_districts(
    regency_id: str,
    service: TerritoryService = Depends(
        get_territory_service,
    ),
):
    return success_response(
        service.get_districts(
            regency_id,
        )
    )


@router.get(
    "/districts/{district_id}/villages",
    response_model=ApiResponse[list[VillageResponse]],
    summary="List villages by district",
)
def get_villages(
    district_id: str,
    service: TerritoryService = Depends(
        get_territory_service,
    ),
):
    return success_response(
        service.get_villages(
            district_id,
        )
    )

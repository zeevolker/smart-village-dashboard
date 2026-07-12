from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from uuid import UUID

from app.database.dependencies import get_db

from app.dependencies.analytics import get_analytics_service
from app.schemas.analytics import (
    AnalyticsSummary,
    AnalyticsDemographics,
    VillageSummary
)
from app.schemas.response import (
    ApiResponse,
    success_response,
)
from app.services.analytics_service import AnalyticsService

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get(
    "/summary",
    response_model=ApiResponse[AnalyticsSummary],
)
def get_summary(
    service: AnalyticsService = Depends(
        get_analytics_service,
    ),
):

    return success_response(
        data=service.get_summary(),
        message="Success",
    )
    
@router.get(
    "/demographics",
    response_model=ApiResponse[AnalyticsDemographics],
)
def get_demographics(
    service: AnalyticsService = Depends(
        get_analytics_service,
    ),
):

    return success_response(
        data=service.get_demographics(),
    )
    
@router.get(
    "/villages",
    response_model=ApiResponse[list[VillageSummary]],
)
def get_villages(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    search: str | None = Query(
        default=None,
        description="Search village name",
    ),
    district_id: UUID | None = Query(
        default=None,
        description="Filter by district id",
    ),
    sort: str = Query(
        default="village",
        description="Sort by: village, district, population, households",
    ),
    order: str = Query(
        default="asc",
        description="Sort order: asc or desc",
    ),
    service: AnalyticsService = Depends(
        get_analytics_service,
    ),
):
    
    return success_response(
        data=service.get_village_summary(
            page=page,
            page_size=page_size,
            search=search,
            district_id=district_id,
            sort=sort,
            order=order,
        )
    )
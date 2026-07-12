from fastapi import APIRouter, Depends

from app.dependencies.dashboard import get_dashboard_service
from app.schemas.dashboard import DashboardResponse
from app.schemas.response import (
    ApiResponse,
    success_response,
)
from app.services.dashboard_service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "",
    response_model=ApiResponse[DashboardResponse],
    summary="Dashboard summary",
)
def get_dashboard(
    service: DashboardService = Depends(
        get_dashboard_service,
    ),
):
    return success_response(
        data=service.get_dashboard(),
    )
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.repositories.analytics_repository import AnalyticsRepository
from app.services.dashboard_service import DashboardService


def get_dashboard_service(
    db: Session = Depends(get_db),
) -> DashboardService:
    """
    Dependency for DashboardService.
    """

    repository = AnalyticsRepository(db)

    return DashboardService(
        repository,
    )
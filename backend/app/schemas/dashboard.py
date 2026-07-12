from pydantic import BaseModel

from app.schemas.analytics import (
    AnalyticsSummary,
    AnalyticsDemographics,
    VillageSummary,
)


class DashboardResponse(BaseModel):
    summary: AnalyticsSummary
    demographics: AnalyticsDemographics
    villages: list[VillageSummary]
from app.repositories.analytics_repository import AnalyticsRepository
from app.services.dashboard_service import DashboardService


def test_get_dashboard(db):
    repository = AnalyticsRepository(db)
    service = DashboardService(repository)

    result = service.get_dashboard()

    assert result.summary.population > 0
    assert result.summary.households > 0
    assert result.summary.villages > 0

    assert result.summary.male >= 0
    assert result.summary.female >= 0

    assert len(result.demographics.religion) > 0
    assert len(result.demographics.occupation) > 0
    assert len(result.demographics.marital_status) > 0

    assert len(result.villages) > 0
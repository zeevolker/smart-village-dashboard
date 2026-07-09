from app.repositories.analytics_repository import AnalyticsRepository
from app.services.analytics_service import AnalyticsService


def test_get_summary(db):
    # Arrange
    repo = AnalyticsRepository(db)
    service = AnalyticsService(repo)

    # Act
    summary = service.get_summary()

    # Assert
    assert summary["population"] > 0
    assert summary["households"] > 0
    assert summary["villages"] > 0

    assert summary["male"] >= 0
    assert summary["female"] >= 0

    assert (
        summary["male"] + summary["female"]
        == summary["population"]
    )
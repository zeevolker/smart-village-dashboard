from app.repositories.analytics_repository import AnalyticsRepository
from app.services.analytics_service import AnalyticsService


def test_get_village_summary(db):
    # Arrange
    repo = AnalyticsRepository(db)
    service = AnalyticsService(repo)

    # Act
    data = service.get_village_summary()

    # Assert
    assert len(data) > 0

    first = data[0]

    assert "village_id" in first
    assert "district" in first
    assert "village" in first
    assert "households" in first
    assert "population" in first


def test_get_village_summary_search(db):
    # Arrange
    repo = AnalyticsRepository(db)
    service = AnalyticsService(repo)

    # Act
    data = service.get_village_summary(
        search="BABAKAN",
    )

    # Assert
    assert len(data) > 0

    for row in data:
        assert "babakan" in row["village"].lower()
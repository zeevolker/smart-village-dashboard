from app.repositories.analytics_repository import AnalyticsRepository


def test_religion_distribution(db):
    # Arrange
    repo = AnalyticsRepository(db)

    # Act
    result = repo.religion_distribution()

    # Assert
    assert len(result) > 0

    for item in result:
        assert "name" in item
        assert "count" in item
        assert item["count"] >= 0


def test_occupation_distribution(db):
    # Arrange
    repo = AnalyticsRepository(db)

    # Act
    result = repo.occupation_distribution()

    # Assert
    assert len(result) > 0

    for item in result:
        assert "name" in item
        assert "count" in item
        assert item["count"] >= 0


def test_marital_status_distribution(db):
    # Arrange
    repo = AnalyticsRepository(db)

    # Act
    result = repo.marital_status_distribution()

    # Assert
    assert len(result) > 0

    for item in result:
        assert "name" in item
        assert "count" in item
        assert item["count"] >= 0
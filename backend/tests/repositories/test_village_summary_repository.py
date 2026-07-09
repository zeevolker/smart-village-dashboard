from app.repositories.analytics_repository import AnalyticsRepository


def test_village_summary_default(db):
    # Arrange
    repo = AnalyticsRepository(db)

    # Act
    data = repo.village_summary()

    # Assert
    assert len(data) > 0

    first = data[0]

    assert "village_id" in first
    assert "district" in first
    assert "village" in first
    assert "households" in first
    assert "population" in first


def test_village_summary_sort_desc(db):
    # Arrange
    repo = AnalyticsRepository(db)

    # Act
    data = repo.village_summary(
        sort="village",
        order="desc",
    )

    # Assert
    assert len(data) > 1

    villages = [row["village"] for row in data]

    assert villages == sorted(villages, reverse=True)


def test_village_summary_search(db):
    # Arrange
    repo = AnalyticsRepository(db)

    # Act
    data = repo.village_summary(
        search="BABAKAN",
    )

    # Assert
    assert len(data) > 0

    for row in data:
        assert "babakan" in row["village"].lower()


def test_village_summary_filter_district(db):
    # Arrange
    repo = AnalyticsRepository(db)

    # Act
    data = repo.village_summary(
        district_id="9f3e37e8-0570-4685-b089-cff3be75eabc",
    )

    # Assert
    assert len(data) > 0

    for row in data:
        assert row["district"] == "BABAKAN MADANG"
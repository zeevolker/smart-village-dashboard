from app.services.household_service import HouseholdService


def test_search_without_keyword(db):
    service = HouseholdService(db)

    result = service.search(
        keyword="",
        page=1,
        size=20,
    )

    assert result.total > 0
    assert result.pages > 0
    assert len(result.items) > 0


def test_search_with_keyword(db):
    service = HouseholdService(db)

    result = service.search(
        keyword="3201",
        page=1,
        size=20,
    )

    assert result.total > 0
    assert result.pages > 0
    assert len(result.items) > 0

    assert all(
        "3201" in household.kk_number
        for household in result.items
    )
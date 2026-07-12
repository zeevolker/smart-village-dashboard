from app.repositories.household_repository import HouseholdRepository


def test_search_without_keyword(db):
    repo = HouseholdRepository(db)

    items, total, pages = repo.search(
        keyword="",
        page=1,
        size=20,
    )

    assert total > 0
    assert pages > 0
    assert len(items) > 0


def test_search_with_keyword(db):
    repo = HouseholdRepository(db)

    items, total, pages = repo.search(
        keyword="3201",
        page=1,
        size=20,
    )

    assert total > 0
    assert pages > 0
    assert len(items) > 0

    assert all(
        "3201" in household.kk_number
        for household in items
    )
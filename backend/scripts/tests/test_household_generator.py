from uuid import uuid4

from scripts.generators.household_generator import HouseholdGenerator


def main():

    print("=== Household Generator Test ===\n")

    household = HouseholdGenerator.generate(
        village_id=uuid4(),
        region_code="320122",
    )

    print(household)

    assert len(household.kk_number) == 16

    assert household.kk_number.startswith(
        "320122"
    )

    assert len(household.rt) == 3

    assert len(household.rw) == 3

    assert len(household.postal_code) == 5

    print("\n✅ All tests passed.")


if __name__ == "__main__":
    main()
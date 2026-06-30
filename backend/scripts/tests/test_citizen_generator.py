from uuid import uuid4

from scripts.generators.citizen_generator import CitizenGenerator
from scripts.generators.household_generator import HouseholdGenerator
from scripts.generators.profile_generator import ProfileGenerator
from app.enums.relationship import RelationshipType


def main():

    print("=== Citizen Generator Test ===\n")

    household = HouseholdGenerator.generate(
        village_id=uuid4(),
        region_code="320122",
    )

    profiles = ProfileGenerator.generate_family_profiles(
        [
            RelationshipType.HEAD,
            RelationshipType.SPOUSE,
            RelationshipType.CHILD,
        ]
    )

    for profile in profiles:

        citizen = CitizenGenerator.generate(
            household=household,
            profile=profile,
        )

        print(citizen)

    print("\n✅ All tests passed.")


if __name__ == "__main__":
    main()
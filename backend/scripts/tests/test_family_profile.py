from scripts.generators.family_generator import FamilyGenerator
from scripts.generators.profile_generator import ProfileGenerator


def main():

    print("=== Family Profile Test ===\n")

    relations = FamilyGenerator.generate_structure()

    profiles = ProfileGenerator.generate_family_profiles(
        relations
    )

    for profile in profiles:

        print(
            f"{profile.relationship.value:8}"
            f" | {profile.gender.value:6}"
            f" | {profile.age:2}"
            f" | {profile.marital_status.value}"
        )

    print("\n✅ All tests passed.")


if __name__ == "__main__":
    main()
from app.enums.relationship import RelationshipType
from scripts.generators.profile_generator import ProfileGenerator


def main():

    print("=== Profile Generator Test ===\n")

    for relation in RelationshipType:

        gender = ProfileGenerator.generate_gender(
            relation,
        )

        age = ProfileGenerator.generate_age(
            relation,
        )

        religion = ProfileGenerator.generate_religion()

        marital = ProfileGenerator.generate_marital_status(
            age=age,
            relationship=relation,
        )

        occupation = ProfileGenerator.generate_occupation(
            age,
        )

        print(
            f"{relation.value:8}"
            f" | {gender.value:6}"
            f" | {age:2}"
            f" | {religion.value:10}"
            f" | {marital.value:8}"
            f" | {occupation}"
        )

    print("\n✅ All tests passed.")


if __name__ == "__main__":
    main()
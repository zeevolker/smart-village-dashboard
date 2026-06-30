from app.enums.gender import Gender
from scripts.utils.name_generator import NameGenerator


def main():

    print("=== Name Generator Test ===\n")

    for _ in range(10):

        print(
            NameGenerator.generate(
                Gender.MALE,
            )
        )

    print("\n✅ All tests passed.")


if __name__ == "__main__":
    main()
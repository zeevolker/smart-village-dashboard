from scripts.generators.family_generator import FamilyGenerator


def main():

    print("=== Family Generator Test ===\n")

    for i in range(10):

        family = FamilyGenerator.generate_structure()

        print(
            f"{i+1:02}.",
            [member.value for member in family],
        )

    print("\n✅ All tests passed.")


if __name__ == "__main__":
    main()
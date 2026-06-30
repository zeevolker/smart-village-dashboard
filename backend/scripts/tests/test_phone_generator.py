from scripts.utils.phone_generator import PhoneGenerator


def main():

    print("=== Phone Generator Test ===\n")

    for i in range(10):

        phone = PhoneGenerator.generate()

        print(f"{i + 1:02}. {phone}")

        assert phone.startswith("08")
        assert phone.isdigit()
        assert 10 <= len(phone) <= 12

    print("\n✅ All tests passed.")


if __name__ == "__main__":
    main()
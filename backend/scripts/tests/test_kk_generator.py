from scripts.utils.kk_generator import KKGenerator


def main():

    print("=== KK Generator Test ===\n")

    generated = set()

    for i in range(10):

        kk = KKGenerator.generate(
            region_code="320122",
        )

        print(f"{i + 1:02}. {kk}")

        assert len(kk) == 16
        assert kk.isdigit()
        assert kk.startswith("320122")
        assert kk not in generated

        generated.add(kk)

    print("\n✅ All tests passed.")


if __name__ == "__main__":
    main()
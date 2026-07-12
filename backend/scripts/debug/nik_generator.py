from datetime import date

from app.enums.gender import Gender
from scripts.utils.nik_generator import NIKGenerator


def main():

    print("=== NIK Generator Test ===\n")

    male = NIKGenerator.generate(
        birth_date=date(
            2000,
            1,
            15,
        ),
        gender=Gender.MALE,
        region_code="320122",
    )

    female = NIKGenerator.generate(
        birth_date=date(
            2000,
            1,
            15,
        ),
        gender=Gender.FEMALE,
        region_code="320122",
    )

    print("Male   :", male)
    print("Female :", female)

    assert male[:6] == "320122"
    assert female[:6] == "320122"

    assert male[6:12] == "150100"

    assert female[6:12] == "550100"

    assert male != female

    print("\n✅ All tests passed.")


if __name__ == "__main__":
    main()
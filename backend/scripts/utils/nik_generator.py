from __future__ import annotations

import random
from datetime import date

from app.enums.gender import Gender


class NIKGenerator:
    """
    Generate synthetic Indonesian National Identity Number (NIK).

    Format:
        PPPPKKDDMMYYXXXX

    PPPPKK : 6-digit region code
    DDMMYY : Date of birth
             Female => day + 40
    XXXX   : Random unique sequence

    This generator is intended for development/testing only.
    """

    _generated: set[str] = set()

    @classmethod
    def generate(
        cls,
        *,
        birth_date: date,
        gender: Gender,
        region_code: str,
    ) -> str:
        """
        Generate a unique synthetic NIK.
        """

        if len(region_code) != 6:
            raise ValueError(
                "region_code must be exactly 6 digits."
            )

        day = birth_date.day

        if gender == Gender.FEMALE:
            day += 40

        birth = (
            f"{day:02}"
            f"{birth_date.month:02}"
            f"{birth_date.year % 100:02}"
        )

        while True:
            serial = random.randint(
                1,
                9999,
            )

            nik = (
                f"{region_code}"
                f"{birth}"
                f"{serial:04}"
            )

            if nik not in cls._generated:
                cls._generated.add(nik)
                return nik

    @classmethod
    def reset(cls) -> None:
        """
        Clear generated cache.
        """
        cls._generated.clear()
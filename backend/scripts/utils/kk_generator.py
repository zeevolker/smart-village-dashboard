from __future__ import annotations

import random


class KKGenerator:
    """
    Generate synthetic Indonesian Family Card (KK) numbers.

    Format:
        PPPPKKXXXXXXXXXX

    PPPPKK : 6-digit region code
    XXXXXX : 10-digit unique random number

    This generator is intended for development/testing only.
    """

    _generated: set[str] = set()

    @classmethod
    def generate(
        cls,
        *,
        region_code: str,
    ) -> str:
        """
        Generate a unique KK number.
        """

        if len(region_code) != 6:
            raise ValueError(
                "region_code must be exactly 6 digits."
            )

        while True:
            suffix = "".join(
                random.choices(
                    "0123456789",
                    k=10,
                )
            )

            kk = f"{region_code}{suffix}"

            if kk not in cls._generated:
                cls._generated.add(kk)
                return kk

    @classmethod
    def reset(cls) -> None:
        """
        Reset generated cache.
        """

        cls._generated.clear()
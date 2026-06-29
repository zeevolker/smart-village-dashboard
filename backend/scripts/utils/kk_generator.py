from __future__ import annotations

import random


class KKGenerator:
    """
    Generate unique Indonesian-style Family Card (KK) numbers.

    Format:
        16 digit numeric string

    Note:
        This is synthetic data intended for development and testing.
        It does not represent real government-issued KK numbers.
    """

    _generated: set[str] = set()

    @classmethod
    def generate(cls) -> str:
        while True:
            kk = "".join(random.choices("0123456789", k=16))

            if kk not in cls._generated:
                cls._generated.add(kk)
                return kk

    @classmethod
    def reset(cls) -> None:
        """
        Reset generated cache.
        Useful for unit testing.
        """
        cls._generated.clear()
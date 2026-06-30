from __future__ import annotations

import random


class PhoneGenerator:
    """
    Generate Indonesian mobile phone numbers.
    """

    PREFIXES = (
        "0811",
        "0812",
        "0813",
        "0821",
        "0822",
        "0823",
        "0851",
        "0852",
        "0853",
        "0855",
        "0856",
        "0857",
        "0858",
        "0877",
        "0878",
        "0881",
        "0882",
        "0883",
        "0887",
        "0888",
    )

    @classmethod
    def generate(cls) -> str:
        """
        Generate a valid Indonesian mobile phone number.
        """

        prefix = random.choice(cls.PREFIXES)

        remaining = "".join(
            random.choices(
                "0123456789",
                k=12 - len(prefix),
            )
        )

        return prefix + remaining
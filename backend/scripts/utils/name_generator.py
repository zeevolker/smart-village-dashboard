from __future__ import annotations

from faker import Faker

import re

from app.enums.gender import Gender


class NameGenerator:
    """
    Generate Indonesian names.
    """

    _faker = Faker("id_ID")

    @classmethod
    def generate(
        cls,
        gender: Gender,
    ) -> str:
        """
        Generate a clean Indonesian full name without titles.
        """

        name = cls._faker.name()

        # Remove prefix (anything ending with a dot at the beginning)
        name = re.sub(
            r"^(?:[A-Za-z]{1,5}\.\s*)+",
            "",
            name,
        )

        # Remove suffixes after comma
        name = re.sub(
            r",.*$",
            "",
            name,
        )

        return name.strip()
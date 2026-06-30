from __future__ import annotations

import random

from app.enums.gender import Gender
from app.enums.marital_status import MaritalStatus
from app.enums.relationship import RelationshipType
from app.enums.religion import Religion


class ProfileGenerator:
    """
    Generate demographic profiles for synthetic citizens.
    """

    OCCUPATIONS = (
        "Petani",
        "Pedagang",
        "Guru",
        "Karyawan Swasta",
        "Wiraswasta",
        "Nelayan",
        "Buruh",
        "PNS",
        "Mahasiswa",
        "Pelajar",
    )

    RELIGIONS = tuple(Religion)

    @classmethod
    def generate_gender(
        cls,
        relationship: RelationshipType,
    ) -> Gender:

        if relationship == RelationshipType.HEAD:
            return random.choices(
                [Gender.MALE, Gender.FEMALE],
                weights=[90, 10],
            )[0]

        if relationship == RelationshipType.SPOUSE:
            return Gender.FEMALE

        return random.choice(tuple(Gender))

    @classmethod
    def generate_age(
        cls,
        relationship: RelationshipType,
    ) -> int:

        ranges = {
            RelationshipType.HEAD: (30, 70),
            RelationshipType.SPOUSE: (25, 68),
            RelationshipType.CHILD: (0, 25),
            RelationshipType.PARENT: (55, 90),
            RelationshipType.SIBLING: (20, 75),
            RelationshipType.OTHER: (0, 90),
        }

        minimum, maximum = ranges[relationship]

        return random.randint(
            minimum,
            maximum,
        )

    @classmethod
    def generate_religion(
        cls,
    ) -> Religion:

        return random.choice(
            cls.RELIGIONS
        )

    @classmethod
    def generate_marital_status(
        cls,
        *,
        age: int,
        relationship: RelationshipType,
    ) -> MaritalStatus:

        if relationship == RelationshipType.CHILD:
            return MaritalStatus.SINGLE

        if age < 18:
            return MaritalStatus.SINGLE

        if relationship in (
            RelationshipType.HEAD,
            RelationshipType.SPOUSE,
        ):
            return MaritalStatus.MARRIED

        return random.choice(
            (
                MaritalStatus.SINGLE,
                MaritalStatus.MARRIED,
            )
        )

    @classmethod
    def generate_occupation(
        cls,
        age: int,
    ) -> str:

        if age < 6:
            return "Balita"

        if age < 18:
            return "Pelajar"

        if age <= 24:
            return random.choice(
                (
                    "Mahasiswa",
                    "Pelajar",
                )
            )

        return random.choice(
            cls.OCCUPATIONS
        )
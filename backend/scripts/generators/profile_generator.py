from __future__ import annotations

import random

from app.enums.gender import Gender
from app.enums.marital_status import MaritalStatus
from app.enums.relationship import RelationshipType
from app.enums.religion import Religion

from scripts.dto.family_profile import FamilyProfile

class ProfileGenerator:
    """
    Generate demographic profiles for synthetic citizens.
    """

    ADULT_OCCUPATIONS = (
        "Petani",
        "Pedagang",
        "Guru",
        "Karyawan Swasta",
        "Wiraswasta",
        "Nelayan",
        "Buruh",
        "PNS",
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
            if age < 21:
                return MaritalStatus.SINGLE

            return random.choices(
                [MaritalStatus.SINGLE, MaritalStatus.MARRIED],
                weights=[80, 20],
            )[0]

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
        
        if age >= 60:
            return random.choice(
                (
                    "Pensiunan",
                    "Petani",
                    "Pedagang",
                )
            )

        return random.choice(
            cls.ADULT_OCCUPATIONS
        )
        
    @classmethod
    def generate_family_profiles(
        cls,
        relationships: list[RelationshipType],
    ) -> list["FamilyProfile"]:

        profiles: list[FamilyProfile] = []

        head_gender = cls.generate_gender(
            RelationshipType.HEAD,
        )

        head_age = cls.generate_age(
            RelationshipType.HEAD,
        )
        
        family_religion = cls.generate_religion()
        
        child_count = relationships.count(
            RelationshipType.CHILD
        )

        child_ages = cls.generate_children_ages(
            count=child_count,
            head_age=head_age,
        )

        child_index = 0

        profiles.append(
            FamilyProfile(
                relationship=RelationshipType.HEAD,
                gender=head_gender,
                age=head_age,
                marital_status=MaritalStatus.MARRIED,
                religion=family_religion,
                occupation=cls.generate_occupation(head_age),
            )
        )

        for relation in relationships[1:]:

            if relation == RelationshipType.SPOUSE:

                gender = (
                    Gender.FEMALE
                    if head_gender == Gender.MALE
                    else Gender.MALE
                )

                age = max(
                    18,
                    head_age + random.randint(-5, 5),
                )

                marital = MaritalStatus.MARRIED

            elif relation == RelationshipType.CHILD:

                gender = random.choice(tuple(Gender))

                age = child_ages[child_index]
                child_index += 1

                marital = MaritalStatus.SINGLE

            elif relation == RelationshipType.PARENT:

                gender = random.choice(tuple(Gender))

                age = random.randint(
                    head_age + 18,
                    min(95, head_age + 40),
                )

                marital = random.choice(
                    (
                        MaritalStatus.MARRIED,
                        MaritalStatus.SINGLE,
                    )
                )

            elif relation == RelationshipType.SIBLING:

                gender = random.choice(tuple(Gender))

                age = max(
                    18,
                    head_age + random.randint(-8, 8),
                )

                marital = cls.generate_marital_status(
                    relationship=relation,
                    age=age,
                )

            else:

                gender = random.choice(tuple(Gender))

                age = cls.generate_age(
                    relation,
                )

                marital = cls.generate_marital_status(
                    relationship=relation,
                    age=age,
                )

            profiles.append(
                FamilyProfile(
                    relationship=relation,
                    gender=gender,
                    age=age,
                    marital_status=marital,
                    religion=family_religion,
                    occupation=cls.generate_occupation(age),
                )
            )

        return profiles
    
    @classmethod
    def generate_head_age(cls) -> int:
        """
        Generate age for head of household.
        """
        return random.randint(30, 70)
    
    @classmethod
    def generate_spouse_age(
        cls,
        *,
        head_age: int,
    ) -> int:
        """
        Generate spouse age close to head age.
        """
        return max(
            18,
            head_age + random.randint(-5, 5),
        )
        
    @classmethod
    def generate_children_ages(
        cls,
        *,
        count: int,
        head_age: int,
    ) -> list[int]:
        """
        Generate children ages sorted from oldest to youngest.
        """

        if count == 0:
            return []

        max_oldest = min(
            25,
            max(5, head_age - 20),
        )

        oldest = random.randint(
            5,
            max_oldest,
        )

        ages = [oldest]

        current = oldest

        for _ in range(count - 1):

            current = max(
                1,
                current - random.randint(2, 4),
            )

            ages.append(current)

        return ages
    
    @classmethod
    def generate_parent_age(
        cls,
        *,
        head_age: int,
    ) -> int:
        """
        Generate parent age.
        """
        return random.randint(
            head_age + 18,
            min(
                95,
                head_age + 40,
            ),
        )
        
    @classmethod
    def generate_sibling_age(
        cls,
        *,
        head_age: int,
    ) -> int:
        """
        Generate sibling age.
        """
        return max(
            18,
            head_age + random.randint(-8, 8),
        )
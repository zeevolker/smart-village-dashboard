from __future__ import annotations

import random
from datetime import date

from faker import Faker
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.enums.gender import Gender
from app.enums.marital_status import MaritalStatus
from app.enums.religion import Religion
from app.models.citizen import Citizen
from app.models.village import Village


class CitizenSeeder:
    """
    Seeder for Citizen data.
    """

    def __init__(
        self,
        db: Session,
    ) -> None:
        self.db = db

        self.fake = Faker("id_ID")

        self.villages = self.db.scalars(
            select(Village)
        ).all()

        if not self.villages:
            raise ValueError(
                "No villages found. Seed territories first."
            )

        self.used_niks: set[str] = set()

        with open(
            "data/development/names/male_names.txt",
            encoding="utf-8",
        ) as file:
            self.male_names = [
                line.strip()
                for line in file
                if line.strip()
            ]

        with open(
            "data/development/names/female_names.txt",
            encoding="utf-8",
        ) as file:
            self.female_names = [
                line.strip()
                for line in file
                if line.strip()
            ]

    def _random_village(self) -> Village:
        """
        Return random village.
        """

        return random.choice(
            self.villages,
        )

    def _random_birth_date(self) -> date:
        """
        Generate random birth date.
        """

        return self.fake.date_between(
            start_date="-55y",
            end_date="-15y",
        )

    def _random_gender(self) -> Gender:
        """
        Generate random gender.
        """

        return random.choice(
            [
                Gender.MALE,
                Gender.FEMALE,
            ]
        )

    def _random_name(
        self,
        gender: Gender,
    ) -> str:
        """
        Generate Indonesian name based on gender.
        """

        if gender == Gender.MALE:
            return random.choice(
                self.male_names,
            )

        return random.choice(
            self.female_names,
        )

    def _random_birth_place(self) -> str:
        """
        Generate birth place.
        """

        return self.fake.city()

    def _random_religion(
        self,
    ) -> Religion:
        """
        Generate religion using Indonesian population distribution.
        """

        return random.choices(
            population=[
                Religion.ISLAM,
                Religion.CHRISTIAN,
                Religion.CATHOLIC,
                Religion.HINDU,
                Religion.BUDDHIST,
                Religion.CONFUCIAN,
            ],
            weights=[
                87,
                8,
                3,
                1,
                0.8,
                0.2,
            ],
            k=1,
        )[0]

    def _random_marital_status(
        self,
        birth_date: date,
    ) -> MaritalStatus:
        """
        Generate marital status based on age.
        """

        today = date.today()

        age = (
            today.year
            - birth_date.year
            - (
                (today.month, today.day)
                < (
                    birth_date.month,
                    birth_date.day,
                )
            )
        )

        if age < 21:

            return MaritalStatus.SINGLE

        if age < 30:

            return random.choices(
                population=[
                    MaritalStatus.SINGLE,
                    MaritalStatus.MARRIED,
                ],
                weights=[
                    70,
                    30,
                ],
                k=1,
            )[0]

        if age < 55:

            return random.choices(
                population=[
                    MaritalStatus.MARRIED,
                    MaritalStatus.SINGLE,
                    MaritalStatus.DIVORCED,
                ],
                weights=[
                    75,
                    10,
                    15,
                ],
                k=1,
            )[0]

        return random.choices(
            population=[
                MaritalStatus.MARRIED,
                MaritalStatus.WIDOWED,
                MaritalStatus.DIVORCED,
            ],
            weights=[
                55,
                35,
                10,
            ],
            k=1,
        )[0]

    def _random_occupation(self) -> str:
        """
        Generate occupation.
        """

        jobs = [
            "Petani",
            "Guru",
            "Wiraswasta",
            "Buruh",
            "Pegawai Negeri",
            "Karyawan Swasta",
            "Mahasiswa",
            "Pelajar",
            "Pedagang",
            "Nelayan",
        ]

        return random.choice(
            jobs,
        )

    def _random_phone_number(self) -> str:
        """
        Generate phone number.
        """

        return (
            "08"
            + "".join(
                random.choices(
                    "0123456789",
                    k=10,
                )
            )
        )

    def _random_address(
        self,
    ) -> str:
        """
        Generate address.
        """

        return self.fake.street_address()

    def _build_nik(
        self,
        region_code: str,
        birth_date: date,
        gender: Gender,
        serial: int,
    ) -> str:
        """
        Build Indonesian-style NIK.
        """

        day = birth_date.day

        if gender == Gender.FEMALE:
            day += 40

        birth = (
            f"{day:02d}"
            f"{birth_date.month:02d}"
            f"{birth_date.year % 100:02d}"
        )

        return (
            f"{region_code}"
            f"{birth}"
            f"{serial:04d}"
        )

    def _generate_nik(
        self,
        village: Village,
        birth_date: date,
        gender: Gender,
    ) -> str:
        """
        Generate unique NIK.
        """

        region_code = (
            village.code.replace(
                ".",
                "",
            )
        )[:6]

        while True:

            serial = random.randint(
                1,
                9999,
            )

            nik = self._build_nik(
                region_code=region_code,
                birth_date=birth_date,
                gender=gender,
                serial=serial,
            )

            if nik not in self.used_niks:

                self.used_niks.add(
                    nik,
                )

                return nik

    def run(
        self,
        total: int = 500,
    ) -> None:
        """
        Run seeder.
        """

        citizens: list[Citizen] = []

        for _ in range(total):

            village = self._random_village()

            gender = self._random_gender()

            birth_date = self._random_birth_date()

            nik = self._generate_nik(
                village=village,
                birth_date=birth_date,
                gender=gender,
            )

            citizen = Citizen(
                nik=nik,
                full_name=self._random_name(
                    gender,
                ),
                gender=gender,
                birth_place=self._random_birth_place(),
                birth_date=birth_date,
                religion=self._random_religion(),
                marital_status=self._random_marital_status(
                    birth_date,
                ),
                occupation=self._random_occupation(),
                phone_number=self._random_phone_number(),
                address=self._random_address(),
                village_id=village.id,
            )

            citizens.append(
                citizen,
            )

        try:

            self.db.add_all(
                citizens,
            )

            self.db.commit()

            print(
                f"Successfully inserted {len(citizens)} citizens."
            )

        except Exception:

            self.db.rollback()

            raise
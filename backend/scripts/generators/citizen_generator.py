from __future__ import annotations

from datetime import date

from scripts.dto.citizen_data import CitizenData
from scripts.dto.family_profile import FamilyProfile
from scripts.dto.household_data import HouseholdData

from scripts.utils.name_generator import NameGenerator
from scripts.utils.nik_generator import NIKGenerator
from scripts.utils.phone_generator import PhoneGenerator


class CitizenGenerator:
    """
    Generate a complete CitizenData object from
    HouseholdData and FamilyProfile.
    """

    @classmethod
    def generate(
        cls,
        *,
        household: HouseholdData,
        profile: FamilyProfile,
    ) -> CitizenData:

        today = date.today()

        birth_date = date(
            today.year - profile.age,
            1,
            1,
        )

        nik = NIKGenerator.generate(
            region_code=household.region_code,
            birth_date=birth_date,
            gender=profile.gender,
        )

        return CitizenData(
            nik=nik,
            full_name=NameGenerator.generate(profile.gender),
            gender=profile.gender,
            birth_place="Purbalingga",
            birth_date=birth_date,
            religion=profile.religion,
            marital_status=profile.marital_status,
            occupation=profile.occupation,
            phone_number=PhoneGenerator.generate(),
            address=household.address,
            village_id=household.village_id,
            household_id=None,
            relationship_to_head=profile.relationship,
        )
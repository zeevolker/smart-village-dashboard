from __future__ import annotations

import random

from sqlalchemy.orm import Session

from app.models.citizen import Citizen

from scripts.generators.family_generator import FamilyGenerator
from scripts.generators.profile_generator import ProfileGenerator
from scripts.generators.citizen_generator import CitizenGenerator

from app.models.household import Household
from app.repositories.village_repository import VillageRepository

from scripts.generators.household_generator import HouseholdGenerator


class PopulationSeeder:
    """
    Seed synthetic population into database.
    """

    def __init__(
        self,
        db: Session,
    ) -> None:

        self.db = db
        self.village_repository = VillageRepository(db)

    def seed(
        self,
        *,
        households: int,
    ) -> None:

        try:

            villages = self.village_repository.get_all()

            if not villages:
                raise ValueError(
                    "No villages found in database."
                )
                
            total_citizens = 0

            for index in range(households):

                village = random.choice(villages)

                household_data = HouseholdGenerator.generate(
                    village_id=village.id,
                    region_code=village.bps_code[:6],
                )

                household = Household(
                    kk_number=household_data.kk_number,
                    address=household_data.address,
                    rt=household_data.rt,
                    rw=household_data.rw,
                    postal_code=household_data.postal_code,
                    village_id=household_data.village_id,
                )

                self.db.add(household)

                self.db.flush()
                
                relationships = FamilyGenerator.generate_structure()

                profiles = ProfileGenerator.generate_family_profiles(
                    relationships
                )
                
                total_citizens += len(profiles)
                
                for profile in profiles:

                    citizen_data = CitizenGenerator.generate(
                        household=household_data,
                        profile=profile,
                    )
                    
                    citizen = Citizen(
                        nik=citizen_data.nik,
                        full_name=citizen_data.full_name,
                        gender=citizen_data.gender,
                        birth_place=citizen_data.birth_place,
                        birth_date=citizen_data.birth_date,
                        religion=citizen_data.religion,
                        marital_status=citizen_data.marital_status,
                        occupation=citizen_data.occupation,
                        phone_number=citizen_data.phone_number,
                        address=citizen_data.address,
                        village_id=citizen_data.village_id,
                        household_id=household.id,
                        relationship_to_head=citizen_data.relationship_to_head,
                    )

                    self.db.add(citizen)

                print(
                    f"[{index+1}/{households}] "
                    f"{household.kk_number}"
                    f" ({len(profiles)} citizens)"
                )

            self.db.commit()
            
            print()

            print("=" * 40)

            print(f"Households : {households}")

            print(f"Citizens   : {total_citizens}")

            print("=" * 40)

            print(
                f"\n✓ Successfully created {households} households."
            )

        except Exception:

            self.db.rollback()

            raise
from __future__ import annotations

import random
from uuid import UUID

from scripts.dto.household_data import HouseholdData
from scripts.utils.kk_generator import KKGenerator


class HouseholdGenerator:
    """
    Generate synthetic household data.

    This generator is independent from the database.
    It only returns HouseholdData objects.
    """

    STREET_NAMES = (
        "Jl. Merdeka",
        "Jl. Melati",
        "Jl. Mawar",
        "Jl. Kenanga",
        "Jl. Anggrek",
        "Jl. Cendana",
        "Jl. Diponegoro",
        "Jl. Sudirman",
        "Jl. Gatot Subroto",
        "Jl. Ahmad Yani",
    )

    @classmethod
    def generate(
        cls,
        *,
        village_id: UUID,
        region_code: str,
    ) -> HouseholdData:

        address = (
            f"{random.choice(cls.STREET_NAMES)} "
            f"No. {random.randint(1, 250)}"
        )

        rt = f"{random.randint(1, 15):03}"

        rw = f"{random.randint(1, 10):03}"

        postal_code = str(
            random.randint(
                10000,
                99999,
            )
        )

        kk_number = KKGenerator.generate(
            region_code=region_code,
        )

        return HouseholdData(
            kk_number=kk_number,
            address=address,
            rt=rt,
            rw=rw,
            postal_code=postal_code,
            village_id=village_id,
            region_code=region_code,
        )
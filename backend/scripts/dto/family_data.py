from __future__ import annotations

from dataclasses import dataclass, field

from scripts.dto.citizen_data import CitizenData
from scripts.dto.household_data import HouseholdData


@dataclass(slots=True)
class FamilyData:
    """
    DTO representing one household and all of its members.
    """

    household: HouseholdData

    citizens: list[CitizenData] = field(
        default_factory=list,
    )
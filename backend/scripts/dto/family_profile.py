from __future__ import annotations

from dataclasses import dataclass

from app.enums.gender import Gender
from app.enums.marital_status import MaritalStatus
from app.enums.relationship import RelationshipType


@dataclass(slots=True)
class FamilyProfile:
    """
    Demographic profile for one family member.

    This object is generated before CitizenData.
    """

    relationship: RelationshipType

    gender: Gender

    age: int

    marital_status: MaritalStatus
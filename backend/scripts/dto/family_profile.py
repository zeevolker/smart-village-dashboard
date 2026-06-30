from __future__ import annotations

from dataclasses import dataclass

from app.enums.gender import Gender
from app.enums.marital_status import MaritalStatus
from app.enums.relationship import RelationshipType
from app.enums.religion import Religion


@dataclass(slots=True)
class FamilyProfile:
    """
    Demographic profile for one family member.
    """

    relationship: RelationshipType

    gender: Gender

    age: int

    marital_status: MaritalStatus

    religion: Religion

    occupation: str
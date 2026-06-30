from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from uuid import UUID

from app.enums.gender import Gender
from app.enums.marital_status import MaritalStatus
from app.enums.relationship import RelationshipType
from app.enums.religion import Religion


@dataclass(slots=True)
class CitizenData:
    """
    DTO for a generated citizen.
    """

    nik: str
    full_name: str

    gender: Gender

    birth_place: str
    birth_date: date

    religion: Religion
    marital_status: MaritalStatus

    occupation: str

    phone_number: str | None

    address: str

    village_id: UUID

    household_id: UUID | None

    relationship_to_head: RelationshipType
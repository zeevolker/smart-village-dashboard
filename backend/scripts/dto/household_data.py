from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class HouseholdData:
    """
    Data Transfer Object (DTO) for a generated household.

    This object is produced by HouseholdGenerator and later
    consumed by the Population Seeder.
    """

    kk_number: str
    address: str
    rt: str
    rw: str
    postal_code: str
    village_id: UUID
    region_code: str
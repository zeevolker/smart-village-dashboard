from uuid import UUID

from pydantic import BaseModel

from app.enums.gender import Gender
from app.enums.marital_status import MaritalStatus
from app.enums.religion import Religion


class CitizenFilter(BaseModel):
    keyword: str | None = None
    gender: Gender | None = None
    religion: Religion | None = None
    marital_status: MaritalStatus | None = None
    village_id: UUID | None = None
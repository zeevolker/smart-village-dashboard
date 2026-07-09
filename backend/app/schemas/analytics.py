from pydantic import BaseModel
from uuid import UUID


class AnalyticsSummary(BaseModel):
    population: int
    households: int
    villages: int
    male: int
    female: int

class CountItem(BaseModel):
    name: str
    count: int


class GenderSummary(BaseModel):
    male: int
    female: int


class AnalyticsDemographics(BaseModel):
    gender: GenderSummary
    religion: list[CountItem]
    occupation: list[CountItem]
    marital_status: list[CountItem]
    
class VillageSummary(BaseModel):
    village_id: UUID
    village: str
    households: int
    population: int
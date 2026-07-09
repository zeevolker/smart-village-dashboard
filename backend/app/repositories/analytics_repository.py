from sqlalchemy import func, select, distinct
from sqlalchemy.orm import Session

from uuid import UUID

from app.models.citizen import Citizen
from app.models.household import Household
from app.models.village import Village
from app.models.district import District

from app.enums.gender import Gender

class AnalyticsRepository:

    def __init__(self, db: Session):
        self.db = db

    def count_population(self) -> int:
        return (
            self.db.scalar(
                select(func.count(Citizen.id))
            )
            or 0
        )

    def count_households(self) -> int:
        return (
            self.db.scalar(
                select(func.count(Household.id))
            )
            or 0
        )

    def count_villages(self) -> int:
        return (
            self.db.scalar(
                select(func.count(Village.id))
            )
            or 0
        )

    def count_gender(self) -> dict[str, int]:

        male = (
            self.db.scalar(
                select(func.count(Citizen.id))
                .where(
                    Citizen.gender == Gender.MALE
                )
            )
            or 0
        )

        female = (
            self.db.scalar(
                select(func.count(Citizen.id))
                .where(
                    Citizen.gender == Gender.FEMALE
                )
            )
            or 0
        )

        return {
            "male": male,
            "female": female,
        }
        
    def religion_distribution(self) -> list[dict]:

        rows = self.db.execute(
            select(
                Citizen.religion,
                func.count(Citizen.id),
            )
            .group_by(Citizen.religion)
            .order_by(
                func.count(Citizen.id).desc()
            )
        )

        return [
            {
                "name": religion.value,
                "count": count,
            }
            for religion, count in rows
        ]
        
    def occupation_distribution(self) -> list[dict]:

        rows = self.db.execute(
            select(
                Citizen.occupation,
                func.count(Citizen.id),
            )
            .group_by(Citizen.occupation)
            .order_by(
                func.count(Citizen.id).desc()
            )
        )

        return [
            {
                "name": occupation,
                "count": count,
            }
            for occupation, count in rows
        ]
        
    def marital_status_distribution(self) -> list[dict]:

        rows = self.db.execute(
            select(
                Citizen.marital_status,
                func.count(Citizen.id),
            )
            .group_by(Citizen.marital_status)
            .order_by(
                func.count(Citizen.id).desc()
            )
        )

        return [
            {
                "name": status.value,
                "count": count,
            }
            for status, count in rows
        ]
        
    def village_summary(
        self,
        *,
        page: int = 1,
        page_size: int = 20,
        search: str | None = None,
        district_id: UUID | None = None,
        sort: str = "village",
        order: str = "asc",
    ) -> list[dict]:

        offset = (page - 1) * page_size

        # Base query
        query = (
            select(
                Village.id,
                Village.name,
                District.name,
                func.count(
                    distinct(Household.id)
                ).label("households"),
                func.count(
                    distinct(Citizen.id)
                ).label("population"),
            )
            .outerjoin(
                District,
                Village.district_id == District.id,
            )
            .outerjoin(
                Household,
                Household.village_id == Village.id,
            )
            .outerjoin(
                Citizen,
                Citizen.village_id == Village.id,
            )
        )

        # Search filter
        if search:
            query = query.where(
                Village.name.ilike(f"%{search}%")
            )

        # District filter
        if district_id:
            query = query.where(
                Village.district_id == district_id
            )
            
        sort_columns = {
            "village": Village.name,
            "district": District.name,
            "population": func.count(
                distinct(Citizen.id)
            ),
            "households": func.count(
                distinct(Household.id)
            ),
        }

        sort_column = sort_columns.get(
            sort,
            Village.name,
        )

        # Grouping, sorting, pagination
        query = (
            query
            .group_by(
                Village.id,
                Village.name,
                District.name,
            )
            .order_by(
                sort_column.desc()
                if order.lower() == "desc"
                else sort_column.asc()
            )
            .offset(offset)
            .limit(page_size)
        )

        rows = self.db.execute(query)

        return [
            {
                "village_id": village_id,
                "district": district_name,
                "village": village_name,
                "households": households,
                "population": population,
            }
            for (
                village_id,
                village_name,
                district_name,
                households,
                population,
            ) in rows
        ]
        
    def district_summary(self) -> list[dict]:

        rows = self.db.execute(
            select(
                District.id,
                District.name,
                func.count(
                    distinct(Village.id)
                ).label("villages"),
                func.count(
                    distinct(Household.id)
                ).label("households"),
                func.count(
                    distinct(Citizen.id)
                ).label("population"),
            )
            .outerjoin(
                Village,
                Village.district_id == District.id,
            )
            .outerjoin(
                Household,
                Household.village_id == Village.id,
            )
            .outerjoin(
                Citizen,
                Citizen.village_id == Village.id,
            )
            .group_by(
                District.id,
                District.name,
            )
            .order_by(
                District.name,
            )
        )

        return [
            {
                "district_id": district_id,
                "district": district_name,
                "villages": villages,
                "households": households,
                "population": population,
            }
            for (
                district_id,
                district_name,
                villages,
                households,
                population,
            ) in rows
        ]
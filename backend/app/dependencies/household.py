from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.services.household_service import HouseholdService


def get_household_service(
    db: Session = Depends(
        get_db,
    ),
) -> HouseholdService:
    """
    Dependency for HouseholdService.
    """

    return HouseholdService(
        db,
    )
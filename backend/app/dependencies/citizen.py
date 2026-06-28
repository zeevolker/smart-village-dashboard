from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.services.citizen_service import CitizenService


def get_citizen_service(
    db: Session = Depends(get_db),
) -> CitizenService:
    """
    Dependency untuk CitizenService.
    """

    return CitizenService(db)

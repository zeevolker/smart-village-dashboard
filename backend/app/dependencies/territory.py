from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.services.territory_service import TerritoryService


def get_territory_service(
    db: Session = Depends(get_db),
) -> TerritoryService:

    return TerritoryService(db)
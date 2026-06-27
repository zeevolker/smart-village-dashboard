from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.province import (
    ProvinceCreate,
    ProvinceResponse,
)
from app.services.province_service import ProvinceService

router = APIRouter(
    prefix="/provinces",
    tags=["Provinces"],
)


@router.post(
    "",
    response_model=ProvinceResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_province(
    province: ProvinceCreate,
    db: Session = Depends(get_db),
):
    service = ProvinceService(db)

    try:
        return service.create_province(province)

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc


@router.get(
    "",
    response_model=list[ProvinceResponse],
)
def get_provinces(
    db: Session = Depends(get_db),
):
    service = ProvinceService(db)
    return service.get_provinces()


@router.get(
    "/{province_id}",
    response_model=ProvinceResponse,
)
def get_province(
    province_id: UUID,
    db: Session = Depends(get_db),
):
    service = ProvinceService(db)

    province = service.get_province(province_id)

    if province is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Province not found.",
        )

    return province
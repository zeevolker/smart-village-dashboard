from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.auth.permissions import require_roles
from app.database.dependencies import get_db
from app.enums.user_role import UserRole
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    _: User = Depends(
        require_roles(
            UserRole.SUPER_ADMIN,
        ),
    ),
):
    service = UserService(db)

    return service.create_user(user)

@router.get(
    "/me",
    response_model=UserResponse,
)
def get_me(
    current_user: User = Depends(get_current_user),
):
    return current_user


@router.get("/admin-only")
def admin_only(
    current_user=Depends(require_roles(UserRole.SUPER_ADMIN)),
):
    return {"message": "Welcome Super Admin!"}

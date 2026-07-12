from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.models.user import User
from app.schemas.user import UserResponse

from app.database.dependencies import get_db
from app.schemas.auth import TokenResponse
from app.services.user_service import UserService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    service = UserService(db)

    token = service.login(
        email=form_data.username,
        password=form_data.password,
    )

    return TokenResponse(
        access_token=token,
    )
    
@router.get(
    "/me",
    response_model=UserResponse,
)
def get_me(
    current_user: User = Depends(
        get_current_user,
    ),
):
    """
    Mengembalikan informasi user yang sedang login.
    """

    return current_user

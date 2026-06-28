from fastapi import Depends, HTTPException, status

from app.auth.dependencies import get_current_user
from app.enums.user_role import UserRole


def require_roles(*roles: UserRole):
    """
    Dependency untuk membatasi akses berdasarkan role.
    """

    def checker(current_user=Depends(get_current_user)):
        if current_user.role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied.",
            )

        return current_user

    return checker

from fastapi import APIRouter

from app.api.v1.health import router as health_router
from app.api.v1.users import router as user_router

from app.api.v1.auth import router as auth_router

from app.api.v1.provinces import router as province_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health_router)
api_router.include_router(user_router)
api_router.include_router(auth_router)
api_router.include_router(province_router)
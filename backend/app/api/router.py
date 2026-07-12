from fastapi import APIRouter

from app.api.v1.auth import router as auth_router
from app.api.v1.citizens import router as citizen_router
from app.api.v1.health import router as health_router
from app.api.v1.households import (
    router as household_router,
)
from app.api.v1.territories import (
    router as territory_router,
)
from app.api.v1.users import router as user_router
from app.api.v1 import analytics

from app.api.v1.dashboard import router as dashboard_router

api_router = APIRouter(
    prefix="/api/v1",
)

api_router.include_router(
    health_router,
)

api_router.include_router(
    auth_router,
)

api_router.include_router(
    user_router,
)

api_router.include_router(
    territory_router,
)

api_router.include_router(
    citizen_router,
)

api_router.include_router(
    household_router,
)

api_router.include_router(analytics.router)

api_router.include_router(
    dashboard_router,
)
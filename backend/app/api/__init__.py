from fastapi import APIRouter

from app.api.user import router as user_route
from app.api.passwords import router as pwd_route

router = APIRouter()

router.include_router(user_route, prefix="", tags=["user"])
router.include_router(pwd_route, prefix="/passwords", tags=["passwords"])

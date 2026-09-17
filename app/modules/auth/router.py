from fastapi import APIRouter

from app.core.exceptions import not_implemented

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/")
async def index():
    raise not_implemented("auth")

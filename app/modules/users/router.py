from fastapi import APIRouter

from app.core.exceptions import not_implemented

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def index():
    raise not_implemented("users")

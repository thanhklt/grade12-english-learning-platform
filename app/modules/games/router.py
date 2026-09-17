from fastapi import APIRouter

from app.core.exceptions import not_implemented

router = APIRouter(prefix="/games", tags=["games"])


@router.get("/")
async def index():
    raise not_implemented("games")

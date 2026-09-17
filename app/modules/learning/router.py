from fastapi import APIRouter

from app.core.exceptions import not_implemented

router = APIRouter(prefix="/learning", tags=["learning"])


@router.get("/")
async def index():
    raise not_implemented("learning")

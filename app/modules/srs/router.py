from fastapi import APIRouter

from app.core.exceptions import not_implemented

router = APIRouter(prefix="/srs", tags=["srs"])


@router.get("/")
async def index():
    raise not_implemented("srs")

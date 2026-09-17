from fastapi import APIRouter, Depends

from app.core.exceptions import not_implemented
from app.core.security import require_admin

router = APIRouter(prefix="/admin", tags=["admin"], dependencies=[Depends(require_admin)])


@router.get("/")
async def index():
    raise not_implemented("admin")

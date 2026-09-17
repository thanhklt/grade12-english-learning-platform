from typing import NoReturn

from fastapi import HTTPException, status


async def require_admin() -> NoReturn:
    # Fail closed until DB-backed sessions and role verification are implemented.
    # Never trust a role supplied by a header, query parameter, or browser.
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Authentication is not implemented yet",
    )

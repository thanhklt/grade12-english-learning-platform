import asyncio
from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.config import Settings, get_settings
from app.core.database import get_db
from app.core.templates import APP_DIR, templates
from app.modules import admin, auth, flashcards, games, learning, srs, users


def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings or get_settings()

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        engine = create_async_engine(
            settings.database_url.get_secret_value(),
            pool_size=settings.db_pool_size,
            max_overflow=settings.db_max_overflow,
            pool_pre_ping=True,
            connect_args={"timeout": 3},
        )
        app.state.session_factory = async_sessionmaker(engine, expire_on_commit=False)
        try:
            yield
        finally:
            await engine.dispose()

    application = FastAPI(
        title="Grade 12 English Learning Platform",
        version="0.1.0",
        lifespan=lifespan,
        docs_url="/docs" if settings.app_env in {"local", "test"} else None,
        redoc_url=None,
        openapi_url="/openapi.json" if settings.app_env in {"local", "test"} else None,
    )
    application.mount("/static", StaticFiles(directory=str(APP_DIR / "static")), name="static")
    for module in (auth, users, learning, flashcards, srs, games, admin):
        application.include_router(module.router)

    @application.get("/health", tags=["operations"])
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    @application.get("/ready", tags=["operations"])
    async def ready(db: Annotated[AsyncSession, Depends(get_db)]) -> JSONResponse:
        try:
            async with asyncio.timeout(3):
                await db.execute(text("SELECT 1"))
            return JSONResponse({"status": "ready"})
        except (SQLAlchemyError, OSError, TimeoutError):
            return JSONResponse({"status": "not_ready"}, status_code=503)

    @application.get("/", response_class=HTMLResponse, include_in_schema=False)
    async def home(request: Request):
        return templates.TemplateResponse(request=request, name="user/index.html")

    @application.get("/welcome", response_class=HTMLResponse, include_in_schema=False)
    async def welcome(request: Request):
        return templates.TemplateResponse(request=request, name="user/partials/welcome.html")

    return application


app = create_app()

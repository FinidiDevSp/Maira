"""Fixtures compartidas. La configuración de test no depende de ningún .env real."""

import os
from collections.abc import AsyncIterator

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

ENV_TEST = {
    "ENVIRONMENT": "development",
    "SECRET_KEY": "clave-solo-para-tests-nada-real-0123456789",
    "CORS_ORIGINS": "http://localhost:3000",
    "DATABASE_URL": "sqlite+aiosqlite:///:memory:",
    "SUPABASE_URL": "https://test-proyecto.supabase.co",
    "SUPABASE_JWT_SECRET": "secreto-jwt-solo-tests-0123456789abcdef",
    "SUPABASE_SERVICE_KEY": "service-key-solo-tests",
}


@pytest.fixture(autouse=True)
def entorno_test(monkeypatch: pytest.MonkeyPatch) -> None:
    for clave, valor in ENV_TEST.items():
        monkeypatch.setenv(clave, valor)
    from src.config import get_settings

    get_settings.cache_clear()


@pytest.fixture
async def cliente() -> AsyncIterator[AsyncClient]:
    from src.main import create_app

    app = create_app()
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c


@pytest.fixture
async def sesion_db() -> AsyncIterator[AsyncSession]:
    """Sesión contra SQLite en memoria con el esquema creado desde los modelos."""
    from src.models.base import Base

    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    factory = async_sessionmaker(engine, expire_on_commit=False)
    async with factory() as sesion:
        yield sesion
    await engine.dispose()


def limpiar_env() -> None:
    for clave in ENV_TEST:
        os.environ.pop(clave, None)

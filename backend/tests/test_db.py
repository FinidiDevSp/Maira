"""FEATURE-000 · Tarea TDD 3: la sesión async de BD se construye desde settings."""

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.fixture(autouse=True)
def limpiar_caches_db() -> None:
    from src.db import session

    session.get_engine.cache_clear()
    session.get_session_factory.cache_clear()


async def test_get_db_entrega_sesion_usable() -> None:
    from src.db.session import get_db

    generador = get_db()
    sesion = await anext(generador)
    assert isinstance(sesion, AsyncSession)
    resultado = await sesion.scalar(text("SELECT 1"))
    assert resultado == 1
    with pytest.raises(StopAsyncIteration):
        await anext(generador)

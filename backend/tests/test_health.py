"""FEATURE-000 · Tarea TDD 1: GET /health devuelve 200 con el JSON esperado."""

from httpx import AsyncClient


async def test_health_devuelve_200_y_status_ok(cliente: AsyncClient) -> None:
    respuesta = await cliente.get("/health")
    assert respuesta.status_code == 200
    assert respuesta.json() == {"status": "ok"}


async def test_health_incluye_headers_de_seguridad(cliente: AsyncClient) -> None:
    respuesta = await cliente.get("/health")
    assert respuesta.headers["x-content-type-options"] == "nosniff"
    assert respuesta.headers["x-frame-options"] == "DENY"
    assert "referrer-policy" in respuesta.headers

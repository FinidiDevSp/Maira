"""FEATURE-001 · Tanda 2: alta de protectora (signup atómico con compensación)."""

import uuid
from collections.abc import AsyncIterator

import pytest
import respx
from httpx import ASGITransport, AsyncClient, Response
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

SUPABASE_URL = "https://test-proyecto.supabase.co"
CUENTA_ID = str(uuid.uuid4())

DATOS_VALIDOS = {
    "email": "lucia@refugio.example",
    "nombre_protectora": "Refugio Esperanza",
    "telefono": "+34 600 000 000",
    "persona_responsable": "Lucía Ejemplo",
    "acepta_terminos": True,
}


@pytest.fixture
async def cliente_signup(sesion_db: AsyncSession) -> AsyncIterator[AsyncClient]:
    from src.db.session import get_db
    from src.main import create_app

    app = create_app()

    async def _db() -> AsyncIterator[AsyncSession]:
        yield sesion_db

    app.dependency_overrides[get_db] = _db
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as cliente:
        yield cliente


@pytest.fixture(autouse=True)
def limpiar_rate_limit() -> None:
    from src.core import ratelimit

    ratelimit.reiniciar()


def mock_invite_ok(router: respx.MockRouter) -> None:
    router.post(f"{SUPABASE_URL}/auth/v1/invite").respond(200, json={"id": CUENTA_ID})


@respx.mock
async def test_signup_crea_protectora_y_admin(
    cliente_signup: AsyncClient, sesion_db: AsyncSession, respx_mock: respx.MockRouter
) -> None:
    from src.models import Protectora, RolUsuario, Usuario

    mock_invite_ok(respx_mock)
    respuesta = await cliente_signup.post("/api/v1/auth/signup", json=DATOS_VALIDOS)
    assert respuesta.status_code == 201, respuesta.text

    protectora = await sesion_db.scalar(select(Protectora))
    usuaria = await sesion_db.scalar(select(Usuario))
    assert protectora is not None and protectora.nombre == "Refugio Esperanza"
    assert usuaria is not None
    assert usuaria.id == uuid.UUID(CUENTA_ID)  # mismo id que la cuenta de Supabase
    assert usuaria.rol is RolUsuario.ADMIN
    assert usuaria.protectora_id == protectora.id


async def test_signup_sin_aceptar_terminos_rechazado(cliente_signup: AsyncClient) -> None:
    datos = DATOS_VALIDOS | {"acepta_terminos": False}
    respuesta = await cliente_signup.post("/api/v1/auth/signup", json=datos)
    assert respuesta.status_code == 422


@respx.mock
async def test_signup_email_ya_registrado_devuelve_409(
    cliente_signup: AsyncClient, respx_mock: respx.MockRouter
) -> None:
    mock_invite_ok(respx_mock)
    primera = await cliente_signup.post("/api/v1/auth/signup", json=DATOS_VALIDOS)
    assert primera.status_code == 201
    segunda = await cliente_signup.post("/api/v1/auth/signup", json=DATOS_VALIDOS)
    assert segunda.status_code == 409


@respx.mock
async def test_supabase_caido_no_deja_datos_a_medias(
    cliente_signup: AsyncClient, sesion_db: AsyncSession, respx_mock: respx.MockRouter
) -> None:
    from src.models import Protectora

    respx_mock.post(f"{SUPABASE_URL}/auth/v1/invite").respond(500)
    respuesta = await cliente_signup.post("/api/v1/auth/signup", json=DATOS_VALIDOS)
    assert respuesta.status_code == 503
    assert await sesion_db.scalar(select(Protectora)) is None


@respx.mock
async def test_fallo_de_bd_elimina_la_cuenta_creada(
    cliente_signup: AsyncClient,
    respx_mock: respx.MockRouter,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Compensación: si la BD falla tras crear la cuenta, la cuenta se borra."""
    from src.api import auth as api_auth

    mock_invite_ok(respx_mock)
    borrado = respx_mock.delete(f"{SUPABASE_URL}/auth/v1/admin/users/{CUENTA_ID}").respond(200)

    async def _explota(*args: object, **kwargs: object) -> None:
        raise RuntimeError("bd caida")

    monkeypatch.setattr(api_auth, "_crear_filas", _explota)
    respuesta = await cliente_signup.post("/api/v1/auth/signup", json=DATOS_VALIDOS)
    assert respuesta.status_code == 500
    assert borrado.called


@respx.mock
async def test_rate_limit_en_signup(
    cliente_signup: AsyncClient, respx_mock: respx.MockRouter
) -> None:
    # id único por invite, como en producción (si no, chocan las PK de usuario)
    respx_mock.post(f"{SUPABASE_URL}/auth/v1/invite").mock(
        side_effect=lambda request: Response(200, json={"id": str(uuid.uuid4())})
    )
    ultimo = 0
    for i in range(6):
        datos = DATOS_VALIDOS | {"email": f"v{i}@refugio.example", "nombre_protectora": f"R{i}"}
        r = await cliente_signup.post("/api/v1/auth/signup", json=datos)
        ultimo = r.status_code
    assert ultimo == 429

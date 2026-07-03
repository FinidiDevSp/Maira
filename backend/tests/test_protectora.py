"""FEATURE-001 · Tandas 3-4: perfil de protectora, voluntarias e invitaciones."""

import uuid
from collections.abc import AsyncIterator

import pytest
import respx
from httpx import ASGITransport, AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from tests.utils import crear_token

SUPABASE_URL = "https://test-proyecto.supabase.co"


@pytest.fixture(autouse=True)
def limpiar_rate_limit() -> None:
    from src.core import ratelimit

    ratelimit.reiniciar()


@pytest.fixture
async def entorno(sesion_db: AsyncSession) -> dict:
    """Dos protectoras con una usuaria cada una (admin en A, lectura en B)."""
    from src.db.session import get_db
    from src.main import create_app
    from src.models import Protectora, RolUsuario, Usuario

    prot_a = Protectora(nombre="Refugio Esperanza", email="hola@a.example")
    prot_b = Protectora(nombre="Huellas del Sur", email="hola@b.example")
    sesion_db.add_all([prot_a, prot_b])
    await sesion_db.flush()
    admin_a = Usuario(
        protectora_id=prot_a.id, email="lucia@a.example", nombre="Lucía", rol=RolUsuario.ADMIN
    )
    lectura_b = Usuario(
        protectora_id=prot_b.id, email="marta@b.example", nombre="Marta", rol=RolUsuario.LECTURA
    )
    sesion_db.add_all([admin_a, lectura_b])
    await sesion_db.commit()

    app = create_app()

    async def _db() -> AsyncIterator[AsyncSession]:
        yield sesion_db

    app.dependency_overrides[get_db] = _db
    transport = ASGITransport(app=app)
    cliente = AsyncClient(transport=transport, base_url="http://test")
    return {
        "cliente": cliente,
        "prot_a": prot_a,
        "prot_b": prot_b,
        "admin_a": admin_a,
        "lectura_b": lectura_b,
        "sesion": sesion_db,
    }


def _auth(usuario_id: uuid.UUID) -> dict[str, str]:
    return {"Authorization": f"Bearer {crear_token(usuario_id)}"}


async def test_me_sin_token_devuelve_401(entorno: dict) -> None:
    respuesta = await entorno["cliente"].get("/api/v1/protectora/me")
    assert respuesta.status_code == 401


async def test_me_devuelve_la_protectora_propia(entorno: dict) -> None:
    respuesta = await entorno["cliente"].get(
        "/api/v1/protectora/me", headers=_auth(entorno["admin_a"].id)
    )
    assert respuesta.status_code == 200
    assert respuesta.json()["nombre"] == "Refugio Esperanza"

    respuesta_b = await entorno["cliente"].get(
        "/api/v1/protectora/me", headers=_auth(entorno["lectura_b"].id)
    )
    assert respuesta_b.json()["nombre"] == "Huellas del Sur"  # aislamiento multi-tenant


async def test_patch_me_como_admin_actualiza(entorno: dict) -> None:
    respuesta = await entorno["cliente"].patch(
        "/api/v1/protectora/me",
        headers=_auth(entorno["admin_a"].id),
        json={"descripcion_publica": "Protectora rural de Toledo"},
    )
    assert respuesta.status_code == 200
    assert respuesta.json()["descripcion_publica"] == "Protectora rural de Toledo"


async def test_patch_me_como_lectura_prohibido(entorno: dict) -> None:
    respuesta = await entorno["cliente"].patch(
        "/api/v1/protectora/me",
        headers=_auth(entorno["lectura_b"].id),
        json={"nombre": "Hackeada"},
    )
    assert respuesta.status_code == 403


async def test_listar_usuarias_solo_de_mi_protectora(entorno: dict) -> None:
    respuesta = await entorno["cliente"].get(
        "/api/v1/protectora/usuarios", headers=_auth(entorno["admin_a"].id)
    )
    assert respuesta.status_code == 200
    emails = [u["email"] for u in respuesta.json()]
    assert emails == ["lucia@a.example"]  # nunca las de la protectora B


@respx.mock
async def test_invitar_como_admin_crea_usuaria(entorno: dict, respx_mock: respx.MockRouter) -> None:
    from src.models import RolUsuario, Usuario

    nueva_id = uuid.uuid4()
    respx_mock.post(f"{SUPABASE_URL}/auth/v1/invite").respond(200, json={"id": str(nueva_id)})
    respuesta = await entorno["cliente"].post(
        "/api/v1/protectora/usuarios",
        headers=_auth(entorno["admin_a"].id),
        json={"email": "carmen@a.example", "rol": "editor"},
    )
    assert respuesta.status_code == 201, respuesta.text

    nueva = await entorno["sesion"].scalar(
        select(Usuario).where(Usuario.email == "carmen@a.example")
    )
    assert nueva is not None
    assert nueva.id == nueva_id
    assert nueva.rol is RolUsuario.EDITOR
    assert nueva.protectora_id == entorno["prot_a"].id


async def test_invitar_sin_ser_admin_prohibido(entorno: dict) -> None:
    respuesta = await entorno["cliente"].post(
        "/api/v1/protectora/usuarios",
        headers=_auth(entorno["lectura_b"].id),
        json={"email": "x@b.example", "rol": "editor"},
    )
    assert respuesta.status_code == 403


async def test_invitar_email_ya_existente_devuelve_409(entorno: dict) -> None:
    respuesta = await entorno["cliente"].post(
        "/api/v1/protectora/usuarios",
        headers=_auth(entorno["admin_a"].id),
        json={"email": "marta@b.example", "rol": "editor"},
    )
    assert respuesta.status_code == 409


async def test_invitar_con_rol_invalido_rechazado(entorno: dict) -> None:
    respuesta = await entorno["cliente"].post(
        "/api/v1/protectora/usuarios",
        headers=_auth(entorno["admin_a"].id),
        json={"email": "y@a.example", "rol": "superusuaria"},
    )
    assert respuesta.status_code == 422

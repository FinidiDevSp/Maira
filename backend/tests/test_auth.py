"""FEATURE-001 · Tanda 1: verificación de JWT de Supabase y autorización por rol."""

import uuid
from collections.abc import AsyncIterator
from datetime import UTC, datetime, timedelta

import jwt
import pytest
from fastapi import Depends, FastAPI
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

SECRETO_TEST = "secreto-jwt-solo-tests-0123456789abcdef"


def crear_token(
    sub: uuid.UUID | str,
    *,
    minutos: int = 60,
    aud: str = "authenticated",
    secreto: str = SECRETO_TEST,
) -> str:
    ahora = datetime.now(UTC)
    return jwt.encode(
        {"sub": str(sub), "aud": aud, "iat": ahora, "exp": ahora + timedelta(minutes=minutos)},
        secreto,
        algorithm="HS256",
    )


@pytest.fixture
async def entorno_auth(sesion_db: AsyncSession) -> dict:
    """App mínima con rutas protegidas + una usuaria rol lectura en BD."""
    from src.core.auth import get_usuario_actual, requiere_rol
    from src.core.exceptions import registrar_handlers
    from src.db.session import get_db
    from src.models import Protectora, RolUsuario, Usuario

    protectora = Protectora(nombre="Refugio Esperanza", email="hola@refugio.example")
    sesion_db.add(protectora)
    await sesion_db.flush()
    usuaria = Usuario(
        protectora_id=protectora.id,
        email="lucia@refugio.example",
        nombre="Lucía",
        rol=RolUsuario.LECTURA,
    )
    sesion_db.add(usuaria)
    await sesion_db.commit()

    app = FastAPI()
    registrar_handlers(app)

    @app.get("/protegida")
    async def protegida(usuario: Usuario = Depends(get_usuario_actual)) -> dict[str, str]:
        return {"email": usuario.email}

    @app.get("/solo-admin", dependencies=[Depends(requiere_rol(RolUsuario.ADMIN))])
    async def solo_admin() -> dict[str, bool]:
        return {"ok": True}

    async def _db() -> AsyncIterator[AsyncSession]:
        yield sesion_db

    app.dependency_overrides[get_db] = _db
    return {"app": app, "usuaria": usuaria, "sesion": sesion_db}


async def _get(entorno: dict, ruta: str, token: str | None):
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    transport = ASGITransport(app=entorno["app"])
    async with AsyncClient(transport=transport, base_url="http://test") as cliente:
        return await cliente.get(ruta, headers=headers)


async def test_sin_token_devuelve_401_problem_json(entorno_auth: dict) -> None:
    respuesta = await _get(entorno_auth, "/protegida", None)
    assert respuesta.status_code == 401
    assert respuesta.headers["content-type"].startswith("application/problem+json")
    assert respuesta.headers["www-authenticate"] == "Bearer"


async def test_token_firmado_con_otra_clave_devuelve_401(entorno_auth: dict) -> None:
    token = crear_token(entorno_auth["usuaria"].id, secreto="clave-de-un-atacante-123456789")
    respuesta = await _get(entorno_auth, "/protegida", token)
    assert respuesta.status_code == 401


async def test_token_expirado_devuelve_401(entorno_auth: dict) -> None:
    token = crear_token(entorno_auth["usuaria"].id, minutos=-5)
    respuesta = await _get(entorno_auth, "/protegida", token)
    assert respuesta.status_code == 401


async def test_audiencia_incorrecta_devuelve_401(entorno_auth: dict) -> None:
    token = crear_token(entorno_auth["usuaria"].id, aud="otra-audiencia")
    respuesta = await _get(entorno_auth, "/protegida", token)
    assert respuesta.status_code == 401


async def test_token_valido_sin_perfil_devuelve_403(entorno_auth: dict) -> None:
    token = crear_token(uuid.uuid4())  # cuenta auth sin fila en usuario
    respuesta = await _get(entorno_auth, "/protegida", token)
    assert respuesta.status_code == 403


async def test_token_valido_devuelve_usuaria(entorno_auth: dict) -> None:
    token = crear_token(entorno_auth["usuaria"].id)
    respuesta = await _get(entorno_auth, "/protegida", token)
    assert respuesta.status_code == 200
    assert respuesta.json() == {"email": "lucia@refugio.example"}


async def test_rol_lectura_no_accede_a_ruta_admin(entorno_auth: dict) -> None:
    token = crear_token(entorno_auth["usuaria"].id)
    respuesta = await _get(entorno_auth, "/solo-admin", token)
    assert respuesta.status_code == 403
    assert "permiso" in respuesta.json()["detail"].lower()


async def test_rol_admin_accede_a_ruta_admin(entorno_auth: dict) -> None:
    from src.models import RolUsuario

    entorno_auth["usuaria"].rol = RolUsuario.ADMIN
    await entorno_auth["sesion"].commit()
    token = crear_token(entorno_auth["usuaria"].id)
    respuesta = await _get(entorno_auth, "/solo-admin", token)
    assert respuesta.status_code == 200

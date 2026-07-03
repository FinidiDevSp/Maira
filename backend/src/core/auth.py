"""Autenticación y autorización (D-015).

El frontend obtiene la sesión con Supabase Auth; aquí SOLO se verifica el JWT
(firma + expiración + audiencia) y se resuelve el rol desde la tabla usuario.
Verificación: JWKS del proyecto (asimétrica) o, si `SUPABASE_JWT_SECRET` está
definida, HS256 legacy.
"""

import uuid
from collections.abc import Awaitable, Callable
from functools import lru_cache
from typing import Any

import jwt
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import get_settings
from src.core.exceptions import NoAutenticadoError, ProhibidoError
from src.db.session import get_db
from src.models import RolUsuario, Usuario

_esquema_bearer = HTTPBearer(auto_error=False)

MENSAJE_TOKEN_INVALIDO = "La sesión no es válida o ha caducado. Vuelve a iniciar sesión."


@lru_cache
def _jwks_client() -> jwt.PyJWKClient:
    settings = get_settings()
    if not settings.supabase_url:
        raise NoAutenticadoError(MENSAJE_TOKEN_INVALIDO)
    return jwt.PyJWKClient(f"{settings.supabase_url}/auth/v1/.well-known/jwks.json")


def _decodificar(token: str) -> dict[str, Any]:
    settings = get_settings()
    try:
        if settings.supabase_jwt_secret:
            return jwt.decode(
                token,
                settings.supabase_jwt_secret,
                algorithms=["HS256"],
                audience="authenticated",
            )
        clave = _jwks_client().get_signing_key_from_jwt(token).key
        return jwt.decode(token, clave, algorithms=["ES256", "RS256"], audience="authenticated")
    except jwt.PyJWTError as exc:
        raise NoAutenticadoError(MENSAJE_TOKEN_INVALIDO) from exc


async def get_usuario_actual(
    credenciales: HTTPAuthorizationCredentials | None = Depends(_esquema_bearer),
    db: AsyncSession = Depends(get_db),
) -> Usuario:
    """Dependencia base: token verificado + perfil existente en la protectora."""
    if credenciales is None:
        raise NoAutenticadoError("Necesitas iniciar sesión para hacer esto.")
    payload = _decodificar(credenciales.credentials)
    try:
        usuario_id = uuid.UUID(str(payload["sub"]))
    except (KeyError, ValueError) as exc:
        raise NoAutenticadoError(MENSAJE_TOKEN_INVALIDO) from exc
    usuario = await db.get(Usuario, usuario_id)
    if usuario is None:
        raise ProhibidoError("Tu cuenta no está vinculada a ninguna protectora.")
    return usuario


def requiere_rol(*roles: RolUsuario) -> Callable[..., Awaitable[Usuario]]:
    """Autorización por rol. La RLS de la BD es la segunda línea, no la primera."""

    async def _dependencia(usuario: Usuario = Depends(get_usuario_actual)) -> Usuario:
        if usuario.rol not in roles:
            raise ProhibidoError("No tienes permiso para hacer esta acción.")
        return usuario

    return _dependencia

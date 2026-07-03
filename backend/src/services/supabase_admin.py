"""Cliente de la admin API de Supabase Auth (GoTrue) — solo backend, con service key.

D-015: el alta es passwordless. /invite crea la cuenta y envía el email con el
enlace de acceso; Supabase gestiona el correo (límites del free tier: ~4/hora,
suficiente para la protectora piloto).
"""

import uuid

import httpx
import structlog

from src.config import Settings, get_settings
from src.core.exceptions import AppError

logger = structlog.get_logger()

MENSAJE_NO_DISPONIBLE = (
    "Ahora mismo no podemos completar el registro. Inténtalo de nuevo en unos minutos."
)


class ServicioAuthNoDisponibleError(AppError):
    status = 503
    title = "Servicio no disponible"


def _config() -> Settings:
    settings = get_settings()
    if not settings.supabase_url or not settings.supabase_service_key:
        logger.error("supabase_admin_sin_configurar")
        raise ServicioAuthNoDisponibleError(MENSAJE_NO_DISPONIBLE)
    return settings


def _headers(settings: Settings) -> dict[str, str]:
    clave = settings.supabase_service_key or ""
    return {"apikey": clave, "Authorization": f"Bearer {clave}"}


async def crear_cuenta_invitada(email: str) -> uuid.UUID:
    """Crea la cuenta y dispara el email de invitación. Devuelve el id de la cuenta."""
    settings = _config()
    # El enlace del email debe aterrizar en el callback del frontend (misma
    # origin que CORS), que sabe procesar todos los formatos de sesión.
    destino = settings.cors_origins_list[0].rstrip("/") + "/auth/callback"
    try:
        async with httpx.AsyncClient(timeout=10) as cliente:
            respuesta = await cliente.post(
                f"{settings.supabase_url}/auth/v1/invite",
                headers=_headers(settings),
                params={"redirect_to": destino},
                json={"email": email},
            )
        respuesta.raise_for_status()
        return uuid.UUID(str(respuesta.json()["id"]))
    except (httpx.HTTPError, KeyError, ValueError) as exc:
        logger.error("supabase_invite_fallo", error=str(exc))
        raise ServicioAuthNoDisponibleError(MENSAJE_NO_DISPONIBLE) from exc


async def eliminar_cuenta(cuenta_id: uuid.UUID) -> None:
    """Compensación best-effort: borra una cuenta creada si el alta no se completó."""
    settings = _config()
    try:
        async with httpx.AsyncClient(timeout=10) as cliente:
            await cliente.delete(
                f"{settings.supabase_url}/auth/v1/admin/users/{cuenta_id}",
                headers=_headers(settings),
            )
    except httpx.HTTPError as exc:
        # Se registra para limpieza manual; no se propaga (ya estamos en un error)
        logger.error("supabase_compensacion_fallo", cuenta_id=str(cuenta_id), error=str(exc))

"""Alta de protectora (US-1.1). El login es magic link desde el frontend (D-015)."""

import uuid

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.exceptions import AppError, ConflictoError
from src.core.ratelimit import limitar
from src.db.session import get_db
from src.models import Protectora, RolUsuario, Usuario
from src.schemas.auth import SignupRequest, SignupResponse
from src.services.supabase_admin import crear_cuenta_invitada, eliminar_cuenta

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])


async def _crear_filas(db: AsyncSession, datos: SignupRequest, cuenta_id: uuid.UUID) -> Protectora:
    protectora = Protectora(
        nombre=datos.nombre_protectora,
        email=datos.email,
        cif=datos.cif,
        direccion=datos.direccion,
        telefono=datos.telefono,
        persona_responsable=datos.persona_responsable,
    )
    db.add(protectora)
    await db.flush()
    db.add(
        Usuario(
            id=cuenta_id,  # mismo id que la cuenta de Supabase Auth (auth.uid)
            protectora_id=protectora.id,
            email=datos.email,
            nombre=datos.persona_responsable,
            rol=RolUsuario.ADMIN,
        )
    )
    await db.commit()
    return protectora


@router.post(
    "/signup",
    status_code=201,
    dependencies=[Depends(limitar("signup", maximo=5, ventana_s=60))],
)
async def signup(datos: SignupRequest, db: AsyncSession = Depends(get_db)) -> SignupResponse:
    existente = await db.scalar(select(Usuario).where(Usuario.email == datos.email))
    if existente is not None:
        raise ConflictoError("Ya existe una cuenta con ese email. Prueba a iniciar sesión.")

    cuenta_id = await crear_cuenta_invitada(datos.email)
    try:
        protectora = await _crear_filas(db, datos, cuenta_id)
    except Exception as exc:
        await eliminar_cuenta(cuenta_id)
        raise AppError("No hemos podido completar el registro. Inténtalo de nuevo.") from exc

    return SignupResponse(
        protectora_id=protectora.id,
        usuario_id=cuenta_id,
        mensaje="Registro completado. Revisa tu correo: te hemos enviado un enlace para entrar.",
    )

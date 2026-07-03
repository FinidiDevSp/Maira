"""Perfil de la protectora y gestión de voluntarias (US-1.3, US-1.4)."""

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.auth import get_usuario_actual, requiere_rol
from src.core.exceptions import AppError, ConflictoError, NoEncontradoError
from src.core.ratelimit import limitar
from src.db.session import get_db
from src.models import Protectora, RolUsuario, Usuario
from src.schemas.protectora import (
    InvitacionRequest,
    InvitacionResponse,
    ProtectoraOut,
    ProtectoraUpdate,
    UsuarioOut,
)
from src.services.supabase_admin import crear_cuenta_invitada, eliminar_cuenta

router = APIRouter(prefix="/api/v1/protectora", tags=["protectora"])


async def _protectora_de(usuario: Usuario, db: AsyncSession) -> Protectora:
    protectora = await db.get(Protectora, usuario.protectora_id)
    if protectora is None:
        raise NoEncontradoError("Tu protectora ya no existe. Contacta con soporte.")
    return protectora


@router.get("/me")
async def ver_perfil(
    usuario: Usuario = Depends(get_usuario_actual),
    db: AsyncSession = Depends(get_db),
) -> ProtectoraOut:
    return ProtectoraOut.model_validate(await _protectora_de(usuario, db))


@router.patch("/me")
async def editar_perfil(
    datos: ProtectoraUpdate,
    usuario: Usuario = Depends(requiere_rol(RolUsuario.ADMIN, RolUsuario.EDITOR)),
    db: AsyncSession = Depends(get_db),
) -> ProtectoraOut:
    protectora = await _protectora_de(usuario, db)
    for campo, valor in datos.model_dump(exclude_unset=True).items():
        setattr(protectora, campo, valor)
    await db.commit()
    await db.refresh(protectora)
    return ProtectoraOut.model_validate(protectora)


@router.get("/usuarios")
async def listar_usuarias(
    usuario: Usuario = Depends(get_usuario_actual),
    db: AsyncSession = Depends(get_db),
) -> list[UsuarioOut]:
    resultado = await db.scalars(
        select(Usuario)
        .where(Usuario.protectora_id == usuario.protectora_id)
        .order_by(Usuario.created_at)
    )
    return [UsuarioOut.model_validate(u) for u in resultado]


@router.post(
    "/usuarios",
    status_code=201,
    dependencies=[Depends(limitar("invitar", maximo=5, ventana_s=60))],
)
async def invitar_usuaria(
    datos: InvitacionRequest,
    usuario: Usuario = Depends(requiere_rol(RolUsuario.ADMIN)),
    db: AsyncSession = Depends(get_db),
) -> InvitacionResponse:
    existente = await db.scalar(select(Usuario).where(Usuario.email == datos.email))
    if existente is not None:
        raise ConflictoError("Esa persona ya tiene cuenta en Maira.")

    cuenta_id = await crear_cuenta_invitada(datos.email)
    try:
        db.add(
            Usuario(
                id=cuenta_id,
                protectora_id=usuario.protectora_id,
                email=datos.email,
                rol=datos.rol,
            )
        )
        await db.commit()
    except Exception as exc:
        await eliminar_cuenta(cuenta_id)
        raise AppError("No hemos podido completar la invitación. Inténtalo de nuevo.") from exc

    return InvitacionResponse(
        usuario_id=cuenta_id,
        mensaje=f"Invitación enviada a {datos.email}. Le llegará un enlace para entrar.",
    )

"""FEATURE-000 · Tarea TDD 3-4: modelos baseline (protectora, usuario) persisten y se consultan."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def test_protectora_se_crea_y_recupera(sesion_db: AsyncSession) -> None:
    from src.models.protectora import Protectora

    protectora = Protectora(nombre="Refugio Esperanza", email="hola@refugioesperanza.example")
    sesion_db.add(protectora)
    await sesion_db.commit()

    resultado = await sesion_db.scalar(
        select(Protectora).where(Protectora.nombre == "Refugio Esperanza")
    )
    assert resultado is not None
    assert resultado.id is not None
    assert resultado.email == "hola@refugioesperanza.example"


async def test_usuario_pertenece_a_protectora_con_rol(sesion_db: AsyncSession) -> None:
    from src.models.protectora import Protectora
    from src.models.usuario import RolUsuario, Usuario

    protectora = Protectora(nombre="Refugio Esperanza", email="hola@refugioesperanza.example")
    sesion_db.add(protectora)
    await sesion_db.flush()

    usuaria = Usuario(
        protectora_id=protectora.id,
        email="lucia@refugioesperanza.example",
        nombre="Lucía",
        rol=RolUsuario.ADMIN,
    )
    sesion_db.add(usuaria)
    await sesion_db.commit()

    resultado = await sesion_db.scalar(
        select(Usuario).where(Usuario.email == "lucia@refugioesperanza.example")
    )
    assert resultado is not None
    assert resultado.rol is RolUsuario.ADMIN
    assert resultado.protectora_id == protectora.id

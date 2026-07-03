"""Seed de desarrollo: protectora ficticia + usuaria admin (idempotente).

Uso: python scripts/seed.py   (con DATABASE_URL apuntando a la BD de dev)
Datos 100% ficticios: el repo es público.
"""

import asyncio

from sqlalchemy import select

from src.db.session import get_session_factory
from src.models import Protectora, RolUsuario, Usuario


async def seed() -> None:
    async with get_session_factory()() as sesion:
        existente = await sesion.scalar(
            select(Protectora).where(Protectora.nombre == "Refugio Esperanza")
        )
        if existente:
            print("Seed ya aplicado: Refugio Esperanza existe.")
            return

        protectora = Protectora(
            nombre="Refugio Esperanza",
            email="hola@refugioesperanza.example",
            direccion="Camino de los Olivos 12, Toledo",
            telefono="+34 600 000 000",
            persona_responsable="Lucía Ejemplo",
            descripcion_publica="Protectora ficticia de desarrollo. Ningún dato es real.",
        )
        sesion.add(protectora)
        await sesion.flush()
        sesion.add(
            Usuario(
                protectora_id=protectora.id,
                email="lucia@refugioesperanza.example",
                nombre="Lucía Ejemplo",
                rol=RolUsuario.ADMIN,
            )
        )
        await sesion.commit()
        print("Seed aplicado: Refugio Esperanza + usuaria admin.")


if __name__ == "__main__":
    asyncio.run(seed())

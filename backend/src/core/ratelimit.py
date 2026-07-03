"""Rate limiting en memoria (suficiente para la instancia única de Render free).

Si en fase 2 hay varias instancias, migrar a un almacén compartido (T-009).
"""

import time
from collections import defaultdict, deque
from collections.abc import Awaitable, Callable

from fastapi import Request

from src.core.exceptions import AppError


class DemasiadasPeticionesError(AppError):
    status = 429
    title = "Demasiados intentos"


_registros: dict[str, deque[float]] = defaultdict(deque)


def reiniciar() -> None:
    """Solo para tests."""
    _registros.clear()


def limitar(
    nombre: str, maximo: int = 5, ventana_s: int = 60
) -> Callable[[Request], Awaitable[None]]:
    async def _dependencia(request: Request) -> None:
        ip = request.client.host if request.client else "desconocida"
        clave = f"{nombre}:{ip}"
        ahora = time.monotonic()
        cola = _registros[clave]
        while cola and ahora - cola[0] > ventana_s:
            cola.popleft()
        if len(cola) >= maximo:
            raise DemasiadasPeticionesError(
                "Has hecho demasiados intentos seguidos. Espera un minuto y vuelve a probar."
            )
        cola.append(ahora)

    return _dependencia

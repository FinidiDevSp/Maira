"""Excepciones de aplicación → respuestas RFC 7807 (Problem Details) en español llano.

Regla (docs/technical/API_CONTRACTS.md): los mensajes los lee una voluntaria,
no un dev — nada de trazas ni jerga.
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class AppError(Exception):
    """Base: error controlado con estado HTTP y mensaje para la usuaria."""

    status: int = 500
    title: str = "Error interno"

    def __init__(self, detail: str) -> None:
        super().__init__(detail)
        self.detail = detail


class NoAutenticadoError(AppError):
    status = 401
    title = "Sesión no válida"


class ProhibidoError(AppError):
    status = 403
    title = "Permiso insuficiente"


class NoEncontradoError(AppError):
    status = 404
    title = "No encontrado"


class ConflictoError(AppError):
    status = 409
    title = "Conflicto"


async def _handler_app_error(request: Request, exc: Exception) -> JSONResponse:
    assert isinstance(exc, AppError)
    headers = {"WWW-Authenticate": "Bearer"} if exc.status == 401 else None
    return JSONResponse(
        status_code=exc.status,
        media_type="application/problem+json",
        headers=headers,
        content={
            "type": "about:blank",
            "title": exc.title,
            "status": exc.status,
            "detail": exc.detail,
        },
    )


def registrar_handlers(app: FastAPI) -> None:
    app.add_exception_handler(AppError, _handler_app_error)

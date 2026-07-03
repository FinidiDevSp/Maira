"""Punto de entrada de la API de Maira."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import health
from src.config import get_settings
from src.core.logging import configurar_logging
from src.core.middleware import SecurityHeadersMiddleware


def create_app() -> FastAPI:
    settings = get_settings()
    configurar_logging(settings.environment)

    app = FastAPI(
        title="Maira API",
        version="0.0.1",
        description="Plataforma open source para protectoras de animales pequeñas.",
        docs_url="/docs" if settings.environment == "development" else None,
    )
    app.add_middleware(SecurityHeadersMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(health.router)
    return app


app = create_app()

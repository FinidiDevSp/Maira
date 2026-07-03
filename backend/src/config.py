"""Configuración de la aplicación.

Toda variable viene del entorno (.env en local, dashboard en Render). Si falta
una obligatoria, la app NO arranca: mejor un error claro al inicio que un fallo
a mitad de una petición.
"""

from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    environment: Literal["development", "production"] = "development"
    secret_key: str = Field(min_length=32)
    cors_origins: str = "http://localhost:3000"
    database_url: str

    # Servicios externos: opcionales hasta la feature que los usa (001+)
    supabase_url: str | None = None
    supabase_anon_key: str | None = None
    supabase_service_key: str | None = None
    # Solo si el proyecto Supabase usa la clave JWT legacy (HS256); con JWKS no hace falta
    supabase_jwt_secret: str | None = None
    llm_provider: Literal["groq", "gemini"] = "groq"
    groq_api_key: str | None = None
    gemini_api_key: str | None = None
    hf_api_token: str | None = None
    qdrant_url: str | None = None
    qdrant_api_key: str | None = None
    healthchecks_ping_url: str | None = None

    @property
    def cors_origins_list(self) -> list[str]:
        return [origen.strip() for origen in self.cors_origins.split(",") if origen.strip()]


@lru_cache
def get_settings() -> Settings:
    # Los campos obligatorios llegan del entorno; mypy no puede saberlo (call-arg).
    return Settings()  # type: ignore[call-arg]

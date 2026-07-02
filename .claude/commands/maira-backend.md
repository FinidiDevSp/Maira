---
description: Referencia backend Maira — patrones FastAPI, SQLAlchemy async, capa LLM
---

# Skill: Backend (FastAPI)

Patrones obligatorios del backend de Maira. Docs: `docs/technical/ARCHITECTURE.md`, `docs/technical/API_CONTRACTS.md`.

## Estructura

`src/api/` (routers finos) → `src/services/` (lógica) → `src/models/` (SQLAlchemy) + `src/schemas/` (Pydantic) + `src/core/` (security, logging, exceptions). Un router NUNCA contiene lógica de negocio ni toca la sesión directamente para lógica compleja.

## Router + dependencias

```python
router = APIRouter(prefix="/api/v1/animales", tags=["animales"])

@router.post("", response_model=AnimalOut, status_code=201)
async def crear_animal(
    datos: AnimalCreate,                                  # Pydantic v2 valida entrada
    usuario: Usuario = Depends(requiere_rol("admin", "editor")),
    db: AsyncSession = Depends(get_db),
) -> AnimalOut:
    return await animal_service.crear(db, datos, usuario)
```

- Auth: `Depends(get_usuario_actual)` verifica el JWT de Supabase; `requiere_rol(...)` autoriza. La RLS de la BD es la segunda línea, no la primera.
- Errores: excepciones custom (`src/core/exceptions.py`) → handler global que emite RFC 7807 en español llano. Nunca `HTTPException` con strings sueltos en services.
- Paginación cursor: `?cursor=X&limit=20` (máx 100), respuesta con `items` + `next_cursor`.

## SQLAlchemy 2.0 async

- Sesión por request con `async_sessionmaker`; transacción por operación de servicio (commit en el service, rollback en el handler global).
- Queries con `select()` estilo 2.0, nunca legacy `Query`.
- Modelos: UUID PK (`server_default=text("gen_random_uuid()")`), `created_at`/`updated_at` TIMESTAMPTZ, enums de dominio en español.
- Migraciones: `alembic revision --autogenerate -m "..."` y SIEMPRE revisar/editar el resultado; `downgrade` real.

## Capa LLM (services/llm.py)

```python
class LLMProvider(Protocol):
    async def complete(self, prompt: Prompt, **kw) -> LLMResponse: ...

def get_provider() -> LLMProvider:   # selección por settings.llm_provider
    ...
```

- Prompts como objetos versionados (`prompt_version` en metadata), datos de usuario SIEMPRE delimitados como dato (ver skill de seguridad).
- Fallo del proveedor primario → fallback automático (Groq→Gemini) → si ambos caen, excepción honesta (503), nunca inventar.
- Outputs validados post-generación (idioma, longitud, patrones prohibidos) antes de persistir.
- Timeouts explícitos (8s fichas, 15s triaje) y logging de tokens/latencia con structlog.

## Config y logging

- `src/config.py` con pydantic-settings: toda variable tipada, la app NO arranca si falta algo.
- structlog JSON a stdout: `logger.info("ficha_generada", animal_id=..., modelo=..., latencia_ms=...)`. Nunca loguear datos personales ni claves.

## Async in-process

Sin broker en MVP (decisión T-010 → fase 2): tareas cortas con `BackgroundTasks` de FastAPI (ping a Healthchecks, logs de auditoría). Nada que el usuario espere se hace en background sin feedback.

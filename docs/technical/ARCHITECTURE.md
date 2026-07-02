# Arquitectura

> Fuente extendida: [`ANALYSIS.md`](../../ANALYSIS.md) §10. Este documento es la referencia operativa.

## Diagrama lógico

```
Next.js 14 (Vercel) ──HTTPS──► FastAPI (Render free)
                                    │
              ┌─────────────────────┼──────────────────────┐
              ▼                     ▼                      ▼
      Supabase PostgreSQL    Supabase Storage        Qdrant Cloud
      (+ Auth + RLS)         (fotos, URLs firmadas)  (RAG guías vet)
                                    │
                     ┌──────────────┴──────────────┐
                     ▼                             ▼
              Groq (llama-3.1-70b)          HuggingFace (CLIP)
              fallback: Gemini 1.5 Flash    features de imagen
```

Todo en **free tiers** (restricción TFM: coste 0€). Docker local (`maira-*`) como plan B de demo.

## Stack

| Capa | Tecnología |
|---|---|
| Frontend | Next.js 14 App Router · TypeScript estricto · Tailwind · shadcn/ui · React Hook Form + Zod · TanStack Query · next-intl |
| Backend | Python 3.11 · FastAPI · SQLAlchemy 2.0 async · Alembic · Pydantic v2 · structlog |
| Datos | Supabase PostgreSQL (RLS) · Supabase Auth (magic link) · Supabase Storage · Qdrant Cloud |
| IA | Groq `llama-3.1-70b-versatile` (fallback Gemini 1.5 Flash) · CLIP en HF · embeddings `paraphrase-multilingual-MiniLM-L12-v2` |
| Calidad | pytest + httpx + respx · ruff · mypy · Vitest · Playwright · axe/pa11y |
| Ops | Render + Vercel + Healthchecks.io · GitHub Actions · Docker compose local |

## Principios

1. **Monolito modular** en backend (ADR-001): routers finos → servicios → modelos. Nada de microservicios.
2. **Capa de abstracción LLM** (`services/llm.py`, protocolo `LLMProvider`): cambiar Groq↔Gemini es una env var (`LLM_PROVIDER`).
3. **Multi-tenant por RLS** (ADR-006): 1 protectora en MVP, diseñado para 50 sin cambios de arquitectura.
4. **Sin lock-in**: SQLAlchemy desacopla de Supabase; export CSV/JSON siempre disponible.
5. **API REST versionada** `/api/v1`, errores RFC 7807, paginación cursor. Ver [API_CONTRACTS](API_CONTRACTS.md).
6. **Async por defecto** en todo I/O del backend.

## Estructura del repositorio (monorepo)

```
Maira/
├── backend/          # FastAPI (src/api, src/services, src/models, src/core, tests/)  ← FEATURE-000
├── frontend/         # Next.js (src/app, src/components, src/lib, tests/)             ← FEATURE-000
├── docker/           # Dockerfiles multi-stage (backend, frontend)
├── docs/             # documentación por áreas (este sitio MkDocs)
├── scripts/          # render_planning.py, seed, backup
├── .claude/          # skills + agentes del Consejo de Alexandria SDD
└── .github/          # CI, plantillas
```

El detalle interno de `backend/` y `frontend/` sigue la estructura de `ANALYSIS.md` §10.

## Internacionalización

- **MVP: solo español (es-ES)**, pero preparado: `next-intl` con ficheros de mensajes desde el primer componente (nada de strings hardcodeados en JSX), campo `lang` en `protectora`, mensajes de error del backend centralizados.
- Post-MVP: catalán, euskera, gallego (fase 2); portugués e inglés (fase 3).
- Convenciones: fechas `DD/MM/AAAA`, números `1.234,56`, moneda `€` pospuesto, teléfono `+34 600 000 000`.

## Decisiones

Registradas con contexto y fecha en [DECISIONS.md](DECISIONS.md).

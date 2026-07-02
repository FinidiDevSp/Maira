---
id: FEATURE-000
tipo: feature
titulo: "Inicialización y andamiaje del proyecto"
estado: listo
prioridad: alta
hito: "0.1"
duplicado_de: null
creado: 2026-07-02
actualizado: 2026-07-02
---

# FEATURE-000 — Inicialización y andamiaje del proyecto

## Descripción

Primer item de todo proyecto: dejar el esqueleto técnico funcionando de extremo a extremo para que el resto de features se construyan encima. Al terminar, un juez (o cualquier persona) puede clonar el repo, levantarlo y ver "Maira" respondiendo.

## Contexto / impacto

Sin esto no hay nada demostrable. Corresponde a la "Fase 0 — Pre-MVP" de `ANALYSIS.md`: esqueleto FastAPI, esqueleto Next.js, Supabase con esquema inicial y despliegues en free tiers.

## Plan de desarrollo

### Documentación a consultar
- `docs/technical/ARCHITECTURE.md` (stack exacto y estructura de carpetas)
- `docs/technical/DATA_MODEL.md` (esquema baseline)
- `docs/operations/SETUP.md` y `docs/operations/ENVIRONMENT.md`

### Seguridad
- `.env` fuera de git desde el primer commit (repo público).
- CORS restringido a los orígenes de `CORS_ORIGINS`.
- Headers de seguridad base en FastAPI (middleware).

### Modelo de datos
- Migración Alembic baseline: tablas `protectora` y `usuario` (mínimas).

### API
- `GET /health` → `{"status": "ok"}` (usado por Healthchecks.io y Render).
- Esqueleto de routers versionados bajo `/api/v1`.

### Frontend
- Next.js 14 App Router con TypeScript estricto, Tailwind, shadcn/ui inicializado.
- Página raíz que muestra "Maira" y el estado del backend (fetch a `/health`).
- Tokens de color de `docs/technical/DESIGN.md` en `tailwind.config.ts` + dark mode.

### Tareas TDD
1. Test `GET /health` devuelve 200 y JSON esperado → implementar endpoint.
2. Test de configuración: settings leen de env y fallan claro si falta algo → implementar `config.py` (pydantic-settings).
3. Test de sesión de BD async (fixture con SQLite/testcontainer) → implementar `db/`.
4. Migración baseline aplica y revierte limpia (`alembic upgrade head` / `downgrade base`).
5. Frontend: test de render de la home (Vitest + Testing Library).
6. `docker compose --profile app up` levanta db + qdrant + backend + frontend end-to-end.

### Dependencias
- Ninguna (es el primer item).

## Criterios de aceptación / Casuística a cubrir

- [ ] `pytest` en verde con cobertura ≥ 70% de lo existente.
- [ ] `GET /health` responde 200 en local y en Render.
- [ ] La home en Vercel carga y muestra el estado del backend.
- [ ] `docker compose --profile app up` funciona en máquina limpia (plan B de demo).
- [ ] CI en verde (lint + tests + docs + render de planificación).
- [ ] Sin secretos en el repo (repo público): revisión de `git log` y `.env.example` sin valores reales.
- [ ] Con el backend dormido (Render free), la home explica "arrancando…" en vez de fallar.

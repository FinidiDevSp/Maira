# Decisiones técnicas (ADR)

Formato: contexto → decisión → consecuencias. Las ADR-001..006 provienen de `ANALYSIS.md` (2026-06-28); las D-007+ se tomaron en la inicialización del 2026-07-02.

## ADR-001 — Monolito modular en backend (2026-06-28)

1 dev, 3-4 meses, escala objetivo pequeña. **Decisión:** FastAPI monolítico con módulos (api/services/models), no microservicios. **Consecuencia:** menos ops, refactor a servicios posible si algún día hace falta.

## ADR-002 — Next.js App Router (2026-06-28)

**Decisión:** App Router sobre Pages Router por server components, mejor DX e i18n nativo con next-intl.

## ADR-003 — Supabase sobre Firebase (2026-06-28)

**Decisión:** Supabase por PostgreSQL real, RLS, open source y SQL estándar. **Consecuencia:** migración posible a Neon/RDS gracias a SQLAlchemy (riesgo 8 de ANALYSIS.md).

## ADR-004 — Groq como LLM principal (2026-06-28)

**Decisión:** Groq (`llama-3.1-70b-versatile`) por free tier generoso y latencia mínima; fallback Gemini 1.5 Flash tras capa de abstracción `LLMProvider`. Cambio de proveedor = 1 env var.

## ADR-005 — Licencia AGPL-3.0 (2026-06-28)

**Decisión:** AGPL para que las mejoras vuelvan a la comunidad y evitar forks privativos (incluso como SaaS).

## ADR-006 — Multi-tenant por RLS (2026-06-28)

**Decisión:** una BD con Row Level Security por protectora, no BD por tenant. Suficiente hasta ~50 protectoras.

## D-007 — Restricción transversal: TFM demostrable a coste 0€ (2026-07-02)

**Contexto:** el proyecto se defiende ante un tribunal que debe poder probarlo. **Decisión:** toda elección de infra/servicio debe ser free tier real y estar desplegada públicamente (Vercel + Render + Supabase + Qdrant Cloud + Groq + HF). **Consecuencia:** se aceptan limitaciones (sleep de Render) y se descarta cualquier servicio de pago "aunque sea barato".

## D-008 — Docker como plan B de demo, no como ruta principal (2026-07-02)

**Contexto:** los free tiers pueden fallar el día de la defensa. **Decisión:** mantener `docker-compose.yml` (prefijo `maira-`) capaz de levantar todo end-to-end en local; la ruta principal para los jueces es la URL pública. **Consecuencia:** ensayar `docker compose --profile app up` antes de la defensa (criterio de FEATURE-007).

## D-009 — Dark mode incluido (2026-07-02)

**Decisión del usuario:** dark mode desde el MVP, por defecto según el sistema con toggle. Tokens duales en [DESIGN.md](DESIGN.md).

## D-010 — Sin Sentry en MVP (2026-07-02)

**Contexto:** ANALYSIS.md lo marcaba opcional. **Decisión:** fuera del MVP; la observabilidad se cubre con structlog → logs de Render + Healthchecks.io. **Consecuencia:** revisar tras el MVP si el volumen de errores lo justifica (sigue habiendo free tier).

## D-011 — Monorepo `backend/` + `frontend/` sin `packages/` (2026-07-02)

**Decisión:** respetar la estructura ya fijada en ANALYSIS.md §10 (carpetas planas `backend/` y `frontend/`), sin workspace de npm. Simplifica los deploys separados de Render (root `backend/`) y Vercel (root `frontend/`).

## D-012 — Sistema de items renderizado + pasarela ChatGPT (2026-07-02)

**Decisión:** la planificación vive en `docs/planning/items/*.md` (única verdad); BACKLOG/ROADMAP/catálogo se regeneran con `scripts/render_planning.py`. Una pasarela ChatGPT captura items del analista sin tocar las vistas. **Consecuencia:** CI verifica que las vistas están al día; nadie edita vistas a mano.

## D-013 — Agentes SDD con temática The Walking Dead (2026-07-02)

**Decisión del usuario:** el "Consejo de Alexandria SDD": Rick (orquestador), Hershel (estratega), Deanna (planificadora), Eugene (codificador), Daryl (QA), Milton (memoria/docs). Solo cambia el nombre; los roles del flujo SDD son fijos.

## D-014 — Idioma único español con i18n preparado (2026-07-02)

**Decisión:** solo es-ES en MVP (fijado por ANALYSIS.md §18), pero con next-intl y mensajes centralizados desde el primer componente para que fase 2 (ca/eu/gl) no exija refactor.

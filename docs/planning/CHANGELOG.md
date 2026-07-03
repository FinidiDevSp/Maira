# Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/). Versionado semántico.

## [Sin publicar]

### Añadido (FEATURE-001, en curso)

- Autenticación completa: verificación de JWT de Supabase en backend (JWKS o HS256 legacy), roles admin/editor/lectura, errores RFC 7807 en español llano y rate limiting.
- Registro de protectora passwordless (`POST /api/v1/auth/signup`) con alta atómica y compensación si algo falla a medias.
- Perfil de protectora (ver/editar) y gestión de voluntarias con invitaciones por email y rol.
- Row Level Security en `protectora` y `usuario` (migración 0002, aplicada en Supabase).
- Frontend: login con magic link, registro, callback de sesión, página de perfil con invitaciones (solo admin) e i18n con next-intl desde el primer componente.
- Capturado IMPROVEMENT-001: subida de Next.js por avisos de seguridad de Dependabot.

## [0.0.2] — 2026-07-03

### Añadido

- **Esqueleto backend FastAPI** (FEATURE-000): endpoint `/health`, cabeceras de seguridad, CORS desde configuración, settings validados con pydantic-settings (la app no arranca si falta una variable), logging JSON con structlog.
- Modelos baseline `protectora` y `usuario` (SQLAlchemy 2.0 async) con migración Alembic 0001 reversible (verificada upgrade→downgrade→upgrade contra Postgres real) y seed idempotente con datos ficticios.
- **Esqueleto frontend Next.js 14** (FEATURE-000): tokens de color de DESIGN.md con dark mode (next-themes, según sistema), tipografía Inter, base shadcn/ui, y home que muestra el estado del servicio contemplando el cold start de Render ("arrancando…" con reintento).
- Suite de tests: backend 8/8 (pytest, 100% cobertura) y frontend 3/3 (Vitest + Testing Library); ruff, mypy, ESLint y tsc limpios.
- Verificación end-to-end con Docker: `docker compose --profile app up` levanta los 4 contenedores `maira-*` y la home consume `/health`.
- `dependabot.yml` para pip, npm y GitHub Actions.

### Desplegado (cierre de FEATURE-000)

- **Producción a coste 0€**: frontend en Vercel (https://maira-opal.vercel.app, rama `main`), backend en Render Frankfurt (https://maira-backend-sj81.onrender.com), base de datos Supabase UE con la migración 0001 aplicada. CORS restringido al origen de Vercel. Repo público con CI verde, `main` protegida, CodeQL y Dependabot activos.

## [0.0.1] — 2026-07-02

### Añadido

- Inicialización de la base del proyecto Maira (scaffold de documentación e infraestructura).
- Documentación por áreas en `docs/`: product (PRODUCT_CONTEXT, PLAN, GLOSSARY), technical (ARCHITECTURE, DATA_MODEL, API_CONTRACTS, DESIGN, DECISIONS), planning (BACKLOG, ROADMAP, CHANGELOG, CHATGPT_GATEWAY, items/), operations (SETUP, ENVIRONMENT, OPERATIONS, RUNBOOKS, SECURITY), meta (TESTING, PRIVACY, DOCUMENTATION).
- Sistema de items como única fuente de verdad (`docs/planning/items/`) con render determinista (`scripts/render_planning.py`).
- Items iniciales: FEATURE-000 (andamiaje) y FEATURE-001..007 derivadas del roadmap de ANALYSIS.md, con planes de desarrollo y criterios de aceptación.
- Infraestructura: docker-compose (prefijo `maira-`), Dockerfiles multi-stage, CI de GitHub Actions, Makefile, pre-commit, MkDocs Material, .editorconfig, .gitattributes.
- Skills de Claude adaptadas al stack y agentes SDD con temática The Walking Dead ("Consejo de Alexandria SDD"): Rick, Hershel, Deanna, Eugene, Daryl y Milton.
- Ficheros raíz: README, CLAUDE.md, AGENTS.md, CONTRIBUTING, SECURITY, LICENSE (AGPL-3.0).

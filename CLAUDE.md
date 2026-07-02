# CLAUDE.md — Guía para agentes en Maira

Maira: plataforma open source (AGPL) para protectoras de animales. **Es un TFM que se defiende ante un tribunal: todo debe estar desplegado, accesible y a coste 0€ (free tiers).** Repo público. Todo en español.

## 🧟 Consejo de Alexandria SDD (los 6 agentes de desarrollo)

Punto de entrada único: `/maira-rick "petición"`. Rick clasifica y deriva; cada fase vive en su especialista.

| Agente | Rol | Fichero | Cuándo usarlo directamente |
|---|---|---|---|
| **Rick** | Orquestador | `.claude/commands/maira-rick.md` | Siempre que no sepas por dónde empezar: él deriva |
| **Hershel** | Estratega (RCTF enhancer) | `.claude/commands/maira-hershel.md` | Afinar una petición ambigua antes de planificar |
| **Deanna** | Planificadora SDD | `.claude/commands/maira-deanna.md` | Crear el plan técnico de un item (spec + tareas TDD) |
| **Eugene** | Codificador | `.claude/commands/maira-eugene.md` | Ejecutar un plan aprobado con TDD |
| **Daryl** | QA | `.claude/commands/maira-daryl.md` | Verificar: tests, cobertura, lint, completitud |
| **Milton** | Memoria/Docs | `.claude/commands/maira-milton.md` | Cerrar tarea: render de planificación + docs + CHANGELOG |

Flujo: Rick → (Hershel si es complejo) → Deanna → aprobación del usuario → Eugene → Daryl (si falla, vuelve a Eugene) → Milton → done.

## Regla 0 — Despacho automático de skills

Antes de codificar en un dominio, lee su skill de referencia:

| Si la tarea toca… | Lee |
|---|---|
| Endpoints, servicios, FastAPI, LLM | `.claude/commands/maira-backend.md` |
| Componentes, páginas, Tailwind, shadcn/ui | `.claude/commands/maira-frontend.md` |
| Modelos, migraciones, RLS, queries | `.claude/commands/maira-database.md` |
| Auth, uploads, prompts, secretos | `.claude/commands/maira-security.md` |
| Tests de cualquier capa | `.claude/commands/maira-testing.md` |
| Contenedores, compose, demo local | `.claude/commands/maira-docker.md` |

## Flujo de items (planificación)

- **Única verdad:** `docs/planning/items/*.md`. Nuevo item = copiar `_TEMPLATE.md`, comprobar `INDEX.md` (dedup).
- **Vistas renderizadas** (BACKLOG, ROADMAP, catálogo de PRODUCT_CONTEXT): NUNCA editarlas a mano → `python scripts/render_planning.py`. CI lo verifica.
- La pasarela ChatGPT (analista) también crea items; solo toca `items/`.
- **Apertura de sesión:** lee primero el bloque `📍 Estado actual` de `docs/planning/BACKLOG.md` (~15 líneas).

## Entorno y comandos

- **Windows 11 + PowerShell.** `make` requiere Git Bash/WSL; equivalentes directos en `docs/operations/SETUP.md`.
- Tests: `cd backend && pytest --cov=src` · `cd frontend && npm run test` · E2E: `npx playwright test`.
- Lint: `ruff check . && mypy src` · `npm run lint`.
- Docs: `mkdocs serve -a localhost:8001`.
- Git: trabajo en `develop`; commits Conventional en español; plantilla ya configurada.

## Reglas duras del proyecto

1. **Repo público**: jamás secretos ni datos reales de la piloto en commits, tests o docs.
2. **Coste 0€**: no propongas servicios de pago.
3. **TDD**: test primero; cobertura backend ≥ 70%.
4. **Ética IA**: disclaimers intactos; el triaje nunca "diagnostica"; ante la duda, urgencia más alta.
5. **A11y**: WCAG 2.2 AA; nada de UI que rompa teclado o lector de pantalla.
6. **Español** en código de cara al usuario, commits, docs y mensajes de error.
7. `ANALYSIS.md` (raíz) es la biblia de producto; en conflicto, manda él y se actualiza el doc derivado.

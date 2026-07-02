# Estrategia de testing

> **TDD obligatorio** (ver CONTRIBUTING.md): test que falla → implementación mínima → refactor. Los items traen sus "Tareas TDD" ya ordenadas.

## Pirámide

Muchos unitarios · integración moderada · pocos E2E críticos (los 3 flujos: alta+ficha, registro diario, triaje).

## Backend (objetivo: ≥ 70% cobertura, CI lo exige)

| Qué | Con qué |
|---|---|
| Unitarios de servicios (llm, vision, triage, reglas de anomalías, validadores) | `pytest`, `pytest-asyncio`, `pytest-cov` |
| Endpoints | `httpx.AsyncClient` contra la app FastAPI |
| BD | fixtures async con transacción rollback (SQLite en memoria o testcontainers-postgres para lo que use RLS/trigram) |
| APIs externas (Groq, Gemini, HF, Qdrant) | **`respx`** — nunca llamadas reales en CI (cuotas free tier + determinismo) |
| RLS | tests SQL dedicados: usuaria A no ve datos de B. **Intocables.** |

Convención de nombres: `test_<funcionalidad>_<escenario>_<esperado>`, patrón arrange-act-assert.

## Frontend (objetivo: ≥ 70% en `lib/` y componentes con lógica)

- **Vitest + Testing Library**: componentes con lógica, hooks, validaciones Zod.
- Queries por rol/label (accesibilidad gratis en cada test).
- MSW para mockear la API en tests de componentes.

## E2E — Playwright

Flujos: signup→login→dashboard · alta animal→ficha IA (LLM mockeado) · registro diario · triaje completo. Cross-browser (Chromium + Firefox + WebKit). En CI solo en `main` (lentos); en PR, opcionales.

## Accesibilidad

- `axe-core` (vía axe-playwright) en las pantallas clave — violación crítica = test rojo.
- `pa11y-ci` contra el build en cada deploy.
- Manual pre-release: NVDA + navegación por teclado (checklist en DESIGN.md).

## IA (específico)

- Set de validación de triaje: ≥ 20 casos sintéticos etiquetados; **0 falsos negativos ALTA** es bloqueante de release.
- Prompts versionados (`prompt_version`); un cambio de prompt corre el set completo antes de merge.
- Validadores de output (idioma, longitud, patrones prohibidos) con tests unitarios propios.

## Datos de prueba

`backend/scripts/seed.py` (FEATURE-000/002): protectora ficticia "Refugio Esperanza", 5 animales, 20 registros, 3 triajes. Mismo seed para dev local, demo Docker y fixtures de dashboard.

## En CI

Lint (ruff+mypy / eslint+tsc) → tests con cobertura mínima → build → auditoría deps. Merge a `main` exige todo verde.

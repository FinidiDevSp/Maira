# AGENTS.md

Guía para agentes de IA que trabajen en este repositorio. La versión completa y canónica está en [`CLAUDE.md`](CLAUDE.md); esto es el resumen imprescindible.

## Contexto

Maira: plataforma open source para protectoras de animales. TFM defendido ante tribunal → **desplegable, gratis (free tiers) y repo público presentable**. Todo en español.

## Antes de tocar código

1. Lee el bloque `📍 Estado actual` de `docs/planning/BACKLOG.md`.
2. Lee la skill del dominio que toques en `.claude/commands/` (backend, frontend, database, security, testing, docker).
3. La planificación vive en `docs/planning/items/`; las vistas se regeneran con `python scripts/render_planning.py` (no editar a mano).

## Reglas duras

- TDD obligatorio (cobertura backend ≥ 70%). Bug fix ⇒ test de regresión.
- Sin secretos en el repo (público). Sin servicios de pago.
- Disclaimers de IA intactos; el triaje nunca diagnostica.
- WCAG 2.2 AA; Conventional Commits en español; rama de trabajo → `develop`.

## Verificación

`cd backend && pytest --cov=src` · `cd frontend && npm run test && npm run lint` · `mkdocs build` · CI debe quedar verde.

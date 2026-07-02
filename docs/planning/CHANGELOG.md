# Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/). Versionado semántico.

## [0.0.1] — 2026-07-02

### Añadido

- Inicialización de la base del proyecto Maira (scaffold de documentación e infraestructura).
- Documentación por áreas en `docs/`: product (PRODUCT_CONTEXT, PLAN, GLOSSARY), technical (ARCHITECTURE, DATA_MODEL, API_CONTRACTS, DESIGN, DECISIONS), planning (BACKLOG, ROADMAP, CHANGELOG, CHATGPT_GATEWAY, items/), operations (SETUP, ENVIRONMENT, OPERATIONS, RUNBOOKS, SECURITY), meta (TESTING, PRIVACY, DOCUMENTATION).
- Sistema de items como única fuente de verdad (`docs/planning/items/`) con render determinista (`scripts/render_planning.py`).
- Items iniciales: FEATURE-000 (andamiaje) y FEATURE-001..007 derivadas del roadmap de ANALYSIS.md, con planes de desarrollo y criterios de aceptación.
- Infraestructura: docker-compose (prefijo `maira-`), Dockerfiles multi-stage, CI de GitHub Actions, Makefile, pre-commit, MkDocs Material, .editorconfig, .gitattributes.
- Skills de Claude adaptadas al stack y agentes SDD con temática The Walking Dead ("Consejo de Alexandria SDD"): Rick, Hershel, Deanna, Eugene, Daryl y Milton.
- Ficheros raíz: README, CLAUDE.md, AGENTS.md, CONTRIBUTING, SECURITY, LICENSE (AGPL-3.0).

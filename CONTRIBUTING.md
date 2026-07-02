# Guía de contribución

Gracias por querer ayudar a que las protectoras pequeñas tengan mejor tecnología. 🐾

## Flujo de trabajo (gitflow sin PRs internos)

- `main` — producción. Solo llega código mergeado desde `develop` con CI verde. Protegida.
- `develop` — integración. Aquí se trabaja a diario.
- Ramas de trabajo: `feat/<descripcion-corta>`, `fix/<...>`, `chore/<...>` (sin espacios ni acentos) → merge a `develop`.
- Contribuciones externas: fork + Pull Request contra `develop` (título descriptivo, qué/por qué/cómo probarlo).

## TDD obligatorio

1. Escribe el test que falla (los items de `docs/planning/items/` traen las "Tareas TDD" ordenadas).
2. Implementa lo mínimo para ponerlo en verde.
3. Refactoriza con la red de tests.

Cobertura mínima en CI: **70% backend**. Un fix de bug siempre incluye su test de regresión.

## Estilo y herramientas

| Capa | Herramientas | Regla |
|---|---|---|
| Python | `ruff` (lint+format+isort), `mypy` | Type hints en funciones públicas, docstrings Google, excepciones custom con mensajes en español |
| TypeScript | `eslint`, `prettier`, `tsc --noEmit` | `strict: true`, no `any` sin justificar, Server Components por defecto |
| Docs | MkDocs | Español, lenguaje llano en `docs/product/` |

Instala los hooks: `pip install pre-commit && pre-commit install`.

## Commits — Conventional Commits en español

```
feat: añadir generación de ficha con IA
fix: corregir validación de email en signup
docs: actualizar runbook de despliegue
refactor|test|chore|perf|ci: ...
```

La plantilla está configurada (`git config commit.template .github/commit-message-template.txt`). Referencia items con `Refs: FEATURE-003`.

## Planificación

- La fuente de verdad son los items de `docs/planning/items/` (copia `_TEMPLATE.md`, consulta `INDEX.md` para no duplicar).
- BACKLOG/ROADMAP **no se editan a mano**: `make render-planning` (o `python scripts/render_planning.py`). CI lo verifica.

## Lo innegociable

- **Nada de secretos en el repo** (es público). `.env` jamás se commitea.
- **Accesibilidad**: no se mergea UI que rompa la navegación por teclado o baje Lighthouse A11y de 90.
- **Ética de IA**: disclaimers intactos; el triaje nunca "diagnostica". Si tu cambio toca prompts, corre el set de validación.
- **Coste 0€**: no introduzcas dependencias de servicios de pago.

---
description: Referencia de testing Maira — pytest, respx, Vitest, Playwright, axe
---

# Skill: Testing

Docs: `docs/meta/TESTING.md`. TDD obligatorio: el test se escribe ANTES. Cobertura backend ≥ 70% (CI bloquea por debajo).

## Backend — pytest

```python
# tests/services/test_triage.py
async def test_triaje_con_palabra_veneno_devuelve_alta(triage_service, respx_mock):
    """Regla dura: emergencia vital fuerza ALTA aunque el LLM diga baja."""
    respx_mock.post(GROQ_URL).respond(json=respuesta_llm(nivel="baja"))
    resultado = await triage_service.clasificar(descripcion="creo que ha comido veneno", ...)
    assert resultado.nivel_urgencia == NivelUrgencia.ALTA
```

- Nombres: `test_<funcionalidad>_<escenario>_<esperado>`; arrange-act-assert; docstring de una línea si el caso no es obvio.
- Async: `pytest-asyncio` en modo auto; fixtures async para sesión de BD con rollback por test.
- **APIs externas SIEMPRE con `respx`** (Groq, Gemini, HF, Qdrant): cero llamadas reales en tests (cuotas free + determinismo). Cubrir también 429/500/timeout del proveedor.
- Endpoints: `httpx.AsyncClient(app=app)`; verificar status + body + efecto en BD.
- RLS/multi-tenant: fixture con dos protectoras; los tests de aislamiento no se tocan.
- Migraciones: test que hace `upgrade head` + `downgrade base` en BD efímera.

## Frontend — Vitest + Testing Library

- Queries por rol y label (`getByRole("button", {name: /guardar/i})`) — accesibilidad verificada de rebote.
- API mockeada con MSW; nunca fetch real.
- Qué testear: hooks con lógica, schemas Zod, componentes con estados (loading/error/vacío). Qué NO: estilos, shadcn sin modificar.

## E2E — Playwright

- 4 flujos: auth, alta+ficha (LLM mockeado por route interception), registro diario, triaje.
- Selectores por rol/testid, nunca CSS frágil. `npx playwright test` local; en CI solo `main`.

## Accesibilidad

- axe-playwright en cada pantalla clave: violación crítica/seria = rojo.
- `pa11y-ci` contra el build. Lighthouse A11y > 90 pre-release (FEATURE-007).

## IA — set de validación de triaje

`backend/tests/fixtures/triaje_validacion.json`: ≥ 20 casos etiquetados (esperado: baja/media/alta). Test paramétrico que corre el pipeline con mocks del CV y el LLM real SOLO en ejecución manual pre-release. **Regla bloqueante: 0 falsos negativos en casos ALTA.** Todo cambio de prompt corre el set.

## Comandos

```bash
cd backend && pytest --cov=src --cov-report=term-missing   # make test-backend
cd backend && pytest tests/services/test_triage.py -k veneno -x
cd frontend && npm run test                                # make test-frontend
npx playwright test --ui                                   # E2E con inspector
```

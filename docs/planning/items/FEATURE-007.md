---
id: FEATURE-007
tipo: feature
titulo: "Pulido final: accesibilidad, pentest, piloto real y despliegue estable"
estado: listo
prioridad: alta
hito: "0.6"
duplicado_de: null
creado: 2026-07-02
actualizado: 2026-07-02
---

# FEATURE-007 — Pulido final: A11y, pentest, piloto y release

## Descripción

Cerrar el MVP con calidad demostrable ante el tribunal: auditoría de accesibilidad (Lighthouse > 90), pentest básico sin vulnerabilidades críticas, onboarding de la protectora piloto real con sesiones de feedback, corrección de bugs críticos y despliegue final estable.

## Contexto / impacto

Semanas 9-10 de `ANALYSIS.md` y su Definition of Done del MVP: 1 protectora real usándolo 2 semanas, ≥5 animales con ficha, ≥10 registros, ≥3 triajes con feedback. Es lo que convierte el TFM en un caso validado, no solo código.

## Plan de desarrollo

### Documentación a consultar
- `ANALYSIS.md` §15 (A11y) y §16 (seguridad) · `docs/meta/TESTING.md` · `docs/operations/RUNBOOKS.md`

### Seguridad
- Pentest con OWASP ZAP (baseline scan) contra staging; triaje de hallazgos y corrección de críticos/altos.
- Revisión de headers (CSP, HSTS, X-Frame-Options) y de rate limiting en producción.

### Modelo de datos
- Sin cambios (solo fixes que surjan).

### API
- Sin endpoints nuevos (hardening y fixes).

### Frontend
- Auditoría axe-core + pa11y integrada en CI; corrección de hallazgos.
- Revisión manual con NVDA + navegación por teclado de los 4 flujos críticos.
- Tipografía base ≥ 18px escalable a 200%; foco visible en todo.

### Tareas TDD
1. Tests axe automatizados por pantalla clave → corregir hasta 0 violaciones críticas.
2. Smoke tests post-deploy (health, login, alta, triaje con mock) → pipeline.
3. Tests de regresión para cada bug crítico reportado por la piloto.

### Dependencias
- FEATURE-001 a FEATURE-006.

## Criterios de aceptación / Casuística a cubrir

- [ ] Lighthouse A11y > 90 en dashboard, alta de animal, ficha IA y triaje.
- [ ] 0 vulnerabilidades críticas o altas abiertas tras OWASP ZAP.
- [ ] Protectora piloto onboardeada; ≥ 2 sesiones de feedback documentadas.
- [ ] DoD del MVP de ANALYSIS.md cumplido (5 animales, 10 registros, 3 triajes reales).
- [ ] Demo reproducible ante el tribunal: URL pública operativa + `docker compose --profile app up` como plan B ensayado.
- [ ] README y docs listos para evaluación externa (un juez entiende el proyecto en 5 minutos).

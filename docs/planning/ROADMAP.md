# Roadmap

> ⚠️ **Vista renderizada** desde `items/` por `make render-planning`. Las tablas y porcentajes los pone el script; la narrativa de cada hito la mantiene Milton. Un item entra aquí solo cuando se le asigna hito.

## Narrativa de los hitos del MVP

| Hito | Nombre | Objetivo | Criterio de salida |
|---|---|---|---|
| 0.1 | Andamiaje | Esqueleto end-to-end desplegado en free tiers | `/health` 200 en Render, home en Vercel, compose funcional |
| 0.2 | Puerta de entrada | Auth con magic link y perfil de protectora | Signup→login→dashboard vacío, RLS verificada |
| 0.3 | El animal y su ficha | Alta de animal + ficha de adopción con IA | Alta < 2 min, ficha IA < 8s con regeneración |
| 0.4 | Salud diaria | Registro en 30s + alertas de anomalías | 4 reglas de alerta verificadas con tests |
| 0.5 | Triaje | Clasificación de urgencia con foto + RAG | 0 falsos negativos ALTA en set de validación |
| 0.6 | MVP presentable | Dashboard, export, A11y, pentest, piloto real | DoD de ANALYSIS.md + demo ensayada ante tribunal |

Después del MVP: fase 2 (multi-protectora, i18n) y fase 3 (Elpis) — ver [`ANALYSIS.md` §7](../../ANALYSIS.md) y el archivo de ideas.

## Estado por hito

<!-- RENDER:START -->
| Hito | Items | Hechos | Progreso |
|---|---|---|---|
| **0.1** | 1 | 0 | 0% |
| **0.2** | 1 | 0 | 0% |
| **0.3** | 2 | 0 | 0% |
| **0.4** | 1 | 0 | 0% |
| **0.5** | 1 | 0 | 0% |
| **0.6** | 2 | 0 | 0% |

### Hito 0.1

- [FEATURE-000](items/FEATURE-000.md) — Inicialización y andamiaje del proyecto · 🟢 Listo para desarrollo

### Hito 0.2

- [FEATURE-001](items/FEATURE-001.md) — Registro y acceso de la protectora (auth + perfil) · 🟢 Listo para desarrollo

### Hito 0.3

- [FEATURE-002](items/FEATURE-002.md) — Alta de animal con fotos · 🟢 Listo para desarrollo
- [FEATURE-003](items/FEATURE-003.md) — Generación de ficha de adopción con IA · 🟢 Listo para desarrollo

### Hito 0.4

- [FEATURE-004](items/FEATURE-004.md) — Registro diario de salud y detección de anomalías · 🟢 Listo para desarrollo

### Hito 0.5

- [FEATURE-005](items/FEATURE-005.md) — Triaje veterinario con IA (foto + descripción) · 🟢 Listo para desarrollo

### Hito 0.6

- [FEATURE-006](items/FEATURE-006.md) — Panel de control y exportación de datos · 🟢 Listo para desarrollo
- [FEATURE-007](items/FEATURE-007.md) — Pulido final: accesibilidad, pentest, piloto real y despliegue estable · 🟢 Listo para desarrollo
<!-- RENDER:END -->

---
id: IMPROVEMENT-001
tipo: improvement
titulo: "Actualizar Next.js para resolver los avisos de seguridad de Dependabot"
estado: recibido
prioridad: alta
hito: null
duplicado_de: null
creado: 2026-07-03
actualizado: 2026-07-03
---

# IMPROVEMENT-001 — Actualizar Next.js (avisos de seguridad)

## Descripción

Dependabot reporta 16 avisos en el repo: 14 son del propio Next.js 14.2.35 (5 high, 7 medium, 2 low) y 2 transitivos (glob, postcss). Los fixes de Next viven en la rama 15/16, que la regla "ignorar majors" (TFM) bloquea a propósito. Hay que decidir y ejecutar la subida controlada de versión.

## Contexto / impacto

El DoD del MVP exige 0 vulnerabilidades críticas y el tribunal puede mirar la pestaña Security del repo público. La subida a Next 15 toca React 19 en App Router: hacerla en frío, con la suite en verde, **no** en mitad de una feature. Evaluar el salto mínimo que limpie los avisos high.

## Plan de desarrollo

_(pendiente de promover — lo rellenará Deanna)_

## Criterios de aceptación / Casuística a cubrir

- [ ] 0 avisos high de Dependabot en la rama por defecto.
- [ ] Suite frontend en verde y build de producción funcionando tras la subida.
- [ ] Demo en Vercel verificada tras el deploy.

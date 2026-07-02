---
id: TIPO-NNN
tipo: feature            # feature | bug | improvement
titulo: "Título corto en lenguaje de negocio"
estado: recibido         # recibido → analisis → diseno → listo → desarrollo → bloqueado → hecho → descartado
prioridad: media         # alta | media | baja
hito: null               # se asigna al promover (ej. "0.2"); null = no aparece en el roadmap
duplicado_de: null
creado: AAAA-MM-DD
actualizado: AAAA-MM-DD
---

# TIPO-NNN — Título

<!-- PLANO 1: CAPTURA (lo rellena quien reporta: analista / pasarela ChatGPT) -->

## Descripción

Qué se pide, en lenguaje de negocio, sin jerga técnica.

## Contexto / impacto

A quién afecta (voluntaria, coordinadora, veterinario), en qué momento, y qué pasa si no se hace.
Semilla de criterios en términos de negocio si se conocen.

<!-- PLANO 2: PLAN TÉCNICO (lo rellena Deanna al promover el item) -->

## Plan de desarrollo

### Documentación a consultar
- `docs/technical/...`

### Seguridad
- Consideraciones de seguridad específicas de este item.

### Modelo de datos
- Tablas/campos nuevos o modificados.

### API
- Endpoints nuevos o modificados.

### Frontend
- Pantallas/componentes afectados.

### Tareas TDD
1. Test que falla → implementación → refactor. Lista ordenada.

### Dependencias
- Items que deben estar `hecho` antes.

## Criterios de aceptación / Casuística a cubrir

- [ ] Toda la casuística funcional y de seguridad, no solo el happy path.

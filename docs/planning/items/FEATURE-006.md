---
id: FEATURE-006
tipo: feature
titulo: "Panel de control y exportación de datos"
estado: listo
prioridad: media
hito: "0.6"
duplicado_de: null
creado: 2026-07-02
actualizado: 2026-07-02
---

# FEATURE-006 — Panel de control y exportación de datos

## Descripción

La coordinadora ve de un vistazo al entrar: total de animales, en tratamiento, disponibles para adoptar y triajes pendientes, más los últimos registros del día. Puede filtrar/buscar animales y exportar todos los datos a CSV con un botón (sin lock-in: los datos son de la protectora).

## Contexto / impacto

Épica 5 de `ANALYSIS.md` (US-5.1 a US-5.3). Resuelve la frustración de Marta: "no tenemos visión de conjunto". La exportación además cumple el valor "sin lock-in" y la portabilidad RGPD.

## Plan de desarrollo

### Documentación a consultar
- `docs/technical/API_CONTRACTS.md` (dashboard, export) · `docs/technical/DESIGN.md` (tarjetas, dataviz)

### Seguridad
- Export limitado a la protectora propia (RLS) y a roles `admin`/`editor`.
- CSV con escaping correcto (inyección de fórmulas en Excel: prefijar `'` a valores que empiezan por `=`, `+`, `-`, `@`).

### Modelo de datos
- Sin tablas nuevas; queries agregadas con índices existentes.

### API
- `GET /api/v1/dashboard/resumen` · `GET /api/v1/export/animales.csv` · `GET /api/v1/export/registros.csv`

### Frontend
- Dashboard con saludo personalizado, 4 tarjetas de métricas, últimos registros y accesos rápidos.
- Filtros combinables en la lista (especie + estado + búsqueda por nombre).

### Tareas TDD
1. Test resumen agrega correctamente con dataset seed conocido → endpoint dashboard.
2. Test resumen excluye animales de otras protectoras → RLS.
3. Test CSV: separadores, UTF-8 con BOM (Excel español), escaping de fórmulas → export.
4. Test export respeta filtros de rol → autorización.
5. Test filtros combinados en listado → query params.

### Dependencias
- FEATURE-002 · FEATURE-004 · FEATURE-005 (datos que agregar).

## Criterios de aceptación / Casuística a cubrir

- [ ] Dashboard carga en < 2s con 50 animales y 1.000 registros (seed).
- [ ] Métricas cuadran exactamente con los datos (verificado con seed conocido).
- [ ] CSV abre bien en Excel español (acentos, comas decimales) y en LibreOffice.
- [ ] Celda que empieza por `=` exportada de forma inerte (sin ejecución de fórmula).
- [ ] Protectora sin animales → dashboard con estado vacío amable + CTA "Da de alta tu primer animal".
- [ ] Rol `lectura` puede ver el dashboard pero no exportar.

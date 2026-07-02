---
id: FEATURE-004
tipo: feature
titulo: "Registro diario de salud y detección de anomalías"
estado: listo
prioridad: alta
hito: "0.4"
duplicado_de: null
creado: 2026-07-02
actualizado: 2026-07-02
---

# FEATURE-004 — Registro diario de salud y detección de anomalías

## Descripción

La voluntaria registra el estado diario de cada animal en menos de 30 segundos (peso, apetito 1-5, ánimo 1-5, notas y foto opcionales), ve la evolución en una línea de tiempo con gráficos, y recibe avisos automáticos si algo pinta mal ("lleva 3 días con apetito bajo").

## Contexto / impacto

Épica 3 de `ANALYSIS.md` (US-3.1 a US-3.4) y §13 Componente 3. Sustituye la libreta/Excel: cuando cambia la voluntaria de turno, la historia del animal no se pierde.

## Plan de desarrollo

### Documentación a consultar
- `docs/technical/DATA_MODEL.md` (registro_diario, UNIQUE(animal_id, fecha))
- `ANALYSIS.md` §13 (reglas de anomalías)

### Seguridad
- RLS por protectora en `registro_diario`.
- Solo roles `admin`/`editor` crean registros; `lectura` solo consulta.

### Modelo de datos
- `registro_diario` con UNIQUE(animal_id, fecha) e índice `(animal_id, fecha DESC)`.

### API
- `GET /api/v1/animales/{id}/registros?limit=30` · `POST /api/v1/animales/{id}/registros` · `PATCH /api/v1/registros/{id}`

### Frontend
- Formulario ultrarrápido: escalas 1-5 como botones grandes tocables (móvil), peso numérico, guardar en 1 tap.
- Timeline con gráficos de peso/apetito/ánimo (accesibles: tabla de datos alternativa).
- Banner de alertas en el detalle del animal y en el dashboard.

### Tareas TDD
1. Test crear registro válido / duplicado mismo día (conflicto claro) → endpoint POST.
2. Test regla "apetito < 2 durante 3 días" dispara alerta → motor de reglas.
3. Test regla "peso -10% en 30 días" → motor de reglas.
4. Test regla "sin registro en 3 días" → recordatorio.
5. Test "delta de ánimo > 3" → alerta.
6. Test timeline pagina y ordena DESC → endpoint GET.
7. E2E: registro completo en < 30s de interacciones desde la lista.

### Dependencias
- FEATURE-002.

## Criterios de aceptación / Casuística a cubrir

- [ ] Registro diario completo en < 30 segundos desde la lista de animales.
- [ ] Segundo registro el mismo día → ofrece editar el existente, no duplica.
- [ ] Las 4 reglas de anomalía disparan con datasets sintéticos y NO disparan con datos sanos (sin falsos positivos triviales).
- [ ] Gráficos legibles en móvil y con datos irregulares (huecos de días sin registro).
- [ ] Alternativa textual/tabla para lectores de pantalla en cada gráfico.
- [ ] Registro sin peso (opcional) no rompe el gráfico de evolución.

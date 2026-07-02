---
id: FEATURE-005
tipo: feature
titulo: "Triaje veterinario con IA (foto + descripción)"
estado: listo
prioridad: alta
hito: "0.5"
duplicado_de: null
creado: 2026-07-02
actualizado: 2026-07-02
---

# FEATURE-005 — Triaje veterinario con IA

## Descripción

La voluntaria sube una foto de un síntoma y lo describe; en menos de 30 segundos recibe una clasificación de urgencia (BAJA: cita esta semana · MEDIA: 24-48h · ALTA: clínica YA) con justificación en lenguaje llano y qué observar antes de la cita. **Nunca es un diagnóstico** y la app lo dice siempre.

## Contexto / impacto

Épica 4 de `ANALYSIS.md` (US-4.1 a US-4.5) y §13 Componente 2. Es la capa con mayor peso ético del proyecto: un falso negativo (urgencia alta clasificada como baja) puede causar sufrimiento animal. Riesgo 4 de ANALYSIS.md.

## Plan de desarrollo

### Documentación a consultar
- `ANALYSIS.md` §13 Componente 2 (pipeline CV + RAG + LLM, prompt de triaje)
- `docs/operations/SECURITY.md` (LLM security) · `docs/meta/PRIVACY.md` (art. 22 RGPD)

### Seguridad
- Prompt conservador: ante la duda, clasificar el nivel MÁS alto; envenenamiento/trauma/parto → siempre ALTA.
- Output en JSON estricto validado con Pydantic; si no parsea → reintento y, si falla, error honesto (nunca inventar nivel).
- Disclaimer permanente e ineludible en UI y en la respuesta de la API.
- Log completo de cada triaje para auditoría del veterinario colaborador.

### Modelo de datos
- `triaje_vet` completa (categoría, nivel_urgencia, justificacion_ia, sugerencias_observacion[], revisado_por_vete).
- Índice `(animal_id, created_at DESC)`.

### API
- `POST /api/v1/animales/{id}/triaje` (multipart: foto + descripción + categoría)
- `GET /api/v1/animales/{id}/triajes` · `PATCH /api/v1/triajes/{id}` (marcar revisado).

### Frontend
- Pantalla "Síntoma nuevo": foto grande arrastrable + descripción + categoría pre-listada.
- Resultado en card con badge de color + icono + TEXTO del nivel (no solo color), justificación, sugerencias y disclaimer.
- Historial de triajes en el detalle del animal.

### Tareas TDD
1. Test pipeline con mocks: foto → features CV → chunks RAG → prompt → JSON válido.
2. Test parsing de output: JSON malformado → reintento → error controlado.
3. Test reglas duras: descripción con "veneno"/"atropellado"/"parto" → ALTA siempre, incluso si el LLM dice otra cosa.
4. Test RAG: consulta recupera chunks relevantes de las guías indexadas (fixture con corpus mínimo).
5. Test respuesta incluye siempre el disclaimer → contrato de API.
6. Test triaje persiste en el historial del animal → persistencia.
7. E2E: flujo completo triaje con foto en < 30s (mock del LLM).

### Dependencias
- FEATURE-002 · FEATURE-003 (reutiliza la capa de abstracción LLM).

## Criterios de aceptación / Casuística a cubrir

- [ ] Respuesta en < 15s (p90); indicador de progreso mientras tanto.
- [ ] Set de validación de 20 casos sintéticos revisados: 0 falsos negativos en los casos ALTA.
- [ ] Palabras clave de emergencia vital → ALTA garantizada por regla dura (no depende del LLM).
- [ ] El texto JAMÁS contiene "diagnóstico" ni nombra enfermedad como certeza (validador de output).
- [ ] Disclaimer visible en resultado, historial y export.
- [ ] Nivel de urgencia distinguible sin ver color (texto + icono).
- [ ] LLM/CV caídos → mensaje honesto: "no puedo analizarlo ahora; si es grave, acude al veterinario".
- [ ] Cada triaje queda en el historial con estado "pendiente de revisión / visto por vete".

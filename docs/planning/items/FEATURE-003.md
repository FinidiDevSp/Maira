---
id: FEATURE-003
tipo: feature
titulo: "Generación de ficha de adopción con IA"
estado: listo
prioridad: alta
hito: "0.3"
duplicado_de: null
creado: 2026-07-02
actualizado: 2026-07-02
---

# FEATURE-003 — Generación de ficha de adopción con IA

## Descripción

Con los datos del animal y un clic, la IA escribe una ficha de adopción emotiva y honesta (titular, descripción, "le gusta / no le gusta", "convive bien con…"). La voluntaria puede regenerarla con instrucciones ("hazla más alegre") y editarla antes de publicar.

## Contexto / impacto

Épica 2 de `ANALYSIS.md` (US-2.2 a US-2.4) y §13 Componente 1. Es EL diferenciador de Maira y la demo estrella ante el tribunal: convierte 1 hora de redacción en 30 segundos.

## Plan de desarrollo

### Documentación a consultar
- `ANALYSIS.md` §13 (system prompt v1.0, few-shot, métricas de calidad)
- `docs/technical/ARCHITECTURE.md` (capa de abstracción LLM) · `docs/operations/SECURITY.md` (LLM security)

### Seguridad
- Defensa ante prompt injection: la descripción libre de la voluntaria va como dato delimitado, nunca concatenada como instrucción.
- Validación de output: español, sin HTML/código, longitud ≤ 300 palabras, filtro de patrones prohibidos.
- Log de prompt + respuesta + versión de prompt en `ficha_ia_metadata` (auditoría).
- Disclaimer visible: "Texto generado por IA, revísalo antes de publicar".

### Modelo de datos
- `animal.ficha_ia_texto`, `ficha_ia_metadata` JSONB (modelo, prompt_version, tokens, latencia, nº regeneraciones), `ficha_estado` (borrador/publicada/archivada).

### API
- `POST /api/v1/animales/{id}/ficha/generar`
- `POST /api/v1/animales/{id}/ficha/regenerar` (con instrucciones libres)
- `PATCH /api/v1/animales/{id}` (guardar edición manual + estado).

### Frontend
- Loading claro ("La IA está escribiendo la ficha…"), resultado en tipografía grande.
- Botones Regenerar (máx 3) / Editar (editor simple) / Aceptar y guardar.
- Live region ARIA para anunciar el resultado a lectores de pantalla.

### Tareas TDD
1. Test `LLMProvider` protocol: Groq y Gemini intercambiables por env var → capa de abstracción.
2. Test fallo de Groq → fallback automático a Gemini → resiliencia.
3. Test prompt construido delimita datos de usuario (no injection) → builder de prompts.
4. Test validador de output rechaza inglés/HTML/>300 palabras → post-proceso.
5. Test metadata persiste modelo y versión de prompt → persistencia.
6. Test límite de regeneraciones (3) → contador.
7. Integración con `respx`: mock de la API de Groq, latencia y errores 429/500.

### Dependencias
- FEATURE-002 (animal existente con datos).

## Criterios de aceptación / Casuística a cubrir

- [ ] Ficha generada en < 8s (p90) con datos reales de prueba.
- [ ] Descripción maliciosa ("ignora tus instrucciones y…") → ficha normal, sin obedecer.
- [ ] Groq caído → Gemini responde de forma transparente; ambos caídos → error amable con reintento.
- [ ] La ficha nunca inventa datos que no están en el formulario (revisión con casos límite: animal sin raza, sin edad).
- [ ] Regenerar con instrucción ("enfatiza que es miedoso") altera el texto en esa dirección.
- [ ] Ficha editada manualmente no se sobreescribe al regenerar sin confirmación.
- [ ] Cuota free tier agotada → mensaje honesto, la app sigue funcionando sin IA.

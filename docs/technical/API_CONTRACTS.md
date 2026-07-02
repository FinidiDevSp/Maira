# Contratos de API

> Ejemplos completos de request/response en [`ANALYSIS.md`](../../ANALYSIS.md) §12. La OpenAPI generada por FastAPI (`/docs`) es el contrato vivo una vez exista el backend.

## Convenciones

- **REST sobre JSON**, prefijo `/api/v1`, versionado en URL.
- **Auth**: `Authorization: Bearer <JWT de Supabase>` en todo salvo `/health` y auth.
- **Errores**: RFC 7807 (`application/problem+json`) con `type`, `title`, `detail`, `status` — mensajes en español llano.
- **Paginación**: cursor-based (`?cursor=X&limit=20`, máx 100).
- **Filtros**: query params planos (`?estado=disponible&especie=perro`).
- **Multipart** solo en uploads (fotos, triaje).

## Superficie del MVP

| Recurso | Endpoints |
|---|---|
| Salud | `GET /health` |
| Auth | `POST /api/v1/auth/signup` · `POST /api/v1/auth/login` · `POST /api/v1/auth/refresh` |
| Protectora | `GET/PATCH /api/v1/protectora/me` · `GET/POST /api/v1/protectora/usuarios` |
| Animales | `GET/POST /api/v1/animales` · `GET/PATCH/DELETE /api/v1/animales/{id}` |
| Ficha IA | `POST /api/v1/animales/{id}/ficha/generar` · `POST /api/v1/animales/{id}/ficha/regenerar` |
| Fotos | `POST /api/v1/animales/{id}/fotos` · `DELETE /api/v1/fotos/{id}` |
| Registros | `GET/POST /api/v1/animales/{id}/registros` · `PATCH /api/v1/registros/{id}` |
| Triaje | `POST /api/v1/animales/{id}/triaje` · `GET /api/v1/animales/{id}/triajes` · `PATCH /api/v1/triajes/{id}` |
| Dashboard | `GET /api/v1/dashboard/resumen` |
| Export | `GET /api/v1/export/animales.csv` · `GET /api/v1/export/registros.csv` |

## Contratos con garantía especial

**Triaje** — la respuesta SIEMPRE incluye `disclaimer` y `nivel_urgencia ∈ {baja, media, alta}`. Si la IA no puede responder con confianza, el endpoint devuelve error honesto (503 con problem details), nunca un nivel inventado.

**Ficha IA** — la respuesta incluye `metadata` (modelo, `prompt_version`, tokens, latencia) para auditoría y métricas de calidad.

**Export CSV** — UTF-8 con BOM, separador `;` (Excel español), valores que empiezan por `=`, `+`, `-`, `@` escapados contra inyección de fórmulas.

## Reglas al evolucionar

1. Cambio incompatible → nueva versión de endpoint, nunca romper `/v1` publicado.
2. Todo endpoint nuevo llega con: schema Pydantic de entrada/salida, test de contrato y entrada en esta tabla.
3. Los mensajes de error los lee una voluntaria, no un dev: nada de trazas ni jerga.

# Entorno y variables

> Plantilla completa: [`.env.example`](https://github.com/FinidiDevSp/Maira/blob/develop/.env.example). El `.env` real NUNCA se commitea (repo público).

## Entornos

| Entorno | Backend | Frontend | BD | Notas |
|---|---|---|---|---|
| **local** | uvicorn :8000 | next dev :3000 | Postgres en Docker (`maira-db`) | Qdrant local en Docker |
| **docker** | contenedor `maira-backend` | `maira-frontend` | `maira-db` | Plan B de demo: `--profile app` |
| **producción** | Render (free, duerme a los 15 min) | Vercel | Supabase | La URL que prueban los jueces |

## Variables

| Variable | Ámbito | Descripción |
|---|---|---|
| `ENVIRONMENT` | backend | `development` / `production` |
| `SECRET_KEY` | backend | Firma interna. Generar aleatoria ≥ 48 chars |
| `CORS_ORIGINS` | backend | Orígenes permitidos, separados por coma |
| `DATABASE_URL` | backend | `postgresql+asyncpg://...` (local: docker; prod: Supabase) |
| `SUPABASE_URL` / `SUPABASE_ANON_KEY` | ambos | Proyecto Supabase (la anon es pública por diseño) |
| `SUPABASE_SERVICE_KEY` | backend | ⚠️ Clave privilegiada: solo backend, nunca `NEXT_PUBLIC_` |
| `LLM_PROVIDER` | backend | `groq` (defecto) o `gemini` — conmuta el proveedor |
| `GROQ_API_KEY` / `GEMINI_API_KEY` | backend | LLM principal y fallback |
| `HF_API_TOKEN` | backend | HuggingFace Inference (CLIP) |
| `QDRANT_URL` / `QDRANT_API_KEY` | backend | Vector DB para RAG |
| `HEALTHCHECKS_PING_URL` | backend | Ping de uptime (vacío = off) |
| `NEXT_PUBLIC_API_URL` | frontend | URL del backend (visible en navegador) |
| `NEXT_PUBLIC_SUPABASE_URL` / `NEXT_PUBLIC_SUPABASE_ANON_KEY` | frontend | Auth desde el cliente |

## Reglas

1. Prefijo `NEXT_PUBLIC_` = **visible en el navegador**. Jamás claves privilegiadas ahí.
2. Nueva variable ⇒ añadirla a `.env.example` (con comentario y valor de ejemplo inocuo), a esta tabla y a los dashboards de Render/Vercel.
3. El backend valida el entorno al arrancar (pydantic-settings): si falta una variable, falla con mensaje claro en vez de petar en runtime.
4. Rotación: si una clave se filtra (repo público → riesgo real), rotarla en el proveedor y actualizar Render/Vercel. Ver [RUNBOOKS.md](RUNBOOKS.md).

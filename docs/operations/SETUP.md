# Puesta en marcha

## Requisitos

- **Python 3.11+**, **Node 20+**, **Docker Desktop** y **git**.
- Windows: los comandos `make` requieren Git Bash o WSL. Debajo de cada `make` está el comando directo equivalente.

## Arranque rápido

`backend/` y `frontend/` ya existen (FEATURE-000). Funciona hoy:

```bash
# 1. Clonar y preparar entorno
git clone https://github.com/FinidiDevSp/Maira.git && cd Maira
copy .env.example .env        # (cp en bash) — rellena las claves

# 2. Documentación
pip install -r requirements-docs.txt
mkdocs serve -a localhost:8001          # make docs-serve

# 3. Regenerar planificación tras tocar items
python scripts/render_planning.py       # make render-planning

# 4. Infraestructura local (cuando exista el backend)
docker compose up -d                    # make up  → maira-db + maira-qdrant
```

## Arranque completo

```bash
# Backend (usa venv propio: python -m venv .venv && activarlo)
cd backend
pip install -e ".[dev]"
alembic upgrade head                    # make migrate (necesita DATABASE_URL y SECRET_KEY en el entorno o .env)
python scripts/seed.py                  # datos ficticios "Refugio Esperanza"
uvicorn src.main:app --reload           # http://localhost:8000/docs

# Frontend (otra terminal)
cd frontend
npm install
npm run dev                             # http://localhost:3000

# O todo con Docker (plan B de demo ante el tribunal)
docker compose --profile app up -d --build
```

## Cuentas necesarias (todas free tier — no metas tarjeta en ninguna)

| Servicio | Para qué | Variable(s) |
|---|---|---|
| [Supabase](https://supabase.com) | BD + Auth + Storage | `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_KEY`, `DATABASE_URL` |
| [Groq](https://console.groq.com) | LLM fichas/triaje | `GROQ_API_KEY` |
| [Google AI Studio](https://aistudio.google.com) | LLM fallback | `GEMINI_API_KEY` |
| [Qdrant Cloud](https://cloud.qdrant.io) | Vector DB (RAG) | `QDRANT_URL`, `QDRANT_API_KEY` |
| [HuggingFace](https://huggingface.co) | CV (CLIP) | `HF_API_TOKEN` |
| [Render](https://render.com) | Deploy backend | — (dashboard) |
| [Vercel](https://vercel.com) | Deploy frontend | — (dashboard) |
| [Healthchecks.io](https://healthchecks.io) | Uptime | `HEALTHCHECKS_PING_URL` |

## Calidad local

```bash
pip install pre-commit && pre-commit install   # hooks de commit
cd backend && pytest --cov=src                 # make test-backend
cd frontend && npm run test                    # make test-frontend
```

Ver [ENVIRONMENT.md](ENVIRONMENT.md) para el detalle de cada variable y [RUNBOOKS.md](RUNBOOKS.md) para incidencias.

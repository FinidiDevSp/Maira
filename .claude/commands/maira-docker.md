---
description: Referencia Docker Maira — compose con prefijo maira-, perfiles, demo local
---

# Skill: Docker

Rol de Docker en Maira (decisión D-008): **desarrollo local + plan B de demo ante el tribunal**. El deploy real es Render/Vercel/Supabase.

## Convenciones

- **Prefijo `maira-` en todo**: contenedores (`maira-backend`, `maira-frontend`, `maira-db`, `maira-qdrant`), volúmenes (`maira-db-data`…), red (`maira-net`). Un recurso sin prefijo es un error.
- Infra (db, qdrant) sin profile + con healthcheck; apps bajo `profiles: [app]`.
- Dockerfiles multi-stage en `docker/`: target `development` (hot-reload, volumen montado) y `production` (sin root, sin dev deps).

## Uso diario

```bash
docker compose up -d                        # solo infra: maira-db + maira-qdrant
cd backend && uvicorn src.main:app --reload # apps en el host (más rápido para iterar)
```

## Demo completa (plan B del día de la defensa)

```bash
docker compose --profile app up -d --build
docker compose exec maira-backend alembic upgrade head
docker compose exec maira-backend python scripts/seed.py
# → http://localhost:3000 con "Refugio Esperanza" cargado
```

Ensayar este flujo en frío antes de la defensa (criterio de FEATURE-007).

## Depuración

```bash
docker compose ps                          # estado + healthchecks
docker compose logs -f maira-backend       # logs de un servicio
docker compose exec maira-db psql -U maira -d maira    # make shell-db
docker compose down                        # parar (los volúmenes persisten)
docker compose down -v                     # ⚠️ borra también los datos locales
```

## Reglas

1. Cambios de dependencias → `--build` (el volumen de código no reinstala paquetes).
2. Nada de `latest` en imágenes base de Dockerfiles (pinear `python:3.11-slim`, `node:20-alpine`).
3. El target `production` no lleva usuario root ni dev-deps; verificarlo si se toca un Dockerfile.
4. `.env` se inyecta con `env_file`; jamás claves en el compose (va al repo público).

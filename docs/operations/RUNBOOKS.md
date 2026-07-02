# Runbooks

Procedimientos paso a paso para incidencias. Mantener actualizados: los usará "el yo estresado a las 23h antes de la defensa".

## RB-1 · El backend no responde

1. ¿Es el sleep de Render? Espera 15s y reintenta (cold start). Si responde, no es incidencia.
2. Panel de Render → Logs: busca stack trace del arranque (variable de entorno ausente es lo más común).
3. Healthchecks.io → ¿desde cuándo falla?
4. Si el deploy roto es reciente → **RB-2 (rollback)**.
5. Si es cuota de free tier agotada → mensaje en la UI ya lo contempla; documenta y espera al reset de cuota.

## RB-2 · Rollback de un deploy

- **Render:** Dashboard → servicio → *Deploys* → deploy anterior verde → *Rollback*.
- **Vercel:** Dashboard → *Deployments* → deployment anterior → *Promote to Production*.
- **Ambos son instantáneos** y no tocan la BD. Si la migración es el problema → RB-3.

## RB-3 · Migración de BD problemática

1. `cd backend && alembic downgrade -1` contra la `DATABASE_URL` afectada.
2. Si el downgrade falla: restaurar snapshot de Supabase (Dashboard → Database → Backups → Restore; retención free: 7 días).
3. Arreglar la migración en `develop` con test, nunca editar una migración ya aplicada en prod.

## RB-4 · Secreto filtrado (repo público — tomárselo en serio)

1. **Rotar la clave en el proveedor** (Supabase/Groq/Gemini/Qdrant/HF) inmediatamente. La rotación manda; borrar el commit es secundario.
2. Actualizar la variable en Render/Vercel y en el `.env` local.
3. Revisar logs del proveedor por uso no autorizado.
4. Limpiar el historial si procede (`git filter-repo`) y forzar push coordinado.
5. Anotar el incidente en el CHANGELOG interno y qué lo permitió (¿faltaba hook? ¿.gitignore?).

## RB-5 · La IA devuelve contenido inapropiado u erróneo

1. Capturar el caso completo: prompt, respuesta, modelo y `prompt_version` (están en los logs y en `ficha_ia_metadata`).
2. Ficha: botón regenerar/editar cubre a la usuaria. Triaje: recordar que la validación humana es obligatoria (disclaimer).
3. Añadir el caso al set de validación y ajustar prompt/filtros de salida.
4. Si es grave (contenido ofensivo, falso negativo de urgencia ALTA): crear `BUG-NNN` con prioridad alta y tratarlo antes que cualquier feature.

## RB-6 · Restaurar datos borrados por una usuaria

1. Soft delete (< 30 días): recuperar vía flag `deleted_at = NULL` (endpoint de restauración o SQL directo).
2. Borrado físico: snapshot de Supabase (ver RB-3, paso 2).

## RB-7 · Demo local de emergencia (día de la defensa)

```bash
docker compose --profile app up -d --build   # levanta todo con maira-*
cd backend && alembic upgrade head && python scripts/seed.py
# http://localhost:3000 con datos de la protectora ficticia
```

Si Docker falla: uvicorn + next dev directos (ver SETUP.md) contra la BD local o incluso SQLite de emergencia.

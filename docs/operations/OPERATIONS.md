# Operaciones

## Despliegue (todo free tier)

| Pieza | Dónde | Cómo se despliega |
|---|---|---|
| Backend | **Render** (web service, root `backend/`) | Auto-deploy al hacer push a `main`. Duerme tras 15 min sin tráfico (cold start 5-10s, avisado en la UI) |
| Frontend | **Vercel** (root `frontend/`) | Auto-deploy en `main`; preview deployment por rama |
| BD/Auth/Storage | **Supabase** | Migraciones con `alembic upgrade head` apuntando a la `DATABASE_URL` de prod |
| Vector DB | **Qdrant Cloud** | Colección `guias_vet` poblada por script de ingesta (FEATURE-005) |
| Docs | **GitHub Pages** (opcional) | `mkdocs gh-deploy` |

Flujo: trabajo en `develop` → merge a `main` = release → Render y Vercel despliegan solos → smoke test manual (health + login).

**URLs de producción:** frontend https://maira-opal.vercel.app · backend https://maira-backend-sj81.onrender.com (health: `/health`).

## Monitorización

- **Healthchecks.io**: ping a `GET /health` cada 5 min → email si el backend no responde > 1 min. Mantiene además el free tier de Render despierto en horario razonable.
- **Logs**: structlog JSON → stdout → panel de Render (retención 7 días).
- **Sin Sentry ni analítica de terceros** (D-010 y anti-métricas de ANALYSIS.md §20): las métricas de producto salen de queries SQL.

## Checklist del día de la defensa 🎓

La ejecutamos la víspera y 1h antes:

1. [ ] Abrir la URL pública e iniciar sesión (despierta a Render de paso).
2. [ ] Generar una ficha IA y un triaje de prueba (verifica Groq/HF/Qdrant vivos).
3. [ ] Verificar cuotas free tier (Groq, Supabase, Qdrant) con margen.
4. [ ] Plan B listo: `docker compose --profile app up -d --build` probado en el portátil de la defensa, con `.env` local válido y seed cargado.
5. [ ] Plan C: capturas/vídeo corto de los 3 flujos por si no hay red.
6. [ ] CI en verde y README impecable (el tribunal mirará el repo).

## Tareas periódicas

| Cuándo | Qué |
|---|---|
| Semanal | Revisar PRs de Dependabot; `git pull` de guías RAG si cambian |
| Semanal | Backup manual de Storage si hay fotos de la piloto (script futuro a R2) |
| Mensual | Revisar consumo de free tiers y métricas de calidad IA (tasa regeneración, falsos negativos) |
| Pre-release | pa11y + OWASP ZAP baseline (FEATURE-007) |

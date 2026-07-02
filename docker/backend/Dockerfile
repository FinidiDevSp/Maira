# Backend Maira (FastAPI) — multi-stage.
# development: hot-reload con volumen montado.
# production: imagen mínima sin root (usable en Render si se opta por deploy Docker).

FROM python:3.11-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1
WORKDIR /app

# --- development ---
FROM base AS development
COPY backend/pyproject.toml ./
RUN pip install -e ".[dev]" || pip install fastapi uvicorn[standard]
COPY backend/ ./
EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# --- production ---
FROM base AS production
RUN addgroup --system maira && adduser --system --ingroup maira maira
COPY backend/pyproject.toml ./
RUN pip install .
COPY backend/ ./
USER maira
EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

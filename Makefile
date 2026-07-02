# Maira — ciclo de desarrollo
# En Windows requiere Git Bash o WSL. Alternativa sin make: los comandos
# directos están documentados en docs/operations/SETUP.md.

.PHONY: help setup up down logs test test-backend test-frontend lint migrate seed \
        shell-db render-planning docs-serve docs-build clean

help: ## Lista los comandos disponibles
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

setup: ## Instala dependencias de backend y frontend
	cd backend && pip install -e ".[dev]"
	cd frontend && npm install
	pip install pre-commit && pre-commit install

up: ## Levanta infraestructura local (db + qdrant)
	docker compose up -d maira-db maira-qdrant

up-all: ## Levanta todo (infra + apps) — plan B de demo
	docker compose --profile app up -d --build

down: ## Para todos los contenedores
	docker compose --profile app down

logs: ## Muestra logs de los contenedores
	docker compose logs -f --tail=100

test: test-backend test-frontend ## Todos los tests

test-backend: ## Tests backend con cobertura
	cd backend && pytest --cov=src --cov-report=term-missing

test-frontend: ## Tests frontend
	cd frontend && npm run test

lint: ## Linting de todo el stack
	cd backend && ruff check . && ruff format --check . && mypy src
	cd frontend && npm run lint

migrate: ## Aplica migraciones Alembic
	cd backend && alembic upgrade head

seed: ## Carga datos de prueba (protectora ficticia + animales)
	cd backend && python scripts/seed.py

shell-db: ## Abre psql contra la BD local
	docker compose exec maira-db psql -U maira -d maira

render-planning: ## Regenera BACKLOG/ROADMAP/PRODUCT_CONTEXT desde los items
	python scripts/render_planning.py

docs-serve: ## Sirve la documentación en http://localhost:8001
	mkdocs serve -a localhost:8001

docs-build: ## Compila el sitio de documentación
	mkdocs build

clean: ## Limpia artefactos generados
	rm -rf site/ backend/htmlcov backend/.pytest_cache backend/.ruff_cache backend/.mypy_cache

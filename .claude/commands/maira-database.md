---
description: Referencia de base de datos Maira — SQLAlchemy 2.0, Alembic, RLS de Supabase
---

# Skill: Base de datos

Docs: `docs/technical/DATA_MODEL.md`. Postgres (Supabase en prod, `maira-db` Docker en local).

## Modelos SQLAlchemy 2.0

```python
class Animal(Base):
    __tablename__ = "animal"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, server_default=text("gen_random_uuid()"))
    protectora_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("protectora.id"), index=True)
    especie: Mapped[Especie]                      # Enum de dominio en español
    deleted_at: Mapped[datetime | None]           # soft delete (30 días recuperable)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
```

Reglas: estilo declarativo 2.0 con `Mapped[...]`; UUID PK en todo; TIMESTAMPTZ; enums nativos de Postgres; soft delete solo donde el modelo de datos lo indica (animal).

## Migraciones (Alembic)

1. `alembic revision --autogenerate -m "añadir tabla triaje_vet"` → **revisar SIEMPRE el fichero generado** (autogenerate no ve RLS, triggers ni índices trigram).
2. `downgrade()` real y probado (`upgrade head` + `downgrade -1` en el test de migraciones).
3. Las políticas RLS, extensiones (`pg_trgm`) e índices especiales van como `op.execute(...)` en la migración — la BD es la fuente de verdad, no el dashboard de Supabase.
4. Nunca editar una migración ya aplicada en producción; se corrige con una nueva.

## RLS (innegociable)

Toda tabla con `protectora_id` (directo o vía JOIN a animal) lleva política:

```sql
ALTER TABLE animal ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_animal ON animal FOR ALL
  USING (protectora_id IN (SELECT protectora_id FROM usuario WHERE id = auth.uid()));
```

- El backend con `SUPABASE_SERVICE_KEY`/conexión directa **salta la RLS**: por eso la autorización en FastAPI (roles + filtro por protectora del usuario) es obligatoria en cada query de servicio.
- Test de aislamiento multi-tenant por tabla nueva: usuaria A no ve datos de B. Intocables en la suite.

## Índices y rendimiento

- Declarados en el modelo/migración: `animal(protectora_id, estado)`, `registro_diario(animal_id, fecha DESC)`, `triaje_vet(animal_id, created_at DESC)`, trigram en `animal(nombre)`.
- `UNIQUE(animal_id, fecha)` en registro_diario → capturar `IntegrityError` y devolver conflicto amable ("ya hay registro hoy, ¿quieres editarlo?").
- Listados SIEMPRE paginados (cursor); nunca `SELECT *` sin límite.

## Seed y datos de prueba

`backend/scripts/seed.py`: protectora "Refugio Esperanza" + 5 animales + 20 registros + 3 triajes. Determinista (misma semilla), sin datos reales de nadie (repo público).

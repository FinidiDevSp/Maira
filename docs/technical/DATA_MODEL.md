# Modelo de datos

> Esquema completo con tipos en [`ANALYSIS.md`](../../ANALYSIS.md) §11. Aquí: visión operativa y reglas.

## Entidades

```
protectora 1─N usuario
protectora 1─N animal 1─N foto_animal
                animal 1─N registro_diario   (UNIQUE animal_id + fecha)
                animal 1─N triaje_vet
```

| Tabla | Qué guarda | Claves de diseño |
|---|---|---|
| `protectora` | Datos de la asociación | UUID PK; `descripcion_publica` para futura web pública |
| `usuario` | Perfil vinculado a `auth.users` de Supabase | `rol`: admin / editor / lectura |
| `animal` | El animal y su ficha IA | Enums de especie/sexo/tamaño/estado; `ficha_ia_metadata` JSONB (modelo, prompt_version, regeneraciones); soft delete |
| `foto_animal` | Fotos en Supabase Storage | `es_principal`, `orden`; máx 8 por animal |
| `registro_diario` | Peso, apetito (1-5), ánimo (1-5), notas | `UNIQUE(animal_id, fecha)` — un registro por día |
| `triaje_vet` | Foto + descripción + nivel urgencia + justificación IA | `revisado_por_vete` para el flujo con el veterinario |
| `evento_salud` | Vacunas, visitas… | **Futuro, no MVP** |

## Estados del animal

`en_acogida → disponible → reservado → adoptado`, con desvíos a `en_tratamiento`, `devuelto`, `fallecido`. Las transiciones se validan en el servicio, no en la UI.

## Índices

- `animal(protectora_id, estado)` — listados filtrados.
- `registro_diario(animal_id, fecha DESC)` — timeline.
- `triaje_vet(animal_id, created_at DESC)` — historial clínico.
- `animal(nombre)` con trigram (`pg_trgm`) — búsqueda fuzzy.

## Row Level Security

**Toda tabla con `protectora_id` (directo o vía animal) lleva política RLS.** Patrón:

```sql
CREATE POLICY "usuarios ven su protectora" ON animal
  FOR ALL USING (
    protectora_id IN (SELECT protectora_id FROM usuario WHERE id = auth.uid())
  );
```

La RLS es la última línea de defensa; la autorización por rol se aplica además en FastAPI. **Ningún test de RLS puede quitarse de la suite** (repo público + datos reales de la piloto).

## Reglas de oro

1. UUID como PK en todo; `created_at`/`updated_at` TIMESTAMPTZ en todo.
2. Migraciones **solo** con Alembic; cada una reversible (`downgrade` real).
3. Soft delete en `animal` (recuperable 30 días); el resto, borrado en cascada al ejercer derecho al olvido (ver [PRIVACY](../meta/PRIVACY.md)).
4. Enums de dominio en español (son la lengua del producto).

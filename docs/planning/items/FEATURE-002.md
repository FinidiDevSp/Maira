---
id: FEATURE-002
tipo: feature
titulo: "Alta de animal con fotos"
estado: listo
prioridad: alta
hito: "0.3"
duplicado_de: null
creado: 2026-07-02
actualizado: 2026-07-02
---

# FEATURE-002 — Alta de animal con fotos

## Descripción

La voluntaria da de alta un animal en menos de 2 minutos: una sola pantalla con foto (arrastrar o cámara), nombre, especie, raza, edad estimada, sexo, tamaño y una descripción libre de un párrafo.

## Contexto / impacto

Épica 2 de `ANALYSIS.md` (US-2.1, US-2.5). Es el dato base de todo lo demás: ficha IA, registro diario y triaje cuelgan del animal. La voluntaria tiene 2-3h/día para la protectora — cada minuto de formulario cuenta.

## Plan de desarrollo

### Documentación a consultar
- `docs/technical/DATA_MODEL.md` (animal, foto_animal) · `docs/technical/API_CONTRACTS.md`
- `docs/operations/SECURITY.md` (uploads)

### Seguridad
- Upload: validar tipo MIME real (no extensión), límite 5MB, strip de metadatos EXIF (geolocalización).
- Fotos en Supabase Storage con URLs firmadas y RLS por protectora.
- Soft delete (recuperable 30 días) — nunca borrado físico directo.

### Modelo de datos
- Tabla `animal` completa con enums (`especie`, `sexo`, `tamano`, `estado`) y `foto_animal` (orden, es_principal).
- Índices: `animal(protectora_id, estado)`, trigram en `animal(nombre)`.

### API
- `POST /api/v1/animales` · `GET /api/v1/animales?estado=...` (paginación cursor) · `GET/PATCH/DELETE /api/v1/animales/{id}`
- `POST /api/v1/animales/{id}/fotos` (multipart) · `DELETE /api/v1/fotos/{id}`

### Frontend
- Formulario de alta en una pantalla (1 columna móvil, 2 desktop), drag & drop con preview.
- Lista de animales con cards (foto, nombre, badge de estado, días en protectora), filtros y búsqueda.
- Detalle de animal con hero + tabs (Ficha | Registros | Triajes).

### Tareas TDD
1. Test crear animal con datos mínimos válidos / inválidos (Pydantic) → endpoint POST.
2. Test listado filtra por protectora (RLS) y por estado → endpoint GET.
3. Test upload rechaza MIME falso, >5MB, y elimina EXIF → servicio de fotos.
4. Test soft delete: no aparece en listados pero es recuperable → DELETE.
5. Test máximo 8 fotos por animal → validación.
6. E2E: alta completa con foto en < 2 min de interacciones.

### Dependencias
- FEATURE-001 (auth y protectora).

## Criterios de aceptación / Casuística a cubrir

- [ ] Alta completa (con foto) posible en menos de 2 minutos.
- [ ] Foto con GPS embebido → coordenadas eliminadas antes de guardar.
- [ ] Archivo .exe renombrado a .jpg → rechazado con mensaje claro.
- [ ] Animal borrado → recuperable durante 30 días, invisible en listados.
- [ ] Lista usable con 3G (imágenes lazy, skeletons).
- [ ] Sin foto → placeholder digno, nunca imagen rota.
- [ ] Alt text obligatorio en cada foto (sugerido, editable).

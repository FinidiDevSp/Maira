---
id: FEATURE-001
tipo: feature
titulo: "Registro y acceso de la protectora (auth + perfil)"
estado: desarrollo
prioridad: alta
hito: "0.2"
duplicado_de: null
creado: 2026-07-02
actualizado: 2026-07-03
---

# FEATURE-001 — Registro y acceso de la protectora

## Descripción

Una voluntaria puede registrar su protectora, entrar con magic link (sin recordar contraseñas), editar el perfil de la protectora e invitar a otras voluntarias con roles.

## Contexto / impacto

Épica 1 de `ANALYSIS.md` (US-1.1 a US-1.4). Es la puerta de entrada: sin auth no hay datos protegidos ni multi-usuaria. Usuarias con baja alfabetización digital → magic link como camino principal.

## Plan de desarrollo

### Documentación a consultar
- `docs/technical/ARCHITECTURE.md` (Supabase Auth) · `docs/technical/DATA_MODEL.md` (protectora, usuario)
- `docs/operations/SECURITY.md` (JWT, RLS, roles)

> **Plan aprobado 2026-07-03 (D-015):** identidad en Supabase Auth desde el frontend
> (`@supabase/ssr`); el backend solo verifica el JWT (JWKS con PyJWT; fallback HS256 por
> `SUPABASE_JWT_SECRET` si el proyecto usa clave legacy) y carga perfil/rol de `usuario`.
> Alta passwordless: el signup invita por email (magic link), sin contraseña en MVP.

### Seguridad
- Verificación del JWT de Supabase en el backend (firma + expiración + audiencia).
- RLS en `protectora` y `usuario`: cada usuaria solo ve su protectora.
- Roles `admin | editor | lectura` aplicados en dependencias de FastAPI.
- Rate limiting en endpoints de auth (anti fuerza bruta).
- Invitaciones con token de un solo uso y caducidad.

### Modelo de datos
- `protectora` completa (nombre, CIF, dirección, teléfono, responsable, logo_url, descripcion_publica).
- `usuario` vinculado a `auth.users` de Supabase con `rol` y `protectora_id`.

### API
- `POST /api/v1/auth/signup` (protectora + admin) · `POST /api/v1/auth/login` (magic link)
- `GET/PATCH /api/v1/protectora/me` · `GET/POST /api/v1/protectora/usuarios` (invitar)

### Frontend
- Pantallas login/signup (grupo `(auth)`), perfil de protectora, gestión de voluntarias.
- Formularios con React Hook Form + Zod, mensajes de error en español llano.

### Tareas TDD
1. Test verificación JWT válido/expirado/manipulado → middleware de auth.
2. Test signup crea protectora + usuario admin atómicamente → endpoint signup.
3. Test RLS: usuaria de protectora A no lee datos de B → políticas SQL.
4. Test roles: `lectura` no puede editar perfil → dependencia de autorización.
5. Test invitación: token usado dos veces falla → flujo de invitación.
6. E2E Playwright: signup → login magic link (mock) → dashboard vacío.

### Dependencias
- FEATURE-000.

## Criterios de aceptación / Casuística a cubrir

- [ ] Signup completo en < 5 minutos con verificación de email.
- [ ] Login con magic link funcional; fallback email/contraseña (≥ 12 caracteres).
- [ ] Una usuaria JAMÁS ve datos de otra protectora (test automatizado de RLS).
- [ ] Invitación caducada o reutilizada → error claro, sin crear usuaria.
- [ ] Rol `lectura` bloqueado en toda escritura (API y UI).
- [ ] Términos y política de privacidad aceptados en el registro (texto llano).
- [ ] Accesible: flujo completo navegable por teclado y con NVDA.

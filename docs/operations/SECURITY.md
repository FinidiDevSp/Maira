# Seguridad

> Modelo de amenazas completo en [`ANALYSIS.md`](../../ANALYSIS.md) §16. Principio rector: **security by design** — cada feature llega con su sección de seguridad en el item antes de codificarse. Alineación con controles ISO 27001 anotada por bloque.

## Amenazas principales

Acceso no autorizado a datos (RLS), filtración de datos de protectoras, suplantación de voluntaria, prompt injection, abuso de API y uploads maliciosos. El repo es **público**, lo que eleva el listón: los secretos y su rotación son el riesgo nº 1.

## Controles por capa

### Autenticación y autorización (ISO A.9)

- Supabase Auth: magic link preferente, contraseña ≥ 12 chars como fallback. JWT verificado en backend (firma, expiración, audiencia).
- Roles `admin`/`editor`/`lectura` como dependencias de FastAPI + **RLS en toda tabla** como última línea de defensa (defensa en profundidad).
- Invitaciones con token de un solo uso y caducidad.

### API (ISO A.13/A.14)

- Validación de entrada con Pydantic v2 (tipos estrictos, longitudes máximas).
- Rate limiting (por usuaria, no solo IP), CORS restrictivo a orígenes conocidos.
- Errores RFC 7807 sin trazas ni internals.
- Headers: CSP, HSTS, X-Frame-Options DENY, X-Content-Type-Options nosniff, Referrer-Policy.
- Sanitización de HTML en fichas editadas (allowlist mínima).

### Uploads (ISO A.12)

MIME real verificado (magic bytes), límite 5MB, strip de EXIF (geolocalización de la protectora), fotos servidas con URLs firmadas de Supabase Storage con RLS por bucket.

### LLM (específico de Maira)

- Datos de usuario **delimitados como dato**, nunca concatenados como instrucción (anti prompt injection).
- Validación de outputs: idioma, longitud, sin HTML/código, patrones prohibidos ("diagnóstico", enfermedades como certeza).
- Triaje: reglas duras por encima del LLM (palabras de emergencia vital → ALTA siempre).
- Log de prompt+respuesta+versión para auditoría. Nunca datos de otra protectora en un prompt.

### Secretos y cadena de suministro (ISO A.10/A.15)

- `.env` fuera de git; hook `detect-private-key`; claves solo en Render/Vercel.
- Dependabot semanal; `pip-audit`/`npm audit` en CI; CodeQL (activar en GitHub al publicar).
- Filtración → [RB-4 en RUNBOOKS](RUNBOOKS.md): rotar primero.

### Datos y continuidad (ISO A.12.3, A.18)

- Cifrado at-rest (Supabase) y HTTPS extremo a extremo.
- Snapshots automáticos de Supabase (7 días) + soft delete 30 días.
- Tabla `audit_log` (user, acción, entidad, before/after, timestamp) para acciones de escritura.
- RGPD: ver [PRIVACY.md](../meta/PRIVACY.md).

## Verificación

- CI: auditoría de dependencias en cada push.
- Pre-release (FEATURE-007): OWASP ZAP baseline + revisión de headers + pentest manual de los flujos de auth.
- Reporte de vulnerabilidades externas: ver [`SECURITY.md` raíz](https://github.com/FinidiDevSp/Maira/blob/develop/SECURITY.md).

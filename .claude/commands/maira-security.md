---
description: Referencia de seguridad Maira — OWASP, JWT Supabase, uploads, prompt injection
---

# Skill: Seguridad

Docs: `docs/operations/SECURITY.md`. Contexto que lo cambia todo: **repo público** + datos de una protectora real + IA generativa de cara a usuarias no técnicas.

## Autenticación (JWT de Supabase)

- Verificar SIEMPRE en backend: firma (JWKS de Supabase), `exp`, `aud`. Nunca fiarse de un decode sin verificación.
- `SUPABASE_SERVICE_KEY` solo vive en el backend. Si aparece en frontend o en un commit → RB-4 (rotar ya).
- Autorización en dos capas: `requiere_rol(...)` en FastAPI + RLS en Postgres. Ninguna sustituye a la otra.

## Validación de entrada (OWASP API3/API8)

- Pydantic v2 estricto: longitudes máximas en todos los strings (`descripcion: str = Field(max_length=2000)`), enums cerrados, nada de `dict` libre en entrada.
- HTML de fichas editadas: sanitizar con allowlist mínima (p/em/strong/ul/li) — `nh3` o equivalente.
- CSV export: prefijar `'` a celdas que empiecen por `=`, `+`, `-`, `@` (inyección de fórmulas).

## Uploads (fotos)

1. MIME real por magic bytes (no extensión ni Content-Type del cliente).
2. Límite 5MB; redimensionar server-side.
3. **Strip EXIF** (la geolocalización delataría la ubicación de la protectora/acogida).
4. Nombre de storage generado (UUID), nunca el nombre original del fichero.
5. Servir con URLs firmadas de Supabase Storage (bucket con RLS).

## LLM — prompt injection y outputs

```python
# BIEN: dato delimitado, imposible de confundir con instrucción
prompt = PLANTILLA_FICHA.format(datos_animal=json.dumps(datos, ensure_ascii=False))
# MAL: concatenar texto libre de la usuaria al system prompt
```

- La descripción libre de la voluntaria es DATO, va delimitada (JSON o etiquetas), y el system prompt instruye ignorar instrucciones dentro de los datos.
- Validar output antes de persistir/mostrar: español, ≤ 300 palabras (ficha), JSON estricto parseado con Pydantic (triaje), regex de patrones prohibidos ("diagnóstico", "te garantizo", enfermedad afirmada como certeza).
- **Triaje: reglas duras por encima del LLM** — palabras de emergencia vital (veneno, atropello, convulsión, parto, sangrado abundante, no respira) fuerzan ALTA aunque el LLM diga otra cosa.
- Log de prompt + respuesta + `prompt_version` para auditoría. Jamás datos personales (emails, nombres de voluntarias) en prompts a proveedores externos.

## API hardening

Rate limiting por usuaria autenticada (y por IP en auth) · CORS con allowlist exacta de orígenes · headers CSP/HSTS/X-Frame-Options/nosniff vía middleware · errores RFC 7807 sin stack traces ni versiones.

## Checklist antes de mergear cualquier feature

- [ ] ¿Entrada validada con límites? ¿Salida sanitizada?
- [ ] ¿Query filtrada por protectora + test RLS si hay tabla nueva?
- [ ] ¿Algún secreto nuevo? → `.env.example` + Render/Vercel, nunca al repo.
- [ ] ¿Toca prompts? → set de validación de triaje en verde.
- [ ] ¿Registra la acción en `audit_log` si es escritura?

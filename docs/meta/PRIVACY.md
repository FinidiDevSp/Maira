# Privacidad y RGPD

Maira maneja **datos personales** (voluntarias, responsables de protectora, y potencialmente datos en notas libres), por lo que aplica el RGPD. Compromisos de ANALYSIS.md: datos mínimos, sin tracking de terceros, sin venta de datos, portabilidad total.

## Datos que tratamos

| Dato | Base legal (art. 6) | Finalidad |
|---|---|---|
| Email, nombre de la voluntaria | Ejecución de contrato (6.1.b) — uso del servicio | Cuenta y acceso |
| Datos de la protectora (CIF, dirección, teléfono, responsable) | Ejecución de contrato (6.1.b) | Perfil y ficha pública |
| Registros y fotos de animales | Interés legítimo (6.1.f) — no son datos personales salvo que aparezcan personas | Funcionalidad core |
| Notas libres | Ejecución de contrato; **política: no escribir datos de terceros en notas** (aviso en la UI) | Seguimiento del animal |
| Logs técnicos (IP, user agent) | Interés legítimo (6.1.f) — seguridad | Auditoría y abuso |

**No tratamos:** cookies de tracking, analítica de terceros, perfiles publicitarios. Solo cookies de sesión de Supabase (esenciales).

## Derechos del interesado (arts. 15-22)

- **Acceso y portabilidad:** exportación CSV/JSON completa desde la app (FEATURE-006).
- **Rectificación:** edición directa de perfil y datos.
- **Supresión ("derecho al olvido"):** borrar la protectora elimina todos sus datos (BD + Storage) de forma efectiva; los snapshots de backup expiran a los 7-30 días.
- **Oposición y limitación:** contacto directo (email del responsable en el aviso legal).
- Plazo de respuesta: 1 mes.

## Decisiones automatizadas (art. 22)

El **triaje veterinario** y las **alertas de anomalías** son procesamiento automatizado, pero **no producen efectos jurídicos ni afectan significativamente a personas** (se refieren a animales y son recomendaciones no vinculantes con validación humana explícita y disclaimer permanente). Aun así, por transparencia: la UI explica siempre que es una ayuda, no una decisión, y quién debe decidir (la voluntaria + el veterinario).

## Encargados de tratamiento (DPA)

Todos con cláusulas contractuales tipo / DPA disponibles en sus términos free tier:

| Proveedor | Rol | Datos que ve | Región |
|---|---|---|---|
| Supabase | Hosting BD/Auth/Storage | Todos | UE (elegir región eu-central al crear el proyecto) |
| Vercel / Render | Hosting app | Tráfico, logs | UE si es posible (Render: Frankfurt) |
| Groq / Google (Gemini) | LLM | Texto de fichas/triaje (NO emails ni datos de cuenta) | EE.UU. — **regla: nunca enviar datos personales en prompts** |
| HuggingFace | CV | Fotos de animales | EE.UU./UE |
| Qdrant Cloud | Vector DB | Guías veterinarias públicas (sin datos personales) | UE |
| Healthchecks.io | Uptime | Ninguno (solo pings) | UE |

**Regla de oro con la IA:** a los proveedores de LLM/CV solo viajan datos del *animal*, jamás emails, nombres de voluntarias ni datos de la cuenta.

## Registro y responsabilidad

- MVP: no se requiere DPO (tamaño y naturaleza del tratamiento); reevaluar en fase 2 (multi-protectora).
- Política de privacidad y términos en lenguaje llano antes del onboarding de la piloto (item pre-release, ver C-010/C-011 del archivo de ideas).
- Violación de seguridad con datos personales → notificación a la AEPD en 72h si hay riesgo (procedimiento en [RUNBOOKS RB-4](../operations/RUNBOOKS.md)).

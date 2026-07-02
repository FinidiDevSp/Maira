# Maira 🐾

**Plataforma web open source para protectoras de animales pequeñas.** Ficha de adopción con IA, registro diario de salud y triaje veterinario de urgencia — gratis, en español, y hecho con las voluntarias, no solo para ellas.

> Proyecto TFM · AGPL-3.0 · 100% free tiers · [Repositorio](https://github.com/FinidiDevSp/Maira)

## Empieza por aquí

| Si eres… | Lee |
|---|---|
| 🧭 Nueva en el proyecto | [Contexto de producto](product/PRODUCT_CONTEXT.md) — el mapa de todo |
| 👩‍💻 Developer | [Puesta en marcha](operations/SETUP.md) → [Arquitectura](technical/ARCHITECTURE.md) |
| 📅 Buscando el estado actual | [Backlog](planning/BACKLOG.md) (bloque "📍 Estado actual") y [Roadmap](planning/ROADMAP.md) |
| 🔒 Auditando | [Seguridad](operations/SECURITY.md) · [Privacidad RGPD](meta/PRIVACY.md) · [Testing](meta/TESTING.md) |

## Las tres capas del MVP

1. **Entrada** — la voluntaria saca una foto, escribe 3 líneas y la IA redacta la ficha de adopción.
2. **Estancia** — registro diario en 30 segundos con alertas automáticas de patrones anómalos.
3. **Síntomas** — foto + descripción → urgencia BAJA / MEDIA / ALTA con justificación. Nunca un diagnóstico.

## Stack

FastAPI · Next.js 14 · Supabase (PostgreSQL + Auth + Storage) · Groq/Gemini · Qdrant · CLIP — desplegado en Render + Vercel a **coste 0€**.

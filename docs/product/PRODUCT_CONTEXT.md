# Maira — Contexto de producto

> **Documento raíz del conocimiento del producto.** Empieza aquí si es tu primera vez.

## Qué es Maira

Maira (Μαῖρα, la perra fiel de la Odisea convertida en estrella) es una **plataforma web open source (AGPL-3.0)** para **protectoras de animales pequeñas** en España y Latinoamérica que no pueden pagar herramientas profesionales. Cubre tres momentos del ciclo de un animal:

1. **Entrada** — ficha de adopción generada con IA a partir de una foto y datos básicos.
2. **Estancia** — registro diario de salud en 30 segundos, con avisos si algo pinta mal.
3. **Síntomas** — triaje de urgencia veterinaria (baja/media/alta) con foto y descripción. *Nunca* es un diagnóstico.

Es un **TFM (3-4 meses, 1 dev)** que se defiende ante un tribunal: todo debe estar **desplegado, accesible públicamente y a coste 0€** (Vercel + Render + Supabase free tiers).

**No es:** un marketplace de adopción, un sustituto del veterinario, ni un producto de pago. La biblia completa del proyecto es [`ANALYSIS.md`](../../ANALYSIS.md) en la raíz del repo.

## Para quién

| Persona | Necesita | Maira le da |
|---|---|---|
| **Lucía**, voluntaria | Fichas y registros sin perder horas | Ficha IA en 30s, registro diario en 30s |
| **Carlos**, veterinario colaborador | Que le lleguen solo los casos que lo requieren | Triaje que filtra urgencias con historial ordenado |
| **Marta**, coordinadora | Visión de conjunto | Dashboard con métricas y export CSV |

## Catálogo de funcionalidades (vista de usuario)

<!-- RENDER:START -->
_Aún no hay funcionalidades disponibles: el proyecto está en construcción._
<!-- RENDER:END -->

## Cómo está hecho (mapa técnico)

- [Arquitectura y stack](../technical/ARCHITECTURE.md) — FastAPI + Next.js + Supabase + Groq + Qdrant
- [Modelo de datos](../technical/DATA_MODEL.md) · [Contratos de API](../technical/API_CONTRACTS.md)
- [Diseño y UX](../technical/DESIGN.md) · [Decisiones técnicas (ADR)](../technical/DECISIONS.md)
- [Seguridad](../operations/SECURITY.md) · [Privacidad y RGPD](../meta/PRIVACY.md)

## Dónde estamos y qué viene

- [Backlog operativo](../planning/BACKLOG.md) — abre por el bloque "📍 Estado actual"
- [Roadmap por hitos](../planning/ROADMAP.md) · [Changelog](../planning/CHANGELOG.md)
- [Plan del producto](PLAN.md) · [Glosario](GLOSSARY.md)

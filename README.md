# Maira 🐾

> Plataforma web **open source** para protectoras de animales pequeñas que no pueden pagar herramientas profesionales. En español desde el primer commit.

[![CI](https://github.com/FinidiDevSp/Maira/actions/workflows/ci.yml/badge.svg?branch=develop)](https://github.com/FinidiDevSp/Maira/actions/workflows/ci.yml)
[![Licencia: AGPL-3.0](https://img.shields.io/badge/licencia-AGPL--3.0-blue.svg)](LICENSE)
[![Hecho con: FastAPI + Next.js](https://img.shields.io/badge/stack-FastAPI%20%2B%20Next.js-teal.svg)](docs/technical/ARCHITECTURE.md)

**Maira** (Μαῖρα, la perra fiel de la Odisea convertida en estrella) cubre los tres momentos clave del ciclo de un animal en la protectora:

| | Momento | Qué hace Maira |
|---|---|---|
| 📸 | **Entrada** | Genera la ficha de adopción con IA a partir de una foto y 3 líneas — emotiva, honesta, sin frases hechas |
| 📋 | **Estancia** | Registro diario de salud en 30 segundos (peso, apetito, ánimo) con alertas si algo pinta mal |
| 🩺 | **Síntomas** | Triaje de urgencia con foto + descripción: BAJA / MEDIA / ALTA con justificación. **Nunca es un diagnóstico** |

Más de 1.500 protectoras en España; el 90% de las pequeñas tienen menos de 1.000€/año para herramientas digitales. Maira les da la misma tecnología que las grandes — gratis, para siempre, sin vender datos.

## Probarlo

- 🌐 **Demo desplegada:** *(URL de Vercel — disponible al completar FEATURE-000)*
- 🐳 **En local con Docker:**

```bash
git clone https://github.com/FinidiDevSp/Maira.git && cd Maira
cp .env.example .env    # rellena las claves (todas de servicios free tier)
docker compose --profile app up -d --build
# → http://localhost:3000
```

Guía completa: [docs/operations/SETUP.md](docs/operations/SETUP.md)

## Stack

**FastAPI** (Python 3.11, SQLAlchemy async) · **Next.js 14** (TypeScript, Tailwind, shadcn/ui) · **Supabase** (PostgreSQL + RLS, Auth, Storage) · **Groq** llama-3.1-70b con fallback Gemini · **Qdrant** (RAG sobre guías veterinarias) · **CLIP** en HuggingFace — desplegado en Render + Vercel, **100% free tiers**.

Detalle: [Arquitectura](docs/technical/ARCHITECTURE.md) · [Modelo de datos](docs/technical/DATA_MODEL.md) · [Decisiones (ADR)](docs/technical/DECISIONS.md)

## Documentación

La documentación vive en [`docs/`](docs/index.md) (sitio MkDocs: `make docs-serve`). Puntos de entrada:

- [Contexto de producto](docs/product/PRODUCT_CONTEXT.md) — el mapa de todo el proyecto
- [Backlog y estado actual](docs/planning/BACKLOG.md) · [Roadmap](docs/planning/ROADMAP.md)
- [Análisis completo del proyecto](ANALYSIS.md) — la biblia original (visión, personas, requisitos, riesgos)
- [Seguridad](docs/operations/SECURITY.md) · [Privacidad RGPD](docs/meta/PRIVACY.md) · [Accesibilidad y diseño](docs/technical/DESIGN.md)

## Principios

- **Ética sobre funcionalidad**: la IA nunca diagnostica, nunca promete adopciones, siempre se declara.
- **Open source real** (AGPL-3.0): las mejoras vuelven a la comunidad.
- **Sin lock-in, sin venta de datos, sin publicidad, sin planes de pago.**
- **Accesibilidad radical**: WCAG 2.2 AA, pensado para voluntarias con baja alfabetización digital.

## Contribuir

Lee [CONTRIBUTING.md](CONTRIBUTING.md) (gitflow, TDD obligatorio, Conventional Commits en español). Las vulnerabilidades se reportan según [SECURITY.md](SECURITY.md).

## Licencia

[AGPL-3.0](LICENSE) — puedes usarlo, estudiarlo, modificarlo y desplegarlo; si lo ofreces como servicio, tus mejoras también deben ser libres.

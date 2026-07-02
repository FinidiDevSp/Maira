# Glosario

Términos del dominio y técnicos usados en Maira. Ampliado desde `ANALYSIS.md` §23.

## Dominio

- **Protectora** — asociación sin ánimo de lucro que rescata y busca hogar a animales abandonados.
- **Voluntaria** — persona que colabora con la protectora (usuaria principal de Maira). Se usa el femenino como genérico: es el perfil real mayoritario del sector.
- **Coordinadora** — voluntaria que gestiona la protectora y necesita visión de conjunto.
- **Adoptante** — persona que quiere dar un hogar a un animal.
- **Acogida** — familia temporal que cuida al animal hasta su adopción definitiva.
- **Ficha de adopción** — texto descriptivo del animal para presentarlo a adoptantes.
- **Triaje** — evaluación inicial de la *urgencia* de un síntoma. NO es un diagnóstico.
- **Registro diario** — apunte rápido del estado del animal: peso, apetito, ánimo, notas.
- **Elpis** — futura app móvil para adoptantes (fase 3), conectada a Maira por API.

## Técnico

- **Item** — fichero en `docs/planning/items/` que representa una feature/bug/mejora. Única fuente de verdad de la planificación.
- **Vista renderizada** — BACKLOG, ROADMAP y el catálogo de PRODUCT_CONTEXT: se regeneran con `make render-planning`, nunca se editan a mano.
- **Consejo de Alexandria SDD** — los 6 agentes de desarrollo del proyecto (Rick, Hershel, Deanna, Eugene, Daryl, Milton). Ver `CLAUDE.md`.
- **RLS (Row Level Security)** — seguridad a nivel de fila en PostgreSQL: cada protectora solo ve lo suyo.
- **RAG (Retrieval Augmented Generation)** — el LLM responde apoyándose en guías veterinarias indexadas en Qdrant.
- **Magic link** — enlace de acceso por email, sin contraseña.
- **Free tier** — plan gratuito de un servicio cloud. Restricción dura del proyecto: solo free tiers.
- **MVP** — versión mínima del producto con las funciones esenciales del TFM.
- **ADR** — registro de una decisión de arquitectura, en [`DECISIONS.md`](../technical/DECISIONS.md).
- **WCAG / A11y** — estándar y práctica de accesibilidad web. Objetivo: WCAG 2.2 AA.
- **Soft delete** — borrado lógico recuperable durante 30 días.

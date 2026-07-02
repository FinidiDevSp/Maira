---
description: Referencia frontend Maira — Next.js App Router, shadcn/ui, tokens, a11y, i18n
---

# Skill: Frontend (Next.js 14)

Patrones obligatorios del frontend. Docs: `docs/technical/DESIGN.md` (tokens y a11y completos).

## App Router

- **Server Components por defecto**; `"use client"` solo con estado/efectos/eventos.
- Grupos de rutas: `(auth)` para login/signup, `(app)` para el dashboard autenticado.
- Datos: fetch en servidor donde se pueda; en cliente, **TanStack Query** (claves tipadas, invalidación tras mutación).
- `src/lib/api.ts` centraliza las llamadas al backend (base `NEXT_PUBLIC_API_URL`, token de Supabase inyectado, errores RFC 7807 parseados a mensajes de usuario).

## Tokens de color (de DESIGN.md — NO inventar colores)

CSS variables en `:root`/`.dark` consumidas por Tailwind:
claro → `primary #BF5B3B`, `secondary #6E9075`, `background #FAF6EF`, `foreground #2B2118`, `destructive #B3362B`, `warning #B37E1F`, `success #4A7A52`; oscuro → variantes de DESIGN.md. Urgencias de triaje: ALTA=destructive, MEDIA=warning, BAJA=success, **siempre color + icono + texto**.

## Dark mode

`next-themes` con estrategia `class`, default `system`, toggle persistente en el layout. Todo componente nuevo se revisa en ambos temas (contraste ≥ 4.5:1).

## Componentes

- **shadcn/ui copiado al repo** (`src/components/ui/`): al añadir uno, mapear sus variables a nuestros tokens. No otras librerías de componentes.
- Iconos: solo **Lucide**. Fuente: Inter vía `next/font` (self-hosted, sin CDN).
- Formularios: **React Hook Form + Zod** (schema compartido con el tipo), labels visibles, error específico bajo el campo, `aria-invalid` + `aria-describedby`.

## Accesibilidad (bloqueante)

- HTML semántico; todo interactivo alcanzable por teclado con foco visible.
- Resultados de IA (ficha, triaje) en `aria-live="polite"`.
- Imágenes de animales con `alt` significativo; decorativas `alt=""`.
- Texto base 18px; layout resiste zoom 200%; skeletons con `aria-busy`.
- Antes de dar por hecha una pantalla: test de axe sin violaciones críticas + navegación por teclado manual.

## i18n (preparado, solo ES en MVP)

- **Cero strings hardcodeados en JSX**: todo por `next-intl` (`useTranslations`) en `messages/es.json` desde el primer componente.
- Fechas `DD/MM/AAAA`, números `1.234,56` — usar los formatters de next-intl, no `toLocaleString` suelto.

## Estados de UI

Loading = skeletons (no spinners) · éxito = toast discreto · error = banner con acción de recuperación · vacío = ilustración + CTA · destructivo = modal con consecuencias explícitas. Cold start de Render: la home muestra "arrancando…" con reintento, nunca error crudo.

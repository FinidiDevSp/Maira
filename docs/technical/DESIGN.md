# Diseño y UX

## Principios (de `ANALYSIS.md` §14)

Claridad sobre creatividad · una tarea por pantalla · español cercano sin jerga · mobile-first pero desktop-comfortable · feedback < 500ms · borrado recuperable · ayuda contextual con tooltips.

## Tokens de color

Paleta cálida sin infantilizar (terracota, verde salvia, crema), con **dark mode** (decisión D-009).

| Token | Claro | Oscuro | Uso |
|---|---|---|---|
| `primary` | `#BF5B3B` (terracota) | `#D97D5C` | Acciones principales, enlaces |
| `primary-foreground` | `#FFFFFF` | `#1C1410` | Texto sobre primary |
| `secondary` | `#6E9075` (verde salvia) | `#8AAE91` | Acciones secundarias, éxito suave |
| `background` | `#FAF6EF` (crema) | `#1C1815` | Fondo de página |
| `surface` | `#FFFFFF` | `#262019` | Cards, paneles |
| `foreground` | `#2B2118` | `#F2EAE0` | Texto principal |
| `muted` | `#8A7A6D` | `#A89A8C` | Texto secundario |
| `destructive` | `#B3362B` | `#E05C4F` | Borrar, urgencia ALTA |
| `warning` | `#B37E1F` | `#D9A441` | Urgencia MEDIA |
| `success` | `#4A7A52` | `#7FB389` | Urgencia BAJA, confirmaciones |

Los tokens viven como variables CSS (`:root` / `.dark`) consumidas por Tailwind (`tailwind.config.ts`). Los estados de urgencia usan **color + icono + texto**, nunca solo color.

## Dark mode

- Estrategia `class` con `next-themes`: por defecto **según el sistema**, con toggle persistente.
- Contraste verificado ≥ 4.5:1 en ambos temas antes de introducir un color nuevo.
- Las fotos de animales no se filtran/oscurecen en dark mode.

## Tipografía e iconos

- **Inter** (variable, self-hosted vía `next/font` — sin CDN de terceros). Base **18px mínimo**, escalable a 200% sin romper layout.
- **JetBrains Mono** para código/datos técnicos.
- Iconos **Lucide** exclusivamente.

## Componentes

- **Tailwind CSS + shadcn/ui**: los componentes se copian al repo (`src/components/ui/`), no son dependencia. Ajustar sus variables a los tokens de arriba al copiarlos.
- Formularios: React Hook Form + Zod, labels siempre visibles (no placeholders como label), errores específicos bajo el campo.
- Loading: **skeletons**, no spinners. Éxito: toast discreto. Error: banner con acción de recuperación. Vacío: ilustración amable + CTA.
- Confirmación destructiva: modal con texto explícito de consecuencias.

## Responsive

Mobile-first (la voluntaria de turno usa el móvil) con desktop cómodo (el PC del refugio): formularios 1 columna en móvil / 2 en desktop, botón flotante "+ Nuevo animal" en móvil, tablas → cards en pantallas pequeñas.

## Accesibilidad (WCAG 2.2 AA — resumen operativo)

- HTML semántico, navegación completa por teclado, foco visible de 3px, skip links.
- ARIA live regions para resultados de IA (ficha, triaje).
- Alt text obligatorio en fotos (sugerido por IA, editable).
- Lenguaje llano (nivel lectura ≤ ESO); pictogramas en flujos críticos.
- Testing: axe-core en CI, pa11y por deploy, Lighthouse > 90 obligatorio, sesión manual NVDA pre-release.
- Perfil de usuarias: mayores, baja alfabetización digital, discapacidad visual, TEA (instrucciones literales, sin sobrecarga sensorial).

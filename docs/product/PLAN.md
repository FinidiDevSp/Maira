# Plan del producto

> Resumen operativo. La versión extendida (visión, personas, competencia, riesgos) es [`ANALYSIS.md`](../../ANALYSIS.md), que manda en caso de conflicto.

## El problema

Más de 1.500 protectoras en España; el 85% son asociaciones locales sin empleados y el 90% de las pequeñas tienen menos de 1.000€/año para herramientas digitales. Consecuencias concretas:

- Fichas de adopción pobres → se pierden adopciones.
- Salud registrada en libretas/Excel → la historia se pierde al cambiar de voluntaria.
- Decisiones de urgencia por intuición → visitas al vete tarde o innecesarias.

## La visión

Que cada animal en una protectora pequeña tenga la misma oportunidad de encontrar hogar que uno en una gran organización con presupuesto.

## El MVP (3-4 meses, 1 dev, TFM)

**Dentro:** auth de protectora (1 piloto), alta de animal + ficha IA, registro diario + alertas, triaje veterinario con foto, dashboard básico, export CSV/JSON, deploy 100% free tiers.

**Fuera (fase 2+):** multi-protectora, marketplace, donaciones, app móvil (Elpis), multi-idioma, chat. El archivo completo de ideas descartadas del MVP está en el [`BACKLOG.md` de la raíz](../../BACKLOG.md).

**Nunca:** venta de animales, diagnóstico veterinario, venta de datos, publicidad, planes de pago.

## Criterio de éxito (Definition of Done del MVP)

1. Una protectora real usa Maira durante 2 semanas.
2. ≥ 5 animales dados de alta con ficha generada, ≥ 10 registros diarios, ≥ 3 triajes con feedback.
3. Lighthouse A11y > 90 y 0 vulnerabilidades críticas en pentest.
4. **Demo ante el tribunal sin fricción:** URL pública funcionando + plan B local con Docker.

## Restricciones fijas

- **Coste 0€** en infraestructura y servicios (free tiers reales).
- **Repo público** ([FinidiDevSp/Maira](https://github.com/FinidiDevSp/Maira)) — la calidad del repo es parte de la nota.
- **Español primero**, i18n preparado pero no activado.
- **Ética explícita:** disclaimers de IA, sin dark patterns, accesibilidad WCAG 2.2 AA.

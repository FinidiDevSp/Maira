# Maira — Análisis Completo del Proyecto

> Biblia del proyecto. Documento vivo. Se irá corrigiendo y ampliando durante el desarrollo.
> Última revisión: 2026-06-28

---

## Tabla de contenidos

1. [Resumen ejecutivo](#1-resumen-ejecutivo)
2. [Visión y misión](#2-visión-y-misión)
3. [Problema y contexto](#3-problema-y-contexto)
4. [Usuarios y personas](#4-usuarios-y-personas)
5. [Propuesta de valor](#5-propuesta-de-valor)
6. [Alcance y no-objetivos](#6-alcance-y-no-objetivos)
7. [Roadmap y milestones](#7-roadmap-y-milestones)
8. [Requisitos funcionales](#8-requisitos-funcionales)
9. [Requisitos no funcionales](#9-requisitos-no-funcionales)
10. [Arquitectura y stack técnico](#10-arquitectura-y-stack-técnico)
11. [Modelo de datos](#11-modelo-de-datos)
12. [Diseño de API](#12-diseño-de-api)
13. [Modelo de IA/ML](#13-modelo-de-iaml)
14. [Principios UX/UI](#14-principios-uxui)
15. [Accesibilidad (A11y)](#15-accesibilidad-a11y)
16. [Seguridad y privacidad](#16-seguridad-y-privacidad)
17. [DevSecOps](#17-devsecops)
18. [Internacionalización (i18n)](#18-internacionalización-i18n)
19. [Estrategia de testing](#19-estrategia-de-testing)
20. [Métricas y analítica](#20-métricas-y-analítica)
21. [Riesgos y mitigaciones](#21-riesgos-y-mitigaciones)
22. [Preguntas abiertas](#22-preguntas-abiertas)
23. [Glosario](#23-glosario)
24. [Apéndice A: convenciones de código](#24-apéndice-a-convenciones-de-código)
25. [Apéndice B: recursos y referencias](#25-apéndice-b-recursos-y-referencias)

---

## 1. Resumen ejecutivo

**Maira** (Μαῖρα, en honor al perro fiel de la Odisea transformado en estrella) es una plataforma web open source pensada para **protectoras de animales pequeñas en España y Latinoamérica** que no pueden pagar herramientas profesionales de gestión.

El MVP cubre tres momentos clave del ciclo de un animal en la protectora:

1. **Entrada**: generación automática de fichas de adopción con texto emotivo y honesto a partir de una foto y datos básicos.
2. **Estancia**: registro diario simplificado (peso, apetito, ánimo, foto) con detección de patrones anómalos.
3. **Síntomas**: triaje veterinario básico con análisis de foto + descripción, clasificando urgencia (baja, media, alta).

El proyecto es viable como TFM de 3-4 meses en solitario, desplegable 100% en free tiers (Render, Vercel, Supabase, Groq, HuggingFace), con un piloto real validable con una protectora local.

**No es** una plataforma de marketplace de adopción tipo Petfinder. **No sustituye** al veterinario. **No gestiona** la adopción completa (eso será Elpis, la app móvil futura).

---

## 2. Visión y misión

### Visión

Que cada animal en una protectora pequeña tenga la misma oportunidad de encontrar un hogar que un animal en una gran organización con presupuesto.

### Misión

Construir una plataforma web que:
- Iguale tecnológicamente a las protectoras pequeñas con las grandes.
- Reduzca el tiempo que las voluntarias dedican a tareas administrativas y de comunicación.
- Mejore la salud y bienestar de los animales durante su estancia.
- Sea mantenida por una comunidad open source, no por una empresa con ánimo de lucro.

### Valores

- **Ética por encima de funcionalidad**: nunca añadimos una feature que pueda dañar al animal o al adoptante.
- **Open source real**: AGPL-3.0, todo el código público, decisiones transparentes.
- **Sin lock-in**: los datos se exportan en formatos abiertos, no atrapamos al usuario.
- **Hecho por y para protectoras**: las voluntarias son co-creadoras, no solo usuarias.
- **Sin venta de datos**: los datos de animales y protectoras nunca se comercializan.
- **Accesibilidad radical**: si una voluntaria tiene discapacidad o baja alfabetización digital, la herramienta se adapta.

---

## 3. Problema y contexto

### El sector de las protectoras en España (datos 2024-2025)

- Más de **1.500 protectoras** registradas en España, de las cuales el 85% son asociaciones locales sin empleados.
- Reciben entre 5 y 50 animales al mes, según tamaño.
- El 90% de las protectoras pequeñas tienen **menos de 1.000€ de presupuesto anual** para herramientas digitales.
- La tasa de abandono en España se mantiene en torno a **300.000 animales al año** (2024).

### Problemas concretos que Maira resuelve

1. **Visibilidad pobre**: muchas protectoras publican en Instagram, PDFs deprimentes, o webs obsoletas. La ficha de adopción no engancha.
2. **Gestión manual de salud**: los registros se hacen en libretas o Excel. Cuando un voluntario cambia, se pierde la historia.
3. **Decisiones de salud por intuición**: la voluntaria no sabe si un síntoma requiere ir al vete ya o puede esperar. Teme perder el tiempo del vete o, peor, que el animal empeore.
4. **Falta de tiempo**: las voluntarias son gente normal con trabajos, familias, vidas. No tienen 2 horas para escribir una ficha de adopción.
5. **Aislamiento entre protectoras**: cada una reinventa la rueda. Una protectora desbordada no sabe si hay espacio en otra cercana.

### Competencia actual

**Comercial (de pago o freemium)**:
- Shelterluv (USA, no en español)
- Petfinder (marketplace, no gestión)
- PetCoach (vet, no protectora)
- Shelter Manager (UK, no en español)

**Open source (analizado en GitHub)**:
- `mouhurtik/adoptdontshop` (TS, AGPL, 9⭐, mantenido 2026-06). Es la única referencia seria. NO tiene capa de salud ni triaje veterinario. NO tiene multi-protectora.

**Conclusión**: el mercado open source está prácticamente virgen. Maira tiene hueco claro si entrega las 3 capas (ficha + salud + triaje) en MVP.

---

## 4. Usuarios y personas

### Persona primaria: Lucía, voluntaria de protectora (40 años)

- Trabaja en una protectora en un pueblo de Toledo. 30 animales al año.
- Tiene un trabajo de 8h, familia con dos hijos, y 2-3h al día para la protectora.
- No sabe programar. Usa WhatsApp, Instagram, Google Drive, Excel básico.
- Le importa mucho el bienestar de los animales pero está quemada.
- Su mayor frustración: "perdemos adopciones porque nuestras fichas son feas, y no llegamos a todo".

### Persona secundaria: Carlos, veterinario colaborador (45 años)

- Veterinario local que colabora con varias protectoras sin cobrar o con descuento.
- Atiende llamadas de protectoras a cualquier hora.
- Su mayor frustración: "me llaman para cosas que pueden esperar, y cuando es urgente, llegan tarde porque no supieron leer los síntomas".

### Persona terciaria: Marta, coordinadora de protectora (35 años)

- Gestiona la protectora, habla con adoptantes, lleva redes, coordina voluntarios.
- Necesita ver de un vistazo: cuántos animales hay, cuánto tiempo llevan, quién está enfermo, qué fichas están pendientes.
- Su mayor frustración: "no tenemos visión de conjunto, dependemos de que alguien se acuerde".

### Antiperfil: NO es para

- Protectoras grandes con software enterprise (usan Shelterluv, etc.).
- Tiendas de animales (no es nuestro target).
- Particulares que quieren vender/criar (no marketplace).
- Administraciones públicas (necesitan otro tipo de integraciones).

---

## 5. Propuesta de valor

### Para Lucía (voluntaria)

> "Saco una foto, escribo 3 líneas, y la IA me hace la ficha de adopción que me habría llevado una hora. Cada mañana, en 2 minutos, registro el estado de todos los animales. Si un perro está raro, le saco foto y la app me dice si es urgente o puede esperar."

### Para Carlos (veterinario)

> "Las protectoras me llegan con los casos urgentes filtrados. No pierdo el tiempo con consultas que podían esperar. Y tengo un historial ordenado cuando necesito revisarlo."

### Para Marta (coordinadora)

> "Veo en un panel cuántos animales hay, cuánto tiempo llevan, quién está enfermo, qué fichas están sin publicar. Todo actualizado en tiempo real por las otras voluntarias."

### Diferenciadores frente a la competencia

1. **Open source real** (AGPL) vs. todas las alternativas comerciales.
2. **En español desde el primer commit** (no traducción de un producto anglosajón).
3. **Tres funciones en una** (ficha + salud + triaje) vs. competidores que solo hacen una.
4. **Multi-protectora con visión de red** (futuro) vs. cada protectora aislada.
5. **Ética explícita**: disclaimers claros sobre lo que la IA NO hace (no diagnostica, no sustituye al vete, no promete adopciones).
6. **Diseñado para baja alfabetización digital** vs. competidores asumiendo usuario técnico.

---

## 6. Alcance y no-objetivos

### Alcance del MVP (3-4 meses)

**IN-SCOPE**:
- Autenticación de protectoras (1 protectora piloto en MVP, multi en fase 2).
- Alta de animal: foto, datos básicos, generación de ficha IA.
- Registro diario simplificado.
- Triaje veterinario con foto + texto.
- Panel de control básico (animales, estados, alertas).
- Exportación de datos (CSV, JSON).
- Despliegue en free tiers reales.

### Fuera del alcance del MVP (a backlog)

- Marketplace público de adopción.
- Federación multi-protectora.
- Pasarela de donaciones.
- App móvil nativa.
- Multi-idioma (solo español en MVP).
- Integración con chips de identificación.
- Sistema de matching con adoptantes.
- Veterinario con chat.
- Campañas de email/SMS.
- Web pública personalizada por protectora.

### No-objetivos (no se harán nunca)

- Marketplace de venta de animales.
- Cría o venta de animales de compañía.
- Sustituir al veterinario.
- Diagnóstico veterinario.
- "Adopción instantánea" sin proceso.
- Vender datos de animales, protectoras o adoptantes.
- Publicidad de terceros.
- Planes de pago o freemium.

---

## 7. Roadmap y milestones

### Fase 0 — Pre-MVP (1-2 semanas)

- [ ] Crear cuentas en Render, Vercel, Supabase, Groq, HuggingFace.
- [ ] Esqueleto FastAPI en Render con endpoint `/health`.
- [ ] Esqueleto Next.js en Vercel conectado al backend.
- [ ] Supabase con esquema inicial (tabla protectora, animales, registros).
- [ ] Identificar y entrevistar a 1 protectora piloto real.
- [ ] Validar nombres de los campos con la voluntaria.

**Definition of Done**: ping a `/health` devuelve 200, panel web muestra "Maira" sin errores, base de datos tiene 1 protectora de prueba.

### Fase 1 — MVP técnico (4-6 semanas)

**Semana 1-2**: Auth + protectora + dashboard vacío
- [ ] Sistema de signup/login (Supabase Auth, magic link o email/password).
- [ ] CRUD de perfil de protectora.
- [ ] Dashboard básico con sidebar de navegación.

**Semana 3-4**: Alta de animal + ficha IA
- [ ] Formulario de alta: nombre, especie, raza, edad, sexo, descripción corta, foto.
- [ ] Integración con Groq (o Gemini) para generación de ficha narrativa.
- [ ] LLM con system prompt fine-tuneado en estilo de protectoras reales.
- [ ] Almacenamiento de foto en Supabase Storage.
- [ ] Preview de ficha con opción de regenerar.

**Semana 5-6**: Registro diario
- [ ] Vista de lista de animales.
- [ ] Formulario rápido de registro diario (peso, apetito, ánimo, foto opcional).
- [ ] Historial por animal (timeline visual).
- [ ] Detección básica de anomalías (reglas simples + LLM en backend).

**Semana 7-8**: Triaje veterinario
- [ ] Vista "Síntoma nuevo": foto + descripción.
- [ ] Integración con modelo de visión (CLIP o similar en HF Spaces).
- [ ] LLM con RAG sobre guías veterinarias abiertas (clasificación de urgencia).
- [ ] Disclaimer explícito "NO es diagnóstico, consulte al vete".

**Semana 9-10**: Pulido, validación, deploy
- [ ] Auditoría de accesibilidad (axe-core, pa11y, lectura manual).
- [ ] Pentest básico (OWASP ZAP).
- [ ] Onboarding con la protectora piloto real.
- [ ] Sesiones de feedback (2 mínimo).
- [ ] Corrección de bugs críticos.
- [ ] Documentación en README.
- [ ] Despliegue final estable.

**Definition of Done MVP**:
- 1 protectora real usa Maira durante 2 semanas.
- Al menos 5 animales dados de alta con fichas generadas.
- Al menos 10 registros diarios introducidos.
- Al menos 3 triajes realizados con feedback de la voluntaria.
- Auditoría A11y con score > 90 en Lighthouse.
- 0 vulnerabilidades críticas en pentest.

### Fase 2 — Post-MVP (meses 4-6)

- Federación multi-protectora.
- Mejoras de UX detectadas en feedback.
- Exportación avanzada.
- Estadísticas y métricas para la coordinadora.
- Onboarding de 2-3 protectoras más.

### Fase 3 — Elpis (meses 6-9)

- App móvil para adoptantes (ver `Elpis/ANALYSIS.md`).
- Conexión Maira ↔ Elpis vía API.

---

## 8. Requisitos funcionales

### Épica 1: Autenticación y perfil de protectora

**US-1.1**: Como voluntaria, quiero registrar mi protectora con email y datos básicos.
- Email + contraseña (mínimo 12 caracteres, con verificación).
- Nombre de la protectora, CIF/NIF, dirección, teléfono de contacto, persona responsable.
- Email de confirmación.
- Términos de uso y política de privacidad aceptados (resumidos en lenguaje llano).

**US-1.2**: Como voluntaria, quiero iniciar sesión con magic link para no recordar contraseñas.
- Supabase magic link (preferido) o email/password.

**US-1.3**: Como coordinadora, quiero editar el perfil de la protectora.
- Cambio de datos básicos, logo, descripción pública.

**US-1.4**: Como voluntaria, quiero invitar a otras voluntarias a mi protectora.
- Email de invitación, asignación de rol (admin, editor, lectura).

### Épica 2: Alta y ficha de animal

**US-2.1**: Como voluntaria, quiero dar de alta un animal nuevo en menos de 2 minutos.
- Formulario minimalista en una sola pantalla.
- Foto (drag & drop o desde cámara).
- Datos mínimos: nombre, especie (perro/gato/otro), raza, edad estimada, sexo, tamaño, descripción libre (1 párrafo).
- Peso al ingreso (opcional).

**US-2.2**: Como voluntaria, quiero que la IA genere la ficha de adopción.
- Botón "Generar ficha con IA" tras alta.
- LLM produce: titular llamativo, descripción narrativa emotiva, lista de "le gusta / no le gusta", "convive bien con...", "necesita...".
- Muestra previa con botón "Regenerar" (2-3 reintentos).
- Disclaimer: "Texto generado por IA, revíselo antes de publicar".

**US-2.3**: Como voluntaria, quiero editar la ficha IA antes de guardarla.
- Editor WYSIWYG simple.
- Estado: borrador / publicada / archivada.

**US-2.4**: Como voluntaria, quiero regenerar la ficha con instrucciones ("hazla más alegre", "enfatiza que es miedoso").
- Input de texto libre, LLM reescribe.

**US-2.5**: Como voluntaria, quiero adjuntar varias fotos al animal.
- Carrusel, máximo 5-8 fotos.

### Épica 3: Registro diario

**US-3.1**: Como voluntaria, quiero ver la lista de todos los animales actuales en un click.
- Vista principal del dashboard.
- Filtros: especie, estado (sano, enfermo, en tratamiento, listo para adoptar).
- Búsqueda por nombre.

**US-3.2**: Como voluntaria, quiero registrar el estado diario de un animal en menos de 30 segundos.
- Una pantalla, 4 campos: peso (opcional), apetito (escala 1-5), ánimo (1-5), notas libres (opcional).
- Foto opcional.

**US-3.3**: Como voluntaria, quiero ver el historial de un animal en una línea de tiempo.
- Gráfico de evolución de peso, apetito, ánimo.
- Lista de eventos (vacunas, vete, paseos, etc.).

**US-3.4**: Como voluntaria, quiero que la IA me avise si detecta un patrón anómalo.
- "Este animal lleva 3 días con apetito bajo, considera revisarlo".
- Reglas simples en backend: bajar de X en Y días = alerta.
- LLM en background para alertas complejas.

### Épica 4: Triaje veterinario

**US-4.1**: Como voluntaria, quiero subir una foto de un síntoma y describirlo.
- Una pantalla: foto (obligatoria) + texto (obligatorio, 1+ frases).
- Síntomas pre-categorizados: piel, ojos, comportamiento, digestivo, movilidad, otros.

**US-4.2**: Como voluntaria, quiero recibir una clasificación de urgencia en menos de 30 segundos.
- Tres niveles: BAJA (cita esta semana), MEDIA (cita en 24-48h), ALTA (clínica veterinaria YA).
- Justificación breve: "Detectado enrojecimiento y posible infección, podría requerir antibiótico".

**US-4.3**: Como voluntaria, quiero que la app me sugiera qué observar antes de la cita.
- Lista de preguntas para el vete basadas en el síntoma.

**US-4.4**: Como voluntaria, quiero que el triaje se guarde en el historial del animal.
- Foto + descripción + nivel de urgencia + justificación.
- Estado: pendiente de revisión / visto por vete.

**US-4.5**: Como voluntaria, quiero que la app NUNCA me diga que es un diagnóstico.
- Disclaimer permanente: "Esto NO es un diagnóstico veterinario. Siempre consulta con un profesional".

### Épica 5: Dashboard y métricas

**US-5.1**: Como coordinadora, quiero ver el panel resumen al iniciar sesión.
- Tarjetas: total animales, en tratamiento, listos para adoptar, en triaje pendiente.
- Gráfico de evolución: animales ingresados vs adoptados (futuro) últimos 6 meses.

**US-5.2**: Como coordinadora, quiero filtrar y buscar animales.
- Filtros combinables.

**US-5.3**: Como coordinadora, quiero exportar todos los datos en CSV.
- Botón "Exportar" → CSV descargable con todos los animales y registros.

### Épica 6: Administración (futuro post-MVP)

- Gestión de usuarias y roles.
- Logs de auditoría.
- Configuración de la protectora (logo, colores, datos públicos).
- Federación multi-protectora.

---

## 9. Requisitos no funcionales

### Rendimiento

- **Tiempo de respuesta** del backend < 500ms para operaciones CRUD simples.
- **Tiempo de generación de ficha IA** < 8s (90% de los casos).
- **Tiempo de triaje IA** < 15s (90% de los casos).
- **Disponibilidad objetivo** 99% en horario laboral (8-22h).
- **Carga**: soportar 5 usuarias concurrentes en MVP sin degradación.

### Escalabilidad

- Diseñado para crecer de 1 protectora a 50 sin cambios de arquitectura.
- Base de datos con índices apropiados.
- Storage de fotos con CDN.

### Compatibilidad

- **Navegadores**: Chrome, Firefox, Safari, Edge (últimas 2 versiones).
- **Dispositivos**: responsive (móvil, tablet, escritorio).
- **Conexión**: usable con 3G (graceful degradation).

### Usabilidad

- **Onboarding** completado en < 5 minutos.
- **Tasa de error** en formularios < 5%.
- **Help text** contextual en todos los campos críticos.

### Mantenibilidad

- **Cobertura de tests** mínima 70% en backend.
- **Linting** estricto (ruff en Python, ESLint en TS).
- **Documentación**: cada módulo con docstring y README.
- **Type hints** en Python, TypeScript estricto en frontend.

### Observabilidad

- Logs estructurados (JSON).
- Métricas de uso (animales dados de alta, fichas generadas, triajes).
- Alertas si el backend cae (Healthchecks.io free).

---

## 10. Arquitectura y stack técnico

### Diagrama lógico

```
┌─────────────────┐         ┌──────────────────┐
│  Frontend Web   │ ──────► │   Backend API    │
│  Next.js 14     │  HTTPS  │   FastAPI        │
│  (Vercel)       │         │   (Render free)  │
└─────────────────┘         └────────┬─────────┘
                                     │
                          ┌──────────┴──────────┐
                          ▼                     ▼
                  ┌──────────────┐      ┌──────────────┐
                  │  PostgreSQL  │      │  Supabase    │
                  │  (Supabase)  │      │  Storage     │
                  └──────────────┘      │  (fotos)     │
                          ▲             └──────────────┘
                          │
                  ┌───────┴────────┐
                  │   Qdrant      │
                  │   Cloud free  │
                  │   (RAG)       │
                  └───────────────┘
                          ▲
                          │
       ┌──────────────────┴──────────────────┐
       │                                     │
┌──────┴───────┐                    ┌────────┴────────┐
│  Groq LLM    │                    │  HuggingFace    │
│  (Llama 3.1) │                    │  Spaces         │
│  fichas/     │                    │  (CV models)    │
│  triaje      │                    └─────────────────┘
└──────────────┘
```

### Stack detallado

**Frontend**
- **Next.js 14** (App Router) — SSR + client components.
- **TypeScript estricto** — no `any` salvo justificado.
- **Tailwind CSS** — utility-first, rápido de iterar.
- **shadcn/ui** — componentes accesibles copiados al repo (no dependencia).
- **React Hook Form** + **Zod** — formularios con validación.
- **TanStack Query** — cache y revalidación.
- **next-intl** — i18n (preparado, solo español en MVP).
- **Despliegue**: Vercel (free tier).

**Backend**
- **Python 3.11+** con type hints.
- **FastAPI** — async, OpenAPI auto, validación con Pydantic.
- **SQLAlchemy 2.0** — ORM async.
- **Alembic** — migraciones.
- **Pydantic v2** — validación.
- **structlog** — logging JSON.
- **pytest** + **httpx** — tests.
- **ruff** + **mypy** — linting y tipos.
- **Despliegue**: Render (free tier, sleep tras 15 min inactividad — acceptable para MVP).

**Base de datos**
- **Supabase PostgreSQL** (free tier, 500MB) — DB principal.
- **Row Level Security (RLS)** — seguridad por protectora.
- **Supabase Auth** — magic link o email/password.
- **Supabase Storage** — fotos (10GB free).

**Vector DB**
- **Qdrant Cloud** (free tier, 1GB, 1 cluster) — RAG sobre guías veterinarias y datos propios.

**LLM**
- **Groq** (free tier) — modelo principal: `llama-3.1-70b-versatile`.
- Fallback: **Google Gemini 1.5 Flash** (free tier).
- Capa de abstracción para cambiar de proveedor sin reescribir.

**Computer Vision**
- **HuggingFace Spaces** (free, CPU) — modelo CLIP o fine-tuned.
- Modelo alternativo: `openai/clip-vit-base-patch32` directamente desde HF Inference API.
- Para triaje: modelo fine-tuneado con datos de皮肤病 comunes (placeholder hasta validar).

**Otros servicios**
- **Healthchecks.io** (free, 20 checks) — monitor de uptime.
- **Sentry** (free tier developer) — error tracking (opcional).
- **Cloudflare R2** (10GB free) — backup de fotos (futuro).

### Estructura del repositorio

```
maira/
├── README.md
├── LICENSE (AGPL-3.0)
├── docker-compose.yml (para dev local)
├── .env.example
├── .github/
│   ├── workflows/
│   │   ├── ci.yml (lint + test)
│   │   ├── cd.yml (deploy a Render/Vercel)
│   │   ├── codeql.yml (SAST)
│   │   └── dependabot.yml
│   └── ISSUE_TEMPLATE/
├── backend/
│   ├── pyproject.toml
│   ├── Dockerfile
│   ├── alembic/
│   ├── src/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── api/
│   │   │   ├── auth.py
│   │   │   ├── protectora.py
│   │   │   ├── animal.py
│   │   │   ├── registro.py
│   │   │   ├── triaje.py
│   │   │   └── health.py
│   │   ├── services/
│   │   │   ├── llm.py
│   │   │   ├── vision.py
│   │   │   ├── rag.py
│   │   │   └── triage.py
│   │   └── core/
│   │       ├── security.py
│   │       ├── logging.py
│   │       └── exceptions.py
│   └── tests/
├── frontend/
│   ├── package.json
│   ├── next.config.js
│   ├── tailwind.config.ts
│   ├── src/
│   │   ├── app/
│   │   │   ├── (auth)/
│   │   │   │   ├── login/
│   │   │   │   └── signup/
│   │   │   ├── (app)/
│   │   │   │   ├── dashboard/
│   │   │   │   ├── animales/
│   │   │   │   ├── animales/[id]/
│   │   │   │   ├── triaje/
│   │   │   │   └── perfil/
│   │   │   ├── layout.tsx
│   │   │   └── page.tsx
│   │   ├── components/
│   │   │   ├── ui/ (shadcn)
│   │   │   ├── animal/
│   │   │   ├── triaje/
│   │   │   └── ...
│   │   ├── lib/
│   │   │   ├── api.ts
│   │   │   ├── auth.ts
│   │   │   └── utils.ts
│   │   └── styles/
│   └── tests/
├── docs/
│   ├── ARCHITECTURE.md
│   ├── DATA_MODEL.md
│   ├── API.md
│   ├── DEPLOY.md
│   ├── SECURITY.md
│   ├── A11Y.md
│   └── RUNBOOK.md
└── scripts/
    ├── seed.py
    └── backup.sh
```

### Decisiones de arquitectura (ADRs)

- **ADR-001: Monolito modular en backend** en lugar de microservicios. Razón: 1 dev, 3-4 meses, escala suficiente.
- **ADR-002: Next.js con App Router** sobre Pages Router. Razón: mejor DX, server components, i18n nativo.
- **ADR-003: Supabase en lugar de Firebase**. Razón: PostgreSQL real, RLS, open source, mejor para SQL.
- **ADR-004: Groq como LLM principal** sobre OpenAI. Razón: free tier generoso, latencia muy baja, calidad comparable.
- **ADR-005: AGPL-3.0 como licencia**. Razón: garantiza que las mejoras vuelvan a la comunidad, evita fork privativo.
- **ADR-006: Multi-tenant por protectora con RLS** en lugar de DBs separadas. Razón: simplicidad, escalabilidad aceptable.

---

## 11. Modelo de datos

### Diagrama ER (simplificado)

```
┌─────────────┐      ┌──────────────┐      ┌──────────────┐
│ protectora  │──┐   │   animal     │──┐   │  registro    │
│             │  │   │              │  │   │  _diario     │
└─────────────┘  │   └──────────────┘  │   └──────────────┘
       │        │          │            │          │
       │        └──────────┘            │          │
       │                                │          │
       │          ┌──────────────┐      │          │
       │          │   triaje     │◄─────┘          │
       │          │   _vet       │                 │
       │          └──────────────┘                 │
       │                                │          │
       │          ┌──────────────┐      │          │
       └─────────►│   usuario    │      │          │
                  │   (voluntaria│      │          │
                  └──────────────┘      │          │
                                       │          │
                  ┌──────────────┐      │          │
                  │   foto       │◄─────┴──────────┘
                  │   _animal    │
                  └──────────────┘
```

### Tablas principales (esquema simplificado)

**protectora**
- `id` UUID PK
- `nombre` TEXT NOT NULL
- `cif` TEXT
- `direccion` TEXT
- `telefono` TEXT
- `email` TEXT NOT NULL
- `persona_responsable` TEXT
- `logo_url` TEXT
- `descripcion_publica` TEXT
- `created_at` TIMESTAMPTZ
- `updated_at` TIMESTAMPTZ

**usuario** (Supabase Auth + perfil)
- `id` UUID PK (referencia a auth.users)
- `protectora_id` UUID FK → protectora
- `email` TEXT NOT NULL
- `nombre` TEXT
- `rol` ENUM('admin', 'editor', 'lectura')
- `created_at` TIMESTAMPTZ

**animal**
- `id` UUID PK
- `protectora_id` UUID FK → protectora
- `nombre` TEXT NOT NULL
- `especie` ENUM('perro', 'gato', 'otro')
- `raza` TEXT
- `edad_estimada` TEXT
- `sexo` ENUM('macho', 'hembra', 'desconocido')
- `tamano` ENUM('pequeño', 'mediano', 'grande', 'desconocido')
- `descripcion_libre` TEXT
- `estado` ENUM('en_acogida', 'disponible', 'en_tratamiento', 'reservado', 'adoptado', 'fallecido', 'devuelto')
- `fecha_ingreso` DATE NOT NULL
- `fecha_salida` DATE
- `peso_ingreso_kg` NUMERIC
- `ficha_ia_texto` TEXT
- `ficha_ia_metadata` JSONB (modelo, prompt version, regeneraciones)
- `ficha_estado` ENUM('borrador', 'publicada', 'archivada')
- `created_at` TIMESTAMPTZ
- `updated_at` TIMESTAMPTZ

**foto_animal**
- `id` UUID PK
- `animal_id` UUID FK → animal
- `storage_path` TEXT NOT NULL
- `es_principal` BOOLEAN
- `orden` INT
- `uploaded_by` UUID FK → usuario
- `created_at` TIMESTAMPTZ

**registro_diario**
- `id` UUID PK
- `animal_id` UUID FK → animal
- `fecha` DATE NOT NULL
- `peso_kg` NUMERIC
- `apetito` SMALLINT (1-5)
- `animo` SMALLINT (1-5)
- `notas` TEXT
- `foto_id` UUID FK → foto_animal (nullable)
- `registrado_por` UUID FK → usuario
- `created_at` TIMESTAMPTZ
- UNIQUE(animal_id, fecha)

**triaje_vet**
- `id` UUID PK
- `animal_id` UUID FK → animal
- `foto_id` UUID FK → foto_animal
- `descripcion` TEXT NOT NULL
- `categoria` ENUM('piel', 'ojos', 'comportamiento', 'digestivo', 'movilidad', 'respiratorio', 'otro')
- `nivel_urgencia` ENUM('baja', 'media', 'alta')
- `justificacion_ia` TEXT
- `sugerencias_observacion` TEXT[]
- `revisado_por_vete` BOOLEAN DEFAULT FALSE
- `revisado_at` TIMESTAMPTZ
- `revisado_por_usuario` UUID FK → usuario
- `created_at` TIMESTAMPTZ

**evento_salud** (futuro, no MVP)
- Vacunas, desparasitaciones, visitas al vete, etc.

### Índices clave

- `animal(protectora_id, estado)` — listados filtrados.
- `registro_diario(animal_id, fecha DESC)` — timeline.
- `triaje_vet(animal_id, created_at DESC)` — historial clínico.
- `animal(nombre) trigram` — búsqueda fuzzy.

### Row Level Security (Supabase)

```sql
-- Política ejemplo: un usuario solo ve animales de su protectora
CREATE POLICY "usuarios ven su protectora" ON animal
  FOR ALL USING (
    protectora_id IN (
      SELECT protectora_id FROM usuario WHERE id = auth.uid()
    )
  );
```

---

## 12. Diseño de API

### Convenciones

- **REST** sobre JSON.
- **Prefijo**: `/api/v1`
- **Versionado**: en URL (`/v1/`, `/v2/`).
- **Auth**: Bearer token (JWT de Supabase).
- **Errores**: RFC 7807 (Problem Details for HTTP APIs).
- **Paginación**: cursor-based con `?cursor=X&limit=20`.
- **Filtros**: query params, formato `?field=value`.

### Endpoints principales (resumen)

**Auth**
- `POST /api/v1/auth/signup` — registro de protectora + admin.
- `POST /api/v1/auth/login` — magic link.
- `POST /api/v1/auth/refresh` — refresh token.

**Protectora**
- `GET /api/v1/protectora/me` — perfil actual.
- `PATCH /api/v1/protectora/me` — actualizar perfil.
- `GET /api/v1/protectora/usuarios` — listar voluntarias.
- `POST /api/v1/protectora/usuarios` — invitar voluntaria.

**Animales**
- `GET /api/v1/animales?estado=disponible&limit=20` — listar con filtros.
- `GET /api/v1/animales/{id}` — detalle.
- `POST /api/v1/animales` — crear animal.
- `PATCH /api/v1/animales/{id}` — actualizar.
- `DELETE /api/v1/animales/{id}` — soft delete.
- `POST /api/v1/animales/{id}/ficha/generar` — generar ficha IA.
- `POST /api/v1/animales/{id}/ficha/regenerar` — regenerar con instrucciones.

**Fotos**
- `POST /api/v1/animales/{id}/fotos` — upload (multipart).
- `DELETE /api/v1/fotos/{id}` — eliminar.

**Registros diarios**
- `GET /api/v1/animales/{id}/registros?limit=30` — timeline.
- `POST /api/v1/animales/{id}/registros` — crear registro.
- `PATCH /api/v1/registros/{id}` — editar.

**Triaje**
- `POST /api/v1/animales/{id}/triaje` — crear triaje (multipart: foto + json).
- `GET /api/v1/animales/{id}/triajes` — historial.
- `PATCH /api/v1/triajes/{id}` — marcar revisado por vete.

**Dashboard**
- `GET /api/v1/dashboard/resumen` — métricas para la coordinadora.

**Export**
- `GET /api/v1/export/animales.csv`
- `GET /api/v1/export/registros.csv`

### Ejemplo de request/response

**Generar ficha IA**:
```
POST /api/v1/animales/abc-123/ficha/generar
Authorization: Bearer eyJhbGc...

→ 200 OK
{
  "ficha_id": "ficha-456",
  "texto": "Luna es una perrita de mirada dulce que...",
  "metadata": {
    "modelo": "llama-3.1-70b-versatile",
    "prompt_version": "1.2.0",
    "tokens_input": 234,
    "tokens_output": 412,
    "latencia_ms": 3200
  },
  "created_at": "2026-06-28T15:30:00Z"
}
```

**Triaje**:
```
POST /api/v1/animales/abc-123/triaje
Content-Type: multipart/form-data
Authorization: Bearer eyJhbGc...

foto: [binary]
descripcion: "Cojea de la pata trasera derecha desde ayer"
categoria: "movilidad"

→ 200 OK
{
  "triaje_id": "triaje-789",
  "nivel_urgencia": "media",
  "justificacion": "La cojera en pata trasera puede deberse a esguince, distensión o problema articular. No parece haber herida abierta, pero requiere evaluación veterinaria en 24-48h para descartar fractura o rotura de ligamentos.",
  "sugerencias": [
    "Observar si apoya la pata al caminar",
    "Revisar si hay hinchazón o calor en la zona",
    "Limitar ejercicio hasta la visita al veterinario"
  ],
  "disclaimer": "Esto NO es un diagnóstico veterinario. Consulta siempre con un profesional.",
  "metadata": {
    "vision_model": "openai/clip-vit-base-patch32",
    "llm_model": "llama-3.1-70b-versatile",
    "rag_chunks_used": 3
  }
}
```

---

## 13. Modelo de IA/ML

### Componente 1: Generación de fichas narrativas

**Modelo**: `llama-3.1-70b-versatile` (Groq) o `gemini-1.5-flash` (Google).

**System prompt** (versión 1.0):
```
Eres unaCopywriter especializada en fichas de adopción para protectoras de animales en España. Tu objetivo es escribir textos emotivos, honestos y que conecten con adoptantes potenciales, sin sensacionalismo ni culpa.

Reglas:
- Máximo 300 palabras.
- Tono cálido pero realista (no edulcorado).
- Evita frases hechas tipo "te llenará de amor", "será tu mejor amigo".
- Menciona carácter y necesidades concretas.
- Si el animal tiene miedos, problemas de salud o necesidades especiales, dilo con honestidad.
- Si el animal convive con niños, perros, gatos u otros, especifícalo.
- Termina con una llamada a la acción clara.
- NO inventes información que no te doy.
- NO uses palabras en inglés.

Input del usuario: {datos del animal}

Output: solo el texto de la ficha, sin preámbulos.
```

**Few-shot examples**: 3-5 ejemplos de fichas reales de protectoras (anonimizadas), validadas con la voluntaria piloto.

**Estrategia de mejora continua**:
- Versión 1.0: prompt base, few-shot genérico.
- Versión 1.1: tras feedback de la voluntaria, ajustar tono/longitud.
- Versión 1.2: añadir más ejemplos validados.
- Versión 2.0 (post-MVP): fine-tune con Llama 3.1 8B en HF con dataset propio.

**Métricas de calidad**:
- Tasa de "regenerar" (cuántas veces la voluntaria regenera antes de aceptar): objetivo < 1.5.
- Tasa de "edición manual" (cuánto cambia la voluntaria el texto IA): objetivo < 30% del texto.
- Feedback cualitativo en entrevistas con la voluntaria.

### Componente 2: Triaje veterinario

**Pipeline**:
1. Upload foto + descripción.
2. Modelo CV (CLIP) extrae features de la imagen.
3. RAG: búsqueda semántica en Qdrant sobre guías veterinarias abiertas.
4. LLM recibe: features visuales + descripción texto + contexto RAG → clasificación urgencia + justificación.

**RAG Knowledge Base** (a construir):
- Guías veterinarias en español (CC-BY o abiertas):
  - Manual Merck Veterinary (parcial en español).
  - Guías de AVEPA (Asociación de Veterinarios Españoles).
  - Protocolos de hospitales veterinarios universitarios (CREA, UAB).
  - Recursos de Royal Canin, Hill's en abierto.
- Chunks: ~500 tokens cada uno, overlap 50.
- Embeddings: `paraphrase-multilingual-MiniLM-L12-v2` (multilingüe, gratis en HF).
- Vector store: Qdrant Cloud free.

**Prompt de triaje**:
```
Eres un asistente de triaje veterinario. Tu trabajo es ayudar a voluntarias de protectoras a clasificar la URGENCIA de un síntoma observado en un animal, NO de diagnosticarlo.

Niveles:
- BAJA: cita esta semana. Síntomas leves, sin dolor aparente, sin empeoramiento rápido.
- MEDIA: cita en 24-48h. Síntomas que causan molestias, posibles infecciones, cojeras leves.
- ALTA: clínica veterinaria YA. Síntomas graves: dificultad respiratoria, sangrado, letargo extremo, convulsiones, vómitos repetidos, no come/beber 24h+, dolor intenso.

Información del animal:
- Especie: {especie}
- Edad estimada: {edad}
- Historial relevante: {historial}

Síntoma reportado:
- Foto analizada (features visuales): {features_cv}
- Descripción: {descripcion}
- Categoría: {categoria}

Contexto veterinario relevante (RAG):
{contexto_rag}

Output (JSON estricto):
{
  "nivel_urgencia": "baja|media|alta",
  "justificacion": "máximo 80 palabras, en lenguaje llano",
  "sugerencias_observacion": ["3-5 preguntas para el vete"]
}

IMPORTANTE: 
- NUNCA digas "es un diagnóstico" o "es X enfermedad".
- SIEMPRE recomienda consultar al vete.
- Si dudas, clasifica como nivel más alto.
- Si el síntoma sugiere envenenamiento, trauma, parto difícil, o emergencia vital, SIEMPRE clasifica como ALTA.
```

**Modelo CV**: empezar con `openai/clip-vit-base-patch32` de HF para extraer features. Evaluar tras MVP si vale la pena fine-tunear con datos veterinarios (probablemente no, por falta de dataset).

**Métricas de calidad**:
- Tasa de "falsos negativos altos" (urgencia alta clasificada como baja): objetivo < 5%. Crítico para la ética del proyecto.
- Tasa de acuerdo con veterinario real (cuando se pueda medir): objetivo > 70%.
- Feedback cualitativo del veterinario colaborador.

### Componente 3: Detección de anomalías en registros

**Reglas simples** (MVP):
- Apetito < 2 durante 3 días consecutivos → alerta "revisar".
- Peso baja > 10% en 30 días → alerta "revisar".
- Sin registro en 3 días → recordatorio.
- Cambio brusco de ánimo (delta > 3) → alerta.

**LLM opcional** (MVP): análisis mensual con LLM que resume patrones y sugiere observaciones.

### Capa de abstracción LLM

```python
# src/services/llm.py
class LLMProvider(Protocol):
    async def complete(self, prompt: str, **kwargs) -> LLMResponse: ...
    async def embed(self, text: str) -> list[float]: ...

class GroqProvider:
    ...

class GeminiProvider:
    ...

# Selección por env var
def get_provider() -> LLMProvider:
    if settings.llm_provider == "groq":
        return GroqProvider(...)
    elif settings.llm_provider == "gemini":
        return GeminiProvider(...)
    else:
        raise ValueError(...)
```

---

## 14. Principios UX/UI

### Principios generales

1. **Claridad sobre creatividad**: preferimos interfaces obvias a interfaces ingeniosas.
2. **Una tarea por pantalla**: el usuario nunca debe estar abrumado.
3. **Texto en español con tono cercano**: no traducido, escrito pensando en una voluntaria de protectora.
4. **Sin jerga técnica**: "ficha" no "record", "alta" no "create instance".
5. **Mobile-first pero desktop-comfortable**: la protectora usa el PC del refugio, pero la voluntaria de turno usa el móvil.
6. **Feedback inmediato**: cada acción tiene respuesta visual en < 500ms.
7. **Recuperable**: borrar es reversible (soft delete) durante 30 días.
8. **Ayuda contextual**: tooltip en campos críticos, no modal largo.

### Lenguaje visual

- **Paleta**: tonos cálidos pero no infantilizados. Terracota, verde suave, crema.
- **Tipografía**: Inter (legible, sans, gratis).
- **Iconografía**: Lucide (consistente, open source).
- **Espaciado**: generoso, no claustrofóbico.
- **Sombras**: suaves, nada de flat design duro.

### Pantallas clave (descripción)

**Login**: una pantalla, email + botón "Entrar con magic link". Logo de la protectora arriba. Enlace "¿No tienes cuenta? Regístrate".

**Dashboard**: 
- Saludo personalizado ("Hola, Lucía").
- 4 tarjetas con métricas grandes: total animales, en tratamiento, disponibles para adoptar, triajes pendientes.
- Lista de últimos registros de hoy.
- Accesos rápidos: "Alta animal", "Triaje nuevo", "Ver animales".

**Lista de animales**:
- Cards con foto, nombre, especie, estado (color badge), días en protectora.
- Filtros laterales: especie, estado, edad, tamaño.
- Botón flotante "+ Nuevo animal".

**Detalle de animal**:
- Hero con foto principal, nombre, datos básicos.
- Tabs: Ficha | Registros | Triajes | Eventos.
- Botones de acción: "Generar ficha IA", "Nuevo registro", "Nuevo triaje".

**Alta de animal**:
- Formulario en una pantalla, una columna en móvil, dos en desktop.
- Foto arrastrable, preview inmediato.
- Campos mínimos visibles, avanzados en "Más opciones".
- Botón principal: "Crear y generar ficha IA".

**Generación de ficha IA**:
- Loading claro ("La IA está escribiendo la ficha...").
- Texto generado en grande, fácil de leer.
- Botones: "Regenerar", "Editar", "Aceptar y guardar".

**Triaje nuevo**:
- Foto grande arrastrable, campo de descripción abajo.
- Botón "Analizar".
- Resultado en card con: badge de urgencia (color), justificación, sugerencias, disclaimer.

### Estados y feedback

- **Loading**: skeletons, no spinners.
- **Éxito**: toast discreto en la esquina.
- **Error**: banner claro, no modal bloqueante. Acción de recuperación siempre visible.
- **Vacío**: ilustración amable + CTA claro.
- **Confirmación destructiva**: modal con texto explícito ("¿Estás segura? El animal se archivará y no será visible").

---

## 15. Accesibilidad (A11y)

### Compromiso

WCAG 2.2 nivel AA mínimo, aspiración a AAA donde sea posible.

### Prácticas por defecto

- **HTML semántico**: `<button>`, `<nav>`, `<main>`, `<label>` siempre que aplique.
- **Contraste mínimo** 4.5:1 en texto, 3:1 en elementos UI grandes.
- **Navegación por teclado** completa. Skip links al contenido principal.
- **Foco visible** con outline de 3px y contraste alto.
- **ARIA labels** en iconos sin texto y en regiones dinámicas (live regions para resultados IA).
- **Alt text** obligatorio en todas las fotos de animales. Sugerido por IA pero revisable.
- **Lenguaje claro**: nivel de lectura ≤ ESO. Herramienta: hemingwayapp.com o similar.
- **No depender del color**: estados con texto + icono + color, no solo color.
- **Formularios**: labels asociados, mensajes de error específicos, no "campo inválido".
- **Tiempo**: sin límites de tiempo, pero con persistencia de borradores.

### Testing de A11y

- **axe-core** integrado en CI (Lighthouse + axe-playwright).
- **pa11y** para chequeos automáticos en cada deploy.
- **Lighthouse A11y score** > 90 obligatorio para MVP.
- **Lectura manual** con NVDA (Windows) y VoiceOver (Mac) al menos 1 vez antes de release.
- **Test con usuarias reales** con discapacidad (idealmente 1 sesión pre-release).

### Consideraciones específicas

- **Voluntarias mayores**: tipografía configurable (tamaño base 18px mínimo, escalable a 200%).
- **Baja alfabetización digital**: pictogramas en flujos críticos, no en todos.
- **Voluntarias con discapacidad visual**: NVDA compatible, navegación por teclado.
- **Voluntarias con TEA**: instrucciones literales, sin ambigüedades, sin sobrecarga sensorial.

---

## 16. Seguridad y privacidad

### Modelo de amenazas

**Amenazas principales**:
1. Acceso no autorizado a datos de animales (fotos, fichas).
2. Filtración de datos de protectoras.
3. Suplantación de identidad de una voluntaria.
4. Inyección de prompts en el LLM (prompt injection).
5. Abuso de la API (scraping, brute force).
6. Subida de archivos maliciosos (imágenes con exploits).

### Medidas de seguridad

**Autenticación y autorización**:
- Supabase Auth con magic link o email/password.
- JWT firmado, refresh tokens.
- Roles: admin, editor, lectura. RLS en cada tabla.
- 2FA opcional (futuro).

**Cifrado**:
- HTTPS obligatorio (Vercel y Render lo proveen).
- Cifrado at-rest en Supabase.
- Fotos en Supabase Storage con URLs firmadas.
- Secrets en variables de entorno (nunca en código).

**API security**:
- Rate limiting (Render + Cloudflare).
- CORS restrictivo.
- Validación de inputs con Pydantic.
- Sanitización de HTML en fichas.
- CSRF protection en formularios.
- Headers de seguridad: CSP, HSTS, X-Frame-Options, etc.

**LLM security**:
- System prompts robustos contra prompt injection.
- Validación de outputs (no devolver código, no exponer internals).
- No pasar datos sensibles de otras protectoras en prompts.
- Logs de prompts y respuestas para auditoría.
- Disclaimer permanente de que la IA puede equivocarse.

**Uploads**:
- Validación de tipo MIME.
- Límite de tamaño (5MB por foto en MVP).
- Strip de metadatos EXIF (privacidad de ubicación).
- Virus scan (opcional, futuro).

**Backups**:
- Backup diario de PostgreSQL (Supabase hace snapshots automáticos).
- Backup de Storage semanal.
- Retención 30 días.

**Auditoría**:
- Logs de todas las acciones (crear, editar, borrar, generar ficha, triaje).
- Tabla `audit_log` con: user_id, action, entity, before, after, timestamp.

### Privacidad

- **Datos personales mínimos**: solo lo necesario para el funcionamiento.
- **Sin tracking de terceros**: no Google Analytics, no Meta Pixel, nada.
- **Sin venta de datos**: compromiso explícito en términos.
- **Derecho al olvido**: borrar protectora = borrar todos sus datos.
- **Portabilidad**: exportación CSV/JSON de todos los datos.
- **RGPD compliance**: textos legales revisados, DPO no obligatorio para MVP por tamaño.

---

## 17. DevSecOps

### Pipeline CI/CD (GitHub Actions)

**`ci.yml` (en cada PR)**:
- Linting backend: `ruff check`, `mypy`, `black --check`.
- Linting frontend: `eslint`, `prettier --check`, `tsc --noEmit`.
- Tests backend: `pytest --cov`.
- Tests frontend: `vitest run`.
- Build: docker build del backend.
- Auditoría A11y: `pa11y-ci` contra el dev server.
- SAST: GitHub CodeQL.

**`cd.yml` (en merge a main)**:
- Deploy backend a Render (auto si la PR es mergeada).
- Deploy frontend a Vercel (auto).
- Smoke tests contra el entorno de producción.
- Notificación a Discord/Telegram (opcional).

**`codeql.yml`**: semanal + en cada PR, análisis de seguridad.

**`dependabot.yml`**: actualizaciones automáticas de dependencias (semanal).

### Seguridad

- **Trivy** en CI para escaneo de imágenes Docker.
- **Snyk** (free tier) para análisis de vulnerabilidades en dependencias.
- **OWASP ZAP** para pentest manual pre-release.
- **Secret scanning**: GitHub secret scanning habilitado.
- **Branch protection**: main requiere 1 review + CI passing.

### Despliegue

**Backend (Render)**:
- Free tier, sleep tras 15 min inactividad.
- Cold start aceptable para MVP (5-10s).
- Variable de entorno: `DATABASE_URL`, `SUPABASE_URL`, `SUPABASE_KEY`, `GROQ_API_KEY`, `QDRANT_URL`, `QDRANT_KEY`, `SECRET_KEY`.
- Health check: `GET /health` cada 5 min.
- Logs: stdout JSON, capturados por Render.

**Frontend (Vercel)**:
- Free tier.
- Preview deployments por PR.
- Variables de entorno: `NEXT_PUBLIC_API_URL`, `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`.

**Base de datos (Supabase)**:
- Free tier, 500MB.
- Backups automáticos.
- Migrations vía Alembic.

**Storage (Supabase Storage)**:
- Free tier, 10GB.
- Bucket `fotos-animales` con RLS.

### Monitoring

- **Healthchecks.io** (free, 20 checks): ping cada 5 min al backend.
- **Logs centralizados** en Render (gratis, retenidos 7 días).
- **Alertas**: email si backend > 1 min sin responder.

### Runbook

Ver `docs/RUNBOOK.md` (a crear):
- Cómo desplegar.
- Cómo hacer rollback.
- Cómo restaurar backup.
- Cómo responder a un incidente de seguridad.
- Cómo responder a un bug en producción.

---

## 18. Internacionalización (i18n)

### Estado actual

- **MVP**: solo español (es-ES).
- **Post-MVP**: catalán, euskera, gallego (alta demanda en protectoras locales).
- **Largo plazo**: portugués (Brasil tiene sector similar), inglés.

### Implementación

- **Frontend**: `next-intl` con archivos de mensajes.
- **Backend**: mensajes de error en español, fechas en formato europeo.
- **Textos LLM**: prompts en español, validación de que el output esté en español.
- **Persistencia**: campo `lang` en protectora para futuro multi-idioma.

### Convenciones

- **Fechas**: `DD/MM/AAAA` (formato europeo).
- **Números**: `1.234,56` (coma decimal, punto de millares).
- **Moneda**: EUR con `€` después.
- **Teléfono**: formato internacional `+34 600 000 000`.

---

## 19. Estrategia de testing

### Pirámide de tests

```
       /\
      /  \      E2E (pocos, críticos)
     /----\
    /      \    Integración (moderados)
   /--------\
  /          \  Unitarios (muchos)
 /------------\
```

### Unitarios (objetivo: 70% cobertura backend)

- Servicios: `test_llm.py`, `test_vision.py`, `test_triage.py`.
- Reglas de detección de anomalías.
- Validadores de schemas Pydantic.
- Helpers de seguridad.

**Herramientas**: `pytest`, `pytest-asyncio`, `pytest-cov`.

### Integración

- Endpoints con TestClient de FastAPI.
- DB con SQLite en memoria o testcontainers.
- Mocking de Groq y HuggingFace con `respx` o `vcrpy`.

### E2E (pocos, críticos)

- Flujo signup → alta animal → generación ficha.
- Flujo triaje completo.
- Flujo registro diario.
- Cross-browser en Playwright.

**Herramientas**: Playwright.

### Manuales

- **Sesiones de feedback con voluntaria piloto** (2-3 durante desarrollo).
- **A11y testing** con NVDA + teclado.
- **Pentest** con OWASP ZAP antes de release.

### Datos de test

- **Seed script** (`scripts/seed.py`) con protectora ficticia, 5 animales, 20 registros, 3 triajes.
- **Fixtures** de pytest con datos conocidos.

### CI

- Tests obligatorios para merge a main.
- Tests E2E opcionales en PRs (más lentos).
- Coverage report en PR comments.

---

## 20. Métricas y analítica

### Métricas de producto (a trackear)

- **Adopción**: protectoras registradas, usuarias activas por protectora.
- **Engagement**: animales dados de alta / semana, registros / día, triajes / semana.
- **Calidad IA**:
  - Tasa de regeneración de fichas.
  - Tasa de edición manual de fichas.
  - Feedback cualitativo en entrevistas.
- **Retención**: % de protectoras que vuelven tras 1, 7, 30 días.
- **Errores**: tasa de error 5xx, latencia p95.

### Métricas de salud técnica

- Uptime (objetivo 99% en horario laboral).
- Latencia p50, p95, p99 de endpoints clave.
- Cobertura de tests.
- Vulnerabilidades abiertas (CodeQL, Snyk, Trivy).
- Tiempo medio de resolución de bugs.

### Métricas de IA específicas

- Tokens consumidos / mes (coste real vs free tier).
- Latencia de generación de fichas (p50, p95).
- Latencia de triaje.
- Tasa de falsos negativos altos en triaje (crítico ético).
- Distribución de niveles de urgencia en triajes.

### Cómo se trackean

- **Backend**: logs estructurados con `structlog` → stdout → Render.
- **Frontend**: errores JS a Sentry (opcional, free tier developer).
- **Uptime**: Healthchecks.io.
- **Negocios**: queries SQL a la DB (sin tracking de terceros, sin cookies analíticas).

### Anti-métricas (lo que NO medimos)

- **No Medimos con terceros**: Google Analytics, Hotjar, Mixpanel. Cero.
- **No usamos cookies de tracking**: solo cookies de sesión Supabase (esenciales).
- **No hacemos A/B testing invasivo**: si testeamos variantes, son cambios reversibles con feedback explícito de la voluntaria.

---

## 21. Riesgos y mitigaciones

### Riesgo 1: Groq cambia o limita su free tier

**Probabilidad**: Media.
**Impacto**: Alto.
**Mitigación**: capa de abstracción LLM, fallback a Gemini (también free), fallback a HF Inference. El cambio toma 1 hora de trabajo de código.

### Riesgo 2: Render free tier duerme el backend

**Probabilidad**: Alta.
**Impacto**: Bajo (acceptable para MVP).
**Mitigación**: Healthchecks.io ping cada 5 min para mantenerlo despierto (no abuse). Mensaje claro en UX: "primer load puede tardar unos segundos". Considerar upgrade a Render starter (7$/mes) si se vuelve problemático.

### Riesgo 3: Prompt injection en fichas/triaje

**Probabilidad**: Media.
**Impacto**: Medio-Alto (puede generar contenido inapropiado).
**Mitigación**: validación de outputs (regex de patrones prohibidos), sandboxing de prompts, disclaimers. Logs de prompts y respuestas para auditoría.

### Riesgo 4: Falsos negativos en triaje (urgencia alta clasificada como baja)

**Probabilidad**: Media.
**Impacto**: Crítico (ético: puede causar sufrimiento animal).
**Mitigación**: prompt conservador ("si dudas, clasifica más alto"), validación humana obligatoria antes de actuar, disclaimer explícito. Veterinario revisor en beta. Auditoría periódica de casos.

### Riesgo 5: Falta de datos para entrenar/fine-tunear CV veterinario

**Probabilidad**: Alta.
**Impacto**: Medio.
**Mitigación**: empezar con modelo pre-entrenado (CLIP), no prometer diagnóstico visual fino, usar el LLM con RAG más que el CV. Reconocer limitaciones públicamente.

### Riesgo 6: Protectora piloto abandona el proyecto

**Probabilidad**: Media.
**Impacto**: Alto (perdemos validación).
**Mitigación**: tener 2-3 protectoras en lista de espera, comunicación constante, valor real para la voluntaria (no solo pedirle tiempo).

### Riesgo 7: Burnout del desarrollador (yo)

**Probabilidad**: Media.
**Impacto**: Alto.
**Mitigación**: timeboxing estricto, MVP recortado de verdad, no añadir features "nice to have" en fase final. Sprints de 1 semana con objetivos claros. Descanso obligatorio.

### Riesgo 8: Supabase cambia free tier

**Probabilidad**: Baja.
**Impacto**: Alto.
**Mitigación**: código desacoplado de Supabase (SQLAlchemy), se puede migrar a Neon o RDS. Auth se puede migrar a Clerk o Auth0. Documentar la migración.

### Riesgo 9: Contenido generado por IA ofensivo o sesgado

**Probabilidad**: Media.
**Impacto**: Medio.
**Mitigación**: filtros de salida, revisión humana obligatoria antes de publicar fichas, logs de generaciones, posibilidad de reportar contenido problemático.

### Riesgo 10: Falta de adopción post-MVP

**Probabilidad**: Media.
**Impacto**: Alto (proyecto "muere").
**Mitigación**: validación con usuarias reales desde el inicio, onboarding impecable, comunidad open source, publicación activa, dogfooding (usar Maira yo mismo si tuviera protectora).

---

## 22. Preguntas abiertas

### A resolver durante desarrollo

1. **¿Modelo CV fine-tuneado o generalista?** — Empezar con CLIP, evaluar tras MVP. Decisión: fase 2.
2. **¿Multi-idioma en MVP?** — Decisión: no, solo español.
3. **¿Storage de backups dónde?** — Decisión: Supabase (incluido) + script a R2 manual.
4. **¿Auth magic link o password?** — Decisión: magic link (mejor UX para no técnicas).
5. **¿Telegram/WhatsApp como canal?** — Decisión: NO en MVP (mucho trabajo), sí en fase 2.
6. **¿Veterinario en el equipo?** — Decisión: contactar a uno en fase 1, advisor no coautor.
7. **¿Donaciones integradas?** — Decisión: NO en MVP.
8. **¿Multi-protectora en MVP?** — Decisión: no, solo 1 protectora, multi en fase 2.

### A resolver antes de release

1. ¿El LLM genera fichas con el tono adecuado para protectoras españolas? (validar con entrevistas)
2. ¿La clasificación de urgencia del triaje es suficientemente precisa? (validar con veterinario)
3. ¿La voluntaria es capaz de usar la app sin ayuda? (test con usuaria piloto)
4. ¿La auditoría A11y pasa Lighthouse > 90? (test automático)
5. ¿El pentest no encuentra vulnerabilidades críticas? (test manual)

### A resolver a largo plazo

1. ¿Es sostenible mantener Maira con comunidad open source?
2. ¿Cómo se financia la infraestructura si crece?
3. ¿Federación multi-protectora es el siguiente paso o nos centramos en profundizar el MVP?
4. ¿Cuándo lanzamos Elpis (app móvil)?

---

## 23. Glosario

- **Protectora**: asociación sin ánimo de lucro que rescata y busca hogar a animales abandonados.
- **Adoptante**: persona que quiere dar un hogar a un animal.
- **Ficha de adopción**: texto descriptivo del animal para presentar a adoptantes.
- **Triaje**: evaluación inicial de urgencia de un síntoma (NO diagnóstico).
- **Acogida**: familia temporal que cuida al animal hasta adopción definitiva.
- **LOPD/RGPD**: normativa de protección de datos (en España aplica RGPD).
- **MVP (Minimum Viable Product)**: versión mínima del producto con las funciones esenciales.
- **ADR (Architectural Decision Record)**: documento que captura una decisión técnica.
- **RLS (Row Level Security)**: seguridad a nivel de fila en PostgreSQL.
- **RAG (Retrieval Augmented Generation)**: técnica de LLM que combina búsqueda con generación.
- **A11y (Accessibility)**: accesibilidad web.
- **DevSecOps**: integración de seguridad en el ciclo de desarrollo.
- **WCAG (Web Content Accessibility Guidelines)**: estándar de accesibilidad W3C.

---

## 24. Apéndice A: convenciones de código

### Python (backend)

- **PEP 8** + **ruff** para estilo.
- **Type hints** obligatorios en funciones públicas.
- **Docstrings** estilo Google en funciones públicas.
- **Nombres**: `snake_case` para funciones/variables, `PascalCase` para clases.
- **Imports**: ordenados con `isort` (vía ruff).
- **Errores**: excepciones custom, no strings. Mensajes claros en español.
- **Async**: usar `async/await` por defecto en I/O.
- **Tests**: `pytest` con `arrange-act-assert`. Nombres `test_<funcionalidad>_<escenario>_<esperado>`.

### TypeScript (frontend)

- **TypeScript estricto**: `strict: true`, no `any` salvo justificado.
- **ESLint** + **Prettier** para estilo.
- **Componentes**: funcionales con hooks. Server Components por defecto en App Router.
- **Nombres**: `PascalCase` para componentes, `camelCase` para funciones/variables.
- **Props**: interface, no type. Exportadas solo si se reusan fuera.
- **Tests**: Vitest + Testing Library.

### Commits

- **Conventional Commits**:
  - `feat: añadir generación de ficha con IA`
  - `fix: corregir validación de email en signup`
  - `docs: actualizar README con instrucciones de deploy`
  - `refactor: extraer lógica de triaje a servicio`
  - `test: añadir tests para endpoint de animal`
  - `chore: actualizar dependencias`
- **Idioma**: español en mensajes de commit.
- **Branches**: `feat/...`, `fix/...`, `chore/...` (sin espacios, sin acentos).

### Pull Requests

- Título descriptivo (no "fix bug").
- Descripción con: qué cambia, por qué, cómo probarlo, capturas si hay UI.
- Vinculado a issue si existe.
- Review de al menos 1 persona (en MVP, auto-review con checklist).

---

## 25. Apéndice B: recursos y referencias

### Documentación oficial
- FastAPI: https://fastapi.tiangolo.com
- Next.js: https://nextjs.org/docs
- Supabase: https://supabase.com/docs
- Groq: https://console.groq.com/docs
- Qdrant: https://qdrant.tech/documentation
- HuggingFace: https://huggingface.co/docs
- WCAG 2.2: https://www.w3.org/WAI/standards-guidelines/wcag/

### Recursos de IA
- LangChain: https://python.langchain.com (considerar para RAG)
- LlamaIndex: alternativa a LangChain
- Sentence Transformers: para embeddings multilingües
- OpenCLIP: alternativa a CLIP de OpenAI

### Recursos veterinarios
- Manual Merck Veterinary: https://www.merckvetmanual.com
- AVEPA: https://www.avepa.org
- WSAVA: https://wsava.org

### Estándares y seguridad
- OWASP Top 10: https://owasp.org/Top10
- OWASP API Security: https://owasp.org/API-Security
- CIS Benchmarks: https://www.cisecurity.org/cis-benchmarks
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework

### Comunidad open source
- GitHub Open Source Guides: https://opensource.guide
- First Contributions: https://github.com/firstcontributions/first-contributions
- Choose a License: https://choosealicense.com

### Inspiración
- Shelterluv: https://www.shelterluv.com
- Petfinder: https://www.petfinder.com
- Adoptdontshop (la competencia open source): https://github.com/mouhurtik/adoptdontshop

---

## Historial de revisiones

| Fecha | Versión | Cambios |
|---|---|---|
| 2026-06-28 | 1.0 | Creación inicial del documento |

---

> Este documento es un ser vivo. Se actualizará con cada decisión, error, aprendizaje, y feedback de las voluntarias piloto. Si encuentras algo que mejorar, edita y commitea con `docs: ...`.

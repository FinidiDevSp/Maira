# Maira — Backlog (ideas y features NO incluidas en MVP)

> Documento vivo. Cosas que se nos ocurren que NO entran en el MVP pero que vale la pena tener registradas para fases futuras.
> Última revisión: 2026-06-28

---

## Cómo leer este documento

Cada entrada tiene:
- **Categoría** (funcional / técnica / comercial / comunidad).
- **Descripción** breve.
- **Por qué NO está en MVP** (justificación de descarte).
- **Cuándo recuperarla** (fase 2, fase 3, idea, no).
- **Esfuerzo estimado** (S/M/L/XL).
- **Valor estimado** (Bajo/Medio/Alto).

Si una idea te parece importante y quieres que entre en MVP, **debes justificar** por qué desplazaría a otra. El MVP es sagrado.

---

## Funcionalidades de producto

### B-001 · Federación multi-protectora

Varias protectoras en una sola instancia, con visión de red. Matching entre protectoras saturadas y con espacio.

- **Por qué no en MVP**: complejidad técnica (RLS multi-tenant, dashboards agregados, gobernanza de datos), añade 4-6 semanas de trabajo.
- **Cuándo**: fase 2 (post-MVP, tras validar con 1 protectora).
- **Esfuerzo**: XL.
- **Valor**: Alto (diferenciador real vs competencia).

### B-002 · Marketplace público de adopción

Web pública donde adoptantes ven animales de todas las protectoras federadas.

- **Por qué no en MVP**: es Elpis (la app móvil), no Maira. Maira es la herramienta interna de la protectora.
- **Cuándo**: fase 3 (Elpis).
- **Esfuerzo**: L.
- **Valor**: Alto.

### B-003 · Sistema de matching adoptante-animal

Quiz de compatibilidad (estilo de vida, hogar, experiencia) que recomienda animales concretos.

- **Por qué no en MVP**: requiere base de adoptantes (Elpis) y datos de comportamiento de animales. Prematuro.
- **Cuándo**: fase 3 (Elpis).
- **Esfuerzo**: L.
- **Valor**: Alto (reduce devoluciones).

### B-004 · Donaciones integradas

Pasarela de donación (Bizum, tarjeta, cripto) en la web pública de cada protectora.

- **Por qué no en MVP**: regulatory burden (PSD2, KYC), pasarelas de pago (Stripe cobra comisión), no es core del TFM.
- **Cuándo**: post-TFM, fase 3+.
- **Esfuerzo**: L.
- **Valor**: Alto.

### B-005 · Notificaciones a adoptantes (email/SMS/WhatsApp)

Cuando un animal que les gusta baja de precio, está en tratamiento, o es adoptado por otro.

- **Por qué no en MVP**: requiere base de adoptantes (Elpis).
- **Cuándo**: fase 3.
- **Esfuerzo**: M.
- **Valor**: Medio.

### B-006 · Chat interno protectora ↔ adoptante

Mensajería dentro de Maira para resolver dudas pre-adopción.

- **Por qué no en MVP**: complejidad (WebSockets, moderación, anti-spam), WhatsApp lo cubre mal que bien.
- **Cuándo**: fase 2-3.
- **Esfuerzo**: M.
- **Valor**: Medio.

### B-007 · Web pública personalizada por protectora

Cada protectora tiene su subdominio (`luna-refugio.maira.org`) con sus animales, su historia, su branding.

- **Por qué no en MVP**: no es core, mucha config multi-tenant.
- **Cuándo**: fase 2.
- **Esfuerzo**: L.
- **Valor**: Alto (visibilidad pública).

### B-008 · Multi-idioma (catalán, euskera, gallego, portugués)

i18n completo, no solo traducción de UI sino también de los prompts del LLM.

- **Por qué no en MVP**: añadiría 3-4 semanas solo de localización + testing con usuarios nativos.
- **Cuándo**: fase 2 (catalán, euskera, gallego por cercanía), fase 3 (portugués por mercado).
- **Esfuerzo**: L.
- **Valor**: Alto (mercado real en España).

### B-009 · Integración con chips de identificación

Leer el chip NFC del animal y auto-rellenar datos del registro (nombre del antiguo dueño si está en base de datos).

- **Por qué no en MVP**: requiere hardware NFC compatible, acceso a base de datos de chips (REIAC en España, no público), baja adopción por protectoras pequeñas.
- **Cuándo**: idea, evaluar en 1-2 años.
- **Esfuerzo**: L.
- **Valor**: Bajo (pocos casos de uso real).

### B-010 · Reconocimiento de raza por foto

CV que identifica la raza probable del animal a partir de la foto.

- **Por qué no en MVP**: baja precisión en mestizos, no es crítico, podría dar información sesgada.
- **Cuándo**: idea, no.
- **Esfuerzo**: M.
- **Valor**: Bajo.

### B-011 · Calendario de eventos (vacunas, desparasitaciones, citas vete)

Vista de calendario con próximos eventos por animal y por protectora.

- **Por qué no en MVP**: se puede hacer con el módulo de eventos de salud (futuro), pero MVP tiene suficientes críticos.
- **Cuándo**: fase 2.
- **Esfuerzo**: M.
- **Valor**: Medio.

### B-012 · Recordatorios automáticos (peso cada 30 días, vacunas, etc.)

Push/email a la voluntaria: "Luna no se ha pesado en 25 días, toca pesarla".

- **Por qué no en MVP**: requiere configurar reglas por animal/protección, validación. MVP usa el timeline.
- **Cuándo**: fase 2.
- **Esfuerzo**: M.
- **Valor**: Medio.

### B-013 · Exportación a formato estándar (Petlink, Triana, etc.)

Las protectoras grandes usan software propietario. Exportar a esos formatos permite migración futura.

- **Por qué no en MVP**: complejo, documentación a veces cerrada.
- **Cuándo**: idea.
- **Esfuerzo**: L.
- **Valor**: Bajo.

### B-014 · Integración con redes sociales (autopublicar en Instagram, Facebook)

Cuando un animal es dado de alta o se genera una ficha, publicar automáticamente.

- **Por qué no en MVP**: APIs de Meta son restrictivas, requiere app review, no es core.
- **Cuándo**: fase 3.
- **Esfuerzo**: M.
- **Valor**: Medio.

### B-015 · Tests psicométricos para adoptantes

Cuestionario serio pre-adopción (estilo ASPCA) integrado en Maira o Elpis.

- **Por qué no en MVP**: requiere validación con expertos en comportamiento animal, mucho trabajo de UX.
- **Cuándo**: fase 3.
- **Esfuerzo**: L.
- **Valor**: Alto (reduce devoluciones).

### B-016 · Veterinario en el equipo (asesor técnico)

Un veterinario real que valida los prompts, los outputs del triaje, y firma como advisor.

- **Por qué no en MVP**: decisión de scope del TFM, no de funcionalidad. Pero es importante.
- **Cuándo**: ahora, antes de release.
- **Esfuerzo**: networking.
- **Valor**: Crítico (credibilidad).

### B-017 · Programa de ambassadors

Voluntarias de protectoras que ayudan a otras protectoras a adoptar Maira.

- **Por qué no en MVP**: requiere base instalada.
- **Cuándo**: fase 2-3.
- **Esfuerzo**: M (con comunidad).
- **Valor**: Alto (crecimiento orgánico).

### B-018 · Foro / comunidad de voluntarias

Espacio donde las voluntarias comparten tips, fotos, experiencias. Tipo Discord embebido o Mattermost.

- **Por qué no en MVP**: requiere moderación, mucho trabajo de comunidad.
- **Cuándo**: fase 2-3.
- **Esfuerzo**: L.
- **Valor**: Medio.

### B-019 · Versión nativa móvil (React Native)

App nativa para que la voluntaria registre desde el móvil sin abrir el navegador.

- **Por qué no en MVP**: web responsive cubre el 80% de los casos. MVP no necesita.
- **Cuándo**: fase 2-3.
- **Esfuerzo**: L.
- **Valor**: Medio-Alto.

### B-020 · Modo offline (PWA con service worker)

Maira usable sin conexión, sincroniza cuando vuelve online.

- **Por qué no en MVP**: las protectoras pequeñas tienen cobertura, no es crítico.
- **Cuándo**: fase 3, si hay demanda.
- **Esfuerzo**: M.
- **Valor**: Bajo-Medio.

### B-021 · Reportes automáticos mensuales

PDF/email automático cada mes con métricas, animales adoptados, tendencias, etc.

- **Por qué no en MVP**: se puede generar manualmente desde el dashboard en MVP.
- **Cuándo**: fase 2.
- **Esfuerzo**: M.
- **Valor**: Medio.

### B-022 · Backup y restauración self-service

La voluntaria puede descargar backup completo de su protectora en cualquier momento.

- **Por qué no en MVP**: Supabase ya hace backups automáticos. La voluntaria no necesita.
- **Cuándo**: fase 3.
- **Esfuerzo**: S.
- **Valor**: Bajo.

### B-023 · Multi-tenant con base de datos por protectora

En lugar de RLS, una DB por protectora. Más aislamiento, más coste.

- **Por qué no en MVP**: over-engineering. RLS es suficiente.
- **Cuándo**: nunca, probablemente.
- **Esfuerzo**: L.
- **Valor**: Bajo.

### B-024 · App progresiva (PWA instalable)

Que la voluntaria pueda "instalar" Maira en su móvil como app.

- **Por qué no en MVP**: web ya es responsive. PWA es nice-to-have.
- **Cuándo**: fase 2.
- **Esfuerzo**: S.
- **Valor**: Bajo-Medio.

### B-025 · Sincronización con veterinaria externa

Si la protectora tiene un vete de confianza, que el vete pueda ver el historial del animal desde su propio sistema.

- **Por qué no en MVP**: requiere API de vete, raro que lo tengan.
- **Cuándo**: idea, no.
- **Esfuerzo**: XL.
- **Valor**: Bajo.

### B-026 · Reconocimiento emocional del animal por foto

CV que detecta si el animal parece triste, ansioso, relajado en la foto.

- **Por qué no en MVP**: baja precisión en animales, modelo no maduro.
- **Cuándo**: idea, evaluar en 1-2 años.
- **Esfuerzo**: M.
- **Valor**: Bajo.

### B-027 · Seguimiento post-adopción

Email/WhatsApp automático al adoptante: "¿Cómo está X a la semana, al mes, a los 3 meses, al año?".

- **Por qué no en MVP**: requiere Elpis.
- **Cuándo**: fase 3.
- **Esfuerzo**: M.
- **Valor**: Alto (datos valiosos, reduce devoluciones).

### B-028 · Casos clínicos exportables (anonimizados) para investigación veterinaria

Con consentimiento de las protectoras, compartir datos anonimizados con universidades o veterinarios investigadores.

- **Por qué no en MVP**: requiere base legal, anonimización robusta, partnerships.
- **Cuándo**: fase 3+, si surge oportunidad.
- **Esfuerzo**: M.
- **Valor**: Medio-Alto (impacto social y científico).

### B-029 · Integración con TPV / caja registradora de la protectora

Las protectoras que venden merchandising o hacen eventos pueden tener caja. Integración con Maira.

- **Por qué no en MVP**: no es nuestro foco.
- **Cuándo**: nunca, probablemente.
- **Esfuerzo**: L.
- **Valor**: Bajo.

### B-030 · Webhooks para integraciones externas

Para que otros sistemas (ej. software de contabilidad) se enteren de eventos en Maira.

- **Por qué no en MVP**: nadie lo va a usar aún.
- **Cuándo**: fase 3+.
- **Esfuerzo**: M.
- **Valor**: Bajo.

### B-031 · Dashboard de impacto (animales salvados por protectora, métricas globales)

Para que la protectora pueda mostrar a sus donantes "hemos salvado 50 animales este año".

- **Por qué no en MVP**: requiere datos longitudinales.
- **Cuándo**: fase 3.
- **Esfuerzo**: M.
- **Valor**: Medio-Alto.

### B-032 · Programa de Padrinos/Mecenas

Permitir a particulares "apadrinar" un animal concreto (pago mensual para sus cuidados).

- **Por qué no en MVP**: regulatory + pasarela de pago.
- **Cuándo**: fase 3+.
- **Esfuerzo**: L.
- **Valor**: Alto.

### B-033 · Acogidas temporales (fostering) como entidad separada

Las familias de acogida no son adoptantes, son temporales. Modelo distinto.

- **Por qué no en MVP**: MVP cubre solo estancia en protectora.
- **Cuándo**: fase 2.
- **Esfuerzo**: M.
- **Valor**: Medio.

### B-034 · Galería pública de "finales felices"

Historias de animales adoptados con fotos antes/después.

- **Por qué no en MVP**: requiere flujo de seguimiento post-adopción.
- **Cuándo**: fase 3.
- **Esfuerzo**: M.
- **Valor**: Alto (marketing emocional para protectoras).

### B-035 · Generación de vídeo con la ficha del animal

Mini-vídeo de 30s con fotos del animal, texto y música. Para redes sociales.

- **Por qué no en MVP**: requiere generación de vídeo (caro, lento).
- **Cuándo**: fase 3.
- **Esfuerzo**: M.
- **Valor**: Medio-Alto.

### B-036 · Whitelabel para una protectora grande

Una protectora con dinero paga por tener Maira con su marca.

- **Por qué no en MVP**: rompe el principio open source puro.
- **Cuándo**: nunca, probablemente. Si quieren, que usen la versión open.
- **Esfuerzo**: M.
- **Valor**: Medio (comercial, dudoso éticamente).

### B-037 · Marketplace de servicios para protectoras

Las protectoras pueden contratar veterinarios, abogados, diseñadores a través de Maira.

- **Por qué no en MVP**: no es nuestro foco, regulatory heavy.
- **Cuándo**: nunca, probablemente.
- **Esfuerzo**: XL.
- **Valor**: Bajo (problemas legales).

### B-038 · Integración con cartillas veterinarias digitales (CVIVET, etc.)

Sincronizar el historial de salud con cartillas oficiales.

- **Por qué no en MVP**: requiere partnerships oficiales, APIs cerradas.
- **Cuándo**: idea.
- **Esfuerzo**: L.
- **Valor**: Bajo-Medio.

### B-039 · Asistente de redacción de solicitudes de subvención

LLM que ayuda a escribir solicitudes de subvención para protectoras (contexto: convocatoria X, importe Y).

- **Por qué no en MVP**: es una feature entera, requiere mucho RAG sobre convocatorias.
- **Cuándo**: fase 3, si surge demanda.
- **Esfuerzo**: L.
- **Valor**: Alto (muchas protectoras lo necesitan).

### B-040 · Sistema de reputación / reviews de protectoras

Para que adoptantes valoren a las protectoras tras la adopción.

- **Por qué no en MVP**: no es core, y las protectoras pequeñas temen ser Juzgadas.
- **Cuándo**: nunca, probablemente.
- **Esfuerzo**: M.
- **Valor**: Bajo.

### B-041 · "Maira Academy" — cursos online para voluntarias

Formación en cuidado animal, primeros auxilios, etc.

- **Por qué no en MVP**: no es nuestro foco.
- **Cuándo**: idea, no.
- **Esfuerzo**: XL.
- **Valor**: Bajo (hay otros actores).

### B-042 · Integración con básculas inteligentes

Si la protectora tiene una báscula IoT, que los datos se vuelquen automáticamente.

- **Por qué no en MVP**: requiere hardware.
- **Cuándo**: nunca.
- **Esfuerzo**: L.
- **Valor**: Bajo.

### B-043 · Análisis de sentimientos en notas libres

LLM que detecta preocupación, alegría, agotamiento en las notas de las voluntarias.

- **Por qué no en MVP**: complejidad + privacidad.
- **Cuándo**: fase 3.
- **Esfuerzo**: M.
- **Valor**: Bajo (puede ser invasivo).

### B-044 · Generador de emails para campañas de sensibilización

"Email a medios sobre el caso de Luna" con datos clave.

- **Por qué no en MVP**: es B-019 (Brief Express) de otro proyecto, no core.
- **Cuándo**: idea.
- **Esfuerzo**: M.
- **Valor**: Medio.

### B-045 · Chatbot 24/7 para responder preguntas frecuentes de adoptantes

"¿Cuánto cuesta adoptar? ¿Puedo adoptar si vivo de alquiler? ¿Tenéis gatos con X?"

- **Por qué no en MVP**: requiere Elpis o web pública.
- **Cuándo**: fase 3.
- **Esfuerzo**: M.
- **Valor**: Medio.

### B-046 · Soporte multiidioma en la generación de fichas

Que la protectora pueda generar la ficha en español + inglés para llegar a más adoptantes.

- **Por qué no en MVP**: requiere multi-idioma en prompts.
- **Cuándo**: fase 2-3.
- **Esfuerzo**: M.
- **Valor**: Alto (mercado expats).

### B-047 · Reconocimiento de microchip por NFC móvil

Leer microchip con el móvil de la voluntaria (ya hay apps que lo hacen).

- **Por qué no en MVP**: depende de hardware, baja adopción.
- **Cuándo**: idea.
- **Esfuerzo**: M.
- **Valor**: Bajo.

### B-048 · Sincronización offline de fotos

La voluntaria hace fotos en el refugio (sin cobertura) y se suben cuando vuelve.

- **Por qué no en MVP**: requiere service worker, gestión de colas.
- **Cuándo**: fase 2.
- **Esfuerzo**: M.
- **Valor**: Medio.

### B-049 · Modo "kata" para tests de la voluntaria

Gamificación: la voluntaria gana puntos por usar Maira consistentemente.

- **Por qué no en MVP**: puede sentirse manipulador, no es core.
- **Cuándo**: nunca, probablemente.
- **Esfuerzo**: M.
- **Valor**: Bajo.

### B-050 · Integración con SIAC (Sistema de Identificación de Animales de Compañía)

Registro oficial español de animales. Sincronizar con Maira.

- **Por qué no en MVP**: API no pública, regulatory.
- **Cuándo**: idea, no.
- **Esfuerzo**: L.
- **Valor**: Bajo.

### B-051 · Versión "light" para particulares con camadas no deseadas

Persona que tiene una camada en casa y busca dar los cachorros en adopción. Versión simplificada.

- **Por qué no en MVP**: regulatory + scope creep. No es nuestro target.
- **Cuándo**: nunca.
- **Esfuerzo**: L.
- **Valor**: Bajo.

### B-052 · Generación de contratos de adopción

PDF firmado digitalmente entre protectora y adoptante.

- **Por qué no en MVP**: regulatory + no es core de Maira.
- **Cuándo**: fase 3 (Elpis).
- **Esfuerzo**: M.
- **Valor**: Alto.

### B-053 · Sello "Maira Verified" para protectoras

Distintivo en la ficha del animal: "esta protectora usa Maira para cuidar a sus animales".

- **Por qué no en MVP**: marketing, fase post-MVP.
- **Cuándo**: fase 2.
- **Esfuerzo**: S.
- **Valor**: Medio.

### B-054 · Integración con el chip de geolocalización (Tractive, etc.)

Para que la protectora pueda ver dónde está un animal (post-adopción).

- **Por qué no en MVP**: integración con terceros, post-adopción.
- **Cuándo**: fase 3+.
- **Esfuerzo**: M.
- **Valor**: Bajo (invasivo).

### B-055 · IA que sugiere el "match" entre protectoras para traslados

"Si tienes 30 animales y 5 espacios libres, podríamos enviarte 3 de la protectora X".

- **Por qué no en MVP**: requiere multi-protectora (fase 2).
- **Cuándo**: fase 2-3.
- **Esfuerzo**: M.
- **Valor**: Alto.

### B-056 · Modo de auditoría para inspectors de sanidad

Cuando un inspector viene, la protectora le da acceso temporal a ver todos los registros sanitarios.

- **Por qué no en MVP**: no es core.
- **Cuándo**: idea.
- **Esfuerzo**: S.
- **Valor**: Bajo.

### B-057 · Versión imprimible de la ficha para tablón del refugio

PDF A4 con foto grande, datos y QR al perfil completo.

- **Por qué no en MVP**: nice-to-have.
- **Cuándo**: fase 2.
- **Esfuerzo**: S.
- **Valor**: Medio.

### B-058 · Memoria anual de la protectora generada por IA

Informe anual bonito con estadísticas, historias, fotos, generado por LLM.

- **Por qué no en MVP**: requiere datos longitudinales.
- **Cuándo**: fase 3.
- **Esfuerzo**: M.
- **Valor**: Alto (transparencia, donantes).

### B-059 · Bot de Telegram para consultas rápidas de la voluntaria

"@MairaBot ¿cuántos animales tengo en tratamiento?".

- **Por qué no en MVP**: requiere integración.
- **Cuándo**: fase 2.
- **Esfuerzo**: M.
- **Valor**: Medio.

### B-060 · Modo "compras" para gastos de la protectora

Registro de gastos (comida, vete, material) con categorías y reporte.

- **Por qué no en MVP**: no es core, hay apps específicas.
- **Cuándo**: nunca, probablemente.
- **Esfuerzo**: M.
- **Valor**: Bajo.

### B-061 · IA que detecta anomalías administrativas

"Si llevas 3 meses sin entrar a registrar a Fido, ¿está bien?".

- **Por qué no en MVP**: ya hay alertas de "sin registro en 3 días" en MVP. Versión más amplia = fase 2.
- **Cuándo**: fase 2.
- **Esfuerzo**: S.
- **Valor**: Bajo.

### B-062 · Marketplace de servicios veterinarios con descuento

Las protectoras podrían acceder a vetes colaboradores con descuento a través de Maira.

- **Por qué no en MVP**: regulatory +商业模式.
- **Cuándo**: nunca, probablemente.
- **Esfuerzo**: L.
- **Valor**: Medio (comercial, dudoso éticamente).

### B-063 · Sistema de "ángeles" — padrinos anónimos

Donantes recurrentes pequeños (5€/mes) que reciben updates de un animal concreto.

- **Por qué no en MVP**: regulatory + pasarela.
- **Cuándo**: fase 3.
- **Esfuerzo**: L.
- **Valor**: Alto.

### B-064 · Integración con plataformas de crowdfunding (GoFundMe, Kickstarter)

Para campañas específicas ("Luna necesita operación de X euros").

- **Por qué no en MVP**: no es core.
- **Cuándo**: nunca.
- **Esfuerzo**: S.
- **Valor**: Bajo.

### B-065 · Programa de voluntariado corporativo

Empresas que quieren que sus empleados sean voluntarios. Matching empresa-protección.

- **Por qué no en MVP**: no es nuestro foco.
- **Cuándo**: idea.
- **Esfuerzo**: L.
- **Valor**: Bajo (hay plataformas específicas).

---

## Técnicas / Infraestructura

### T-001 · Migración de Groq a self-hosted LLM

Si los costes crecen, mover el LLM a una instancia propia (RunPod, Lambda Labs, etc.).

- **Cuándo**: si llegamos a >100k generaciones/mes.
- **Esfuerzo**: M.
- **Valor**: Bajo (probablemente no lleguemos).

### T-002 · Cache agresivo de fichas generadas

Para animales similares, no regenerar, reutilizar.

- **Cuándo**: fase 2.
- **Esfuerzo**: S.
- **Valor**: Medio (ahorro de costes).

### T-003 · Fine-tune de Llama 3.1 8B con datos propios

Si tenemos >1000 fichas validadas, entrenar un modelo específico.

- **Cuándo**: fase 3, post-TFM.
- **Esfuerzo**: M.
- **Valor**: Medio (calidad mejora).

### T-004 · Migrar de Render a Railway o Fly.io

Si Render free tier es problemático.

- **Cuándo**: si es necesario.
- **Esfuerzo**: S.
- **Valor**: Bajo.

### T-005 · Implementar GraphQL en lugar de REST

Para queries más flexibles desde Elpis.

- **Cuándo**: fase 3.
- **Esfuerzo**: M.
- **Valor**: Bajo.

### T-006 · CDN para fotos (Cloudflare Images)

Si las fotos se sirven lento.

- **Cuándo**: si surge problema de rendimiento.
- **Esfuerzo**: S.
- **Valor**: Medio.

### T-007 · Migración a Postgres nativo (sin Supabase)

Si necesitamos features específicas de Postgres que Supabase no expone.

- **Cuándo**: improbable.
- **Esfuerzo**: L.
- **Valor**: Bajo.

### T-008 · Implementar OpenTelemetry

Para tracing distribuido backend + frontend.

- **Cuándo**: fase 2-3.
- **Esfuerzo**: M.
- **Valor**: Medio.

### T-009 · Rate limiting por usuaria (no por IP)

Para evitar abuso sin bloquear oficinas共享 IP.

- **Cuándo**: fase 2.
- **Esfuerzo**: S.
- **Valor**: Medio.

### T-010 · Background jobs con Celery o Arq

Para tareas lentas (generación de ficha, triaje).

- **Cuándo**: fase 2.
- **Esfuerzo**: M.
- **Valor**: Medio.

### T-011 · WebSockets para updates en tiempo real del dashboard

"Animal dado de alta en protectora X" en vivo.

- **Cuándo**: fase 3.
- **Esfuerzo**: M.
- **Valor**: Bajo.

### T-012 · Búsqueda full-text con Meilisearch o Typesense

Si la búsqueda por nombre se queda corta.

- **Cuándo**: fase 2.
- **Esfuerzo**: S.
- **Valor**: Medio.

### T-013 · CI/CD con auto-deploy por environment (dev/staging/prod)

Para no deployar a producción sin pasar por staging.

- **Cuándo**: fase 2.
- **Esfuerzo**: S.
- **Valor**: Medio.

### T-014 · Feature flags con Unleash o LaunchDarkly

Para rollout gradual de features.

- **Cuándo**: fase 2.
- **Esfuerzo**: S.
- **Valor**: Bajo.

### T-015 · Observabilidad con Grafana + Prometheus (gratis)

Si queremos dashboards potentes.

- **Cuándo**: fase 2-3.
- **Esfuerzo**: M.
- **Valor**: Medio.

### T-016 · Migración a Astro o Remix si Next.js se queda corto

Improbable pero registrado.

- **Cuándo**: nunca, probablemente.
- **Esfuerzo**: L.
- **Valor**: Bajo.

### T-017 · Edge functions (Cloudflare Workers, Vercel Edge)

Para latencia ultra baja en el futuro.

- **Cuándo**: fase 3+.
- **Esfuerzo**: M.
- **Valor**: Bajo.

### T-018 · MLflow para tracking de experimentos de prompts

Si hacemos A/B de prompts del LLM.

- **Cuándo**: fase 2.
- **Esfuerzo**: M.
- **Valor**: Medio.

### T-019 · Vector DB propio (Chroma embedded) en lugar de Qdrant

Si Qdrant free tier se queda corto.

- **Cuándo**: si es necesario.
- **Esfuerzo**: S.
- **Valor**: Bajo.

### T-020 · CDN de librerías JS (jsdelivr, unpkg) self-hosted

Si queremos más control.

- **Cuándo**: nunca.
- **Esfuerzo**: S.
- **Valor**: Bajo.

---

## Comerciales / Comunidad

### C-001 · Landing page pública

Web bonita explicando el proyecto, captando voluntarias-piloto, mostrando métricas de impacto.

- **Cuándo**: ahora (antes de MVP, para validar).
- **Esfuerzo**: S.
- **Valor**: Alto.

### C-002 · Documentación de usuario (help center)

Artículos cortos: "Cómo dar de alta un animal", "Cómo generar una ficha", etc.

- **Cuándo**: pre-release.
- **Esfuerzo**: M.
- **Valor**: Alto (reduce soporte).

### C-003 · Vídeos tutoriales cortos (1-2 min)

Para YouTube o embebidos en la app.

- **Cuándo**: post-MVP.
- **Esfuerzo**: M.
- **Valor**: Alto (las voluntarias mayores prefieren vídeo).

### C-004 · Blog técnico (qué decisiones tomamos, qué aprendimos)

Para SEO, credibilidad, reclutamiento.

- **Cuándo**: paralelo al desarrollo.
- **Esfuerzo**: S (escribir durante el proceso).
- **Valor**: Alto.

### C-005 · Conferencias y meetups (charlas sobre el proyecto)

Visibilidad, networking, feedback.

- **Cuándo**: post-MVP.
- **Esfuerzo**: S (por charla).
- **Valor**: Alto.

### C-006 · Programa "Maira para tu protectora" (formulario de solicitud)

Para que protectoras se apunten como beta testers.

- **Cuándo**: pre-MVP.
- **Esfuerzo**: S.
- **Valor**: Alto.

### C-007 · Partnerships con asociaciones de protectoras (FAADA, ANAA, etc.)

Para distribución y credibilidad.

- **Cuándo**: pre-MVP.
- **Esfuerzo**: networking.
- **Valor**: Alto.

### C-008 · Press kit y notas de prensa

Para lanzamientos y milestones.

- **Cuándo**: cada hito.
- **Esfuerzo**: S.
- **Valor**: Medio.

### C-009 · Newsletter mensual a protectoras y simpatizantes

Updates, tips, casos de éxito.

- **Cuándo**: post-MVP.
- **Esfuerzo**: S.
- **Valor**: Medio.

### C-010 · Política de privacidad detallada y cumplimiento RGPD

Texto legal serio, con DPO si crece.

- **Cuándo**: pre-MVP.
- **Esfuerzo**: S.
- **Valor**: Crítico (legal).

### C-011 · Términos de servicio claros

- **Cuándo**: pre-MVP.
- **Esfuerzo**: S.
- **Valor**: Crítico.

### C-012 · Trademark del nombre y logo

Proteger la marca si crece.

- **Cuándo**: si crece.
- **Esfuerzo**: M (legal).
- **Valor**: Bajo-Medio.

### C-013 · Becas / grants open source (GitHub Sponsors, Open Collective, etc.)

Para sostenibilidad financiera.

- **Cuándo**: post-MVP si hay tracción.
- **Esfuerzo**: S.
- **Valor**: Medio (sostenibilidad).

### C-014 · Sponsors corporativos

Empresas de pet food, veterinarias, etc. que patrocinen el proyecto.

- **Cuándo**: post-MVP si hay tracción.
- **Esfuerzo**: M (relaciones).
- **Valor**: Alto (sostenibilidad).

### C-015 · Modelo "freemium" ético

Funcionalidades extra para protectoras que donan mensualmente.

- **Cuándo**: nunca, probablemente (rompe open source puro).
- **Esfuerzo**: M.
- **Valor**: Dudoso éticamente.

### C-016 · Governance model (BDFL, foundation, coop)

Definir cómo se toman decisiones cuando hay múltiples contribuidores.

- **Cuándo**: post-MVP.
- **Esfuerzo**: M.
- **Valor**: Alto (sostenibilidad open source).

### C-017 · Código de conducta

Para la comunidad.

- **Cuándo**: ahora.
- **Esfuerzo**: S.
- **Valor**: Alto.

### C-018 · Contributing guide

Cómo contribuir, estilo, proceso de PR.

- **Cuándo**: ahora.
- **Esfuerzo**: S.
- **Valor**: Alto.

### C-019 · Templates de issues y PRs

Para facilitar contribución.

- **Cuándo**: ahora.
- **Esfuerzo**: S.
- **Valor**: Medio.

### C-020 · Discord / Matrix / Element para la comunidad

Para devs y usuarias avanzadas.

- **Cuándo**: post-MVP.
- **Esfuerzo**: S.
- **Valor**: Medio.

### C-021 · Roadmap público (GitHub Projects)

Para que cualquiera vea qué viene.

- **Cuándo**: ahora.
- **Esfuerzo**: S.
- **Valor**: Alto (transparencia).

### C-022 · Changelog público

Cada release documentada.

- **Cuándo**: ahora.
- **Esfuerzo**: S.
- **Valor**: Alto.

### C-023 · Programa de traducciones (Crowdin, Weblate)

Para multi-idioma.

- **Cuándo**: fase 2-3.
- **Esfuerzo**: M.
- **Valor**: Alto.

### C-024 · "Maira Stories" — entrevistas a protectoras

Contenido emocional para marketing.

- **Cuándo**: post-MVP.
- **Esfuerzo**: S (contenido).
- **Valor**: Alto.

### C-025 · Annual report de impacto

Qué cambió en el mundo animal gracias a Maira.

- **Cuándo**: cada año.
- **Esfuerzo**: M.
- **Valor**: Alto (transparencia, donors).

### C-026 · Encuesta anual a usuarias

Para mejorar el producto.

- **Cuándo**: cada año.
- **Esfuerzo**: S.
- **Valor**: Alto.

### C-027 · Integración con universidades (TFG, TFM, prácticas)

Atraer estudiantes que quieran contribuir.

- **Cuándo**: pre-MVP.
- **Esfuerzo**: S.
- **Valor**: Alto (mano de obra gratis + impacto).

### C-028 · Contacto con Cátedras de ética de IA

Para revisión ética del proyecto (especialmente el triaje).

- **Cuándo**: pre-MVP.
- **Esfuerzo**: networking.
- **Valor**: Alto (credibilidad).

### C-029 · Adhesión a Open Source Initiative o similar

Certificación de proyecto open source serio.

- **Cuándo**: post-MVP.
- **Esfuerzo**: S.
- **Valor**: Medio.

### C-030 · Logo y branding profesional

Diseñador/a que done un logo, manual de marca, etc.

- **Cuándo**: ahora.
- **Esfuerzo**: S (outreach).
- **Valor**: Alto (apariencia profesional).

---

## Notas finales

- Este backlog es vivo. Si una idea sube de prioridad, se mueve a "MVP futuro".
- Si una idea baja de prioridad, se mueve a "descartada" o se elimina.
- Cada idea tiene un **esfuerzo** y un **valor** estimados. La matriz esfuerzo/valor guía qué hacer primero en cada fase.
- El backlog NO es una lista de cosas a hacer. Es un registro para no olvidar ideas y priorizarlas conscientemente.

> "Lo perfecto es enemigo de lo bueno. El MVP es lo bueno. El backlog es lo perfecto. Y lo perfecto no llega nunca."

# Sistema documental

Cómo se organiza, quién escribe qué, y qué se genera solo.

## Mapa

```
docs/
├── index.md                 Portada del sitio MkDocs
├── product/                 QUÉ es el producto (negocio/analista entra por aquí)
│   └── PRODUCT_CONTEXT.md   ← hub raíz: empieza aquí
├── technical/               CÓMO está hecho (arquitectura, datos, API, diseño, ADRs)
├── planning/                DÓNDE estamos (backlog, roadmap, changelog, items/)
├── operations/              CÓMO se opera (setup, entorno, deploy, runbooks, seguridad)
└── meta/                    Transversal (testing, privacidad, este doc)

Raíz del repo: README, CLAUDE.md, AGENTS.md, CONTRIBUTING, SECURITY, LICENSE
             + ANALYSIS.md (biblia original) y BACKLOG.md (archivo de ideas post-MVP)
```

## El flujo de items (única fuente de verdad)

1. **Un item = un fichero** `docs/planning/items/<ID>.md` (`FEATURE-NNN`, `BUG-NNN`, `IMPROVEMENT-NNN`), creado copiando `_TEMPLATE.md`.
2. Estados: `recibido → analisis → diseno → listo → desarrollo → bloqueado → hecho → descartado`.
3. **Las vistas se renderizan, no se editan:** `python scripts/render_planning.py` regenera las zonas `<!-- RENDER -->` de BACKLOG, ROADMAP y el catálogo de PRODUCT_CONTEXT, y reescribe `items/INDEX.md`. CI falla si las vistas no están al día.
4. Un item entra en el ROADMAP solo cuando se le asigna `hito` (al promoverlo).
5. La **pasarela ChatGPT** ([CHATGPT_GATEWAY](../planning/CHATGPT_GATEWAY.md)) permite al analista capturar items desde ChatGPT: solo toca `items/`, nunca las vistas.

## Quién escribe qué

| Documento | Escribe | Cuándo |
|---|---|---|
| Items (captura) | Analista / pasarela ChatGPT / cualquiera | Al surgir la necesidad |
| Items (plan técnico) | **Deanna** (planificadora SDD) | Al promover a desarrollo |
| Vistas (BACKLOG/ROADMAP/catálogo) | `render_planning.py` — **nadie a mano** | `make render-planning` |
| Bloque "📍 Estado actual" y narrativa de hitos | **Milton** (memoria/docs) | Al cerrar cada tarea |
| CHANGELOG, ADRs nuevos | **Milton** / quien tome la decisión | Al cerrar tarea / decidir |
| Runbooks, docs técnicos | Quien opere/desarrolle | Cuando la realidad cambie |

## Convenciones

- Todo en **español**, lenguaje llano en `product/`, técnico donde toque.
- Documentos vivos: si el código contradice al doc, se corrige el doc en el mismo PR/commit.
- Enlaces relativos entre docs; `ANALYSIS.md` es la referencia extendida y **manda en caso de conflicto** de producto.
- El sitio se publica con MkDocs Material: `make docs-serve` en local.

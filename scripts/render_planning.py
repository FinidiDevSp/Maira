#!/usr/bin/env python3
"""Render determinista de la planificación de Maira.

Lee docs/planning/items/*.md (única fuente de verdad) y regenera las zonas
marcadas con <!-- RENDER:START --> / <!-- RENDER:END --> de:
  - docs/planning/BACKLOG.md   (items abiertos agrupados por estado)
  - docs/planning/ROADMAP.md   (hitos con items, % de progreso)
  - docs/product/PRODUCT_CONTEXT.md (catálogo de features en lenguaje usuario)
  - docs/planning/items/INDEX.md (índice completo, se reescribe entero)

Solo stdlib. Idempotente: misma carpeta de items => mismo output.
Uso: python scripts/render_planning.py
"""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ITEMS_DIR = ROOT / "docs" / "planning" / "items"
BACKLOG = ROOT / "docs" / "planning" / "BACKLOG.md"
ROADMAP = ROOT / "docs" / "planning" / "ROADMAP.md"
PRODUCT = ROOT / "docs" / "product" / "PRODUCT_CONTEXT.md"
INDEX = ITEMS_DIR / "INDEX.md"

ESTADOS_ABIERTOS = ["desarrollo", "bloqueado", "listo", "diseno", "analisis", "recibido"]
ETIQUETA_ESTADO = {
    "recibido": "📥 Recibido",
    "analisis": "🔍 En análisis",
    "diseno": "📐 En diseño",
    "listo": "🟢 Listo para desarrollo",
    "desarrollo": "🔨 En desarrollo",
    "bloqueado": "⛔ Bloqueado",
    "hecho": "✅ Hecho",
    "descartado": "🗑️ Descartado",
}
PRIORIDAD_ORDEN = {"alta": 0, "media": 1, "baja": 2}


def parse_frontmatter(text: str) -> dict[str, str]:
    """Parsea el frontmatter YAML plano (clave: valor) sin dependencias."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}
    meta: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" not in line or line.strip().startswith("#"):
            continue
        key, _, value = line.partition(":")
        value = value.strip().strip('"').strip("'")
        meta[key.strip()] = value
    return meta


def load_items() -> list[dict[str, str]]:
    items = []
    for path in sorted(ITEMS_DIR.glob("*.md")):
        if path.name in ("_TEMPLATE.md", "INDEX.md"):
            continue
        meta = parse_frontmatter(path.read_text(encoding="utf-8"))
        if not meta.get("id"):
            print(f"AVISO: {path.name} sin frontmatter valido, se ignora", file=sys.stderr)
            continue
        meta.setdefault("estado", "recibido")
        meta.setdefault("prioridad", "media")
        meta.setdefault("hito", "")
        if meta["hito"].lower() in ("null", "none", "~"):
            meta["hito"] = ""
        meta["_file"] = path.name
        items.append(meta)
    return items


def replace_zone(path: Path, rendered: str) -> None:
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(r"(<!-- RENDER:START -->).*?(<!-- RENDER:END -->)", re.DOTALL)
    if not pattern.search(text):
        sys.exit(f"ERROR: {path} no tiene zona <!-- RENDER:START/END -->")
    new = pattern.sub(lambda m: f"{m.group(1)}\n{rendered}\n{m.group(2)}", text)
    path.write_text(new, encoding="utf-8", newline="\n")


def item_link(it: dict[str, str], rel: str) -> str:
    return f"[{it['id']}]({rel}/{it['_file']})"


def render_backlog(items: list[dict[str, str]]) -> str:
    lines: list[str] = []
    abiertos = [i for i in items if i["estado"] in ESTADOS_ABIERTOS]
    for estado in ESTADOS_ABIERTOS:
        grupo = sorted(
            (i for i in abiertos if i["estado"] == estado),
            key=lambda i: (PRIORIDAD_ORDEN.get(i["prioridad"], 9), i["id"]),
        )
        if not grupo:
            continue
        lines.append(f"### {ETIQUETA_ESTADO[estado]}\n")
        lines.append("| Item | Título | Prioridad | Hito |")
        lines.append("|---|---|---|---|")
        for it in grupo:
            hito = it["hito"] or "—"
            lines.append(
                f"| {item_link(it, 'items')} | {it.get('titulo', '')} | {it['prioridad']} | {hito} |"
            )
        lines.append("")
    if not lines:
        lines.append("_No hay items abiertos._")
    return "\n".join(lines).rstrip()


def render_roadmap(items: list[dict[str, str]]) -> str:
    lines: list[str] = []
    hitos = sorted({i["hito"] for i in items if i["hito"]})
    if not hitos:
        return "_Ningún item tiene hito asignado todavía._"
    lines.append("| Hito | Items | Hechos | Progreso |")
    lines.append("|---|---|---|---|")
    for hito in hitos:
        grupo = [i for i in items if i["hito"] == hito]
        hechos = [i for i in grupo if i["estado"] == "hecho"]
        pct = round(100 * len(hechos) / len(grupo)) if grupo else 0
        lines.append(f"| **{hito}** | {len(grupo)} | {len(hechos)} | {pct}% |")
    lines.append("")
    for hito in hitos:
        grupo = sorted((i for i in items if i["hito"] == hito), key=lambda i: i["id"])
        lines.append(f"### Hito {hito}\n")
        for it in grupo:
            estado = ETIQUETA_ESTADO.get(it["estado"], it["estado"])
            lines.append(f"- {item_link(it, 'items')} — {it.get('titulo', '')} · {estado}")
        lines.append("")
    return "\n".join(lines).rstrip()


def render_catalogo(items: list[dict[str, str]]) -> str:
    lines: list[str] = []
    disponibles = sorted((i for i in items if i["estado"] == "hecho"), key=lambda i: i["id"])
    en_camino = sorted((i for i in items if i["estado"] == "desarrollo"), key=lambda i: i["id"])
    if disponibles:
        lines.append("**✅ Disponible hoy:**\n")
        lines += [f"- {i.get('titulo', '')}" for i in disponibles]
        lines.append("")
    if en_camino:
        lines.append("**🚧 En camino:**\n")
        lines += [f"- {i.get('titulo', '')}" for i in en_camino]
        lines.append("")
    if not lines:
        lines.append("_Aún no hay funcionalidades disponibles: el proyecto está en construcción._")
    return "\n".join(lines).rstrip()


def render_index(items: list[dict[str, str]]) -> None:
    lines = [
        "# Índice de items",
        "",
        "> Generado por `scripts/render_planning.py`. NO editar a mano.",
        "> Consultar antes de crear un item nuevo para evitar duplicados.",
        "",
        "| ID | Título | Estado | Hito |",
        "|---|---|---|---|",
    ]
    for it in sorted(items, key=lambda i: i["id"]):
        hito = it["hito"] or "—"
        lines.append(f"| [{it['id']}]({it['_file']}) | {it.get('titulo', '')} | {it['estado']} | {hito} |")
    lines.append("")
    lines.append(f"_Última regeneración: {date.today().isoformat()} · {len(items)} items_")
    INDEX.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    items = load_items()
    replace_zone(BACKLOG, render_backlog(items))
    replace_zone(ROADMAP, render_roadmap(items))
    replace_zone(PRODUCT, render_catalogo(items))
    render_index(items)
    print(f"OK: {len(items)} items renderizados en BACKLOG, ROADMAP, PRODUCT_CONTEXT e INDEX.")


if __name__ == "__main__":
    main()

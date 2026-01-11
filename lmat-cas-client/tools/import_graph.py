"""Print an internal import graph for lmat_cas_client.

Usage (from repo root):
  python lmat-cas-client/tools/import_graph.py --format edges
  python lmat-cas-client/tools/import_graph.py --format dot > imports.dot

This is a lightweight helper to reason about dependency cycles.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ImportEdge:
    src: str
    dst: str


def module_name_from_path(root: Path, py_file: Path) -> str:
    rel = py_file.relative_to(root).with_suffix("")
    return ".".join(rel.parts)


def normalize_import(current_module: str, imported: str) -> str:
    # Keep only internal imports.
    if imported.startswith("lmat_cas_client."):
        return imported
    if imported == "lmat_cas_client":
        return imported

    # Handle relative imports expressed as leading dots in `imported`.
    if imported.startswith("."):
        # Count leading dots
        dots = 0
        for ch in imported:
            if ch == ".":
                dots += 1
            else:
                break
        suffix = imported[dots:]
        parts = current_module.split(".")
        if dots > len(parts):
            return ""
        base = parts[: -dots]
        if suffix:
            return ".".join(base + [suffix])
        return ".".join(base)

    # Everything else is external; drop it.
    return ""


def collect_edges(pkg_root: Path) -> list[ImportEdge]:
    edges: set[ImportEdge] = set()

    for py_file in pkg_root.rglob("*.py"):
        try:
            text = py_file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = py_file.read_text(encoding="utf-8", errors="replace")

        try:
            tree = ast.parse(text, filename=str(py_file))
        except SyntaxError:
            continue

        current_module = module_name_from_path(pkg_root.parent, py_file)

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    dst = normalize_import(current_module, alias.name)
                    if dst:
                        edges.add(ImportEdge(current_module, dst))

            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                if node.level and not module.startswith("."):
                    module = "." * node.level + module
                elif node.level and module == "":
                    module = "." * node.level

                dst = normalize_import(current_module, module)
                if dst:
                    edges.add(ImportEdge(current_module, dst))

    return sorted(edges, key=lambda e: (e.src, e.dst))


def to_dot(edges: list[ImportEdge], focus_prefix: str) -> str:
    lines = ["digraph imports {", "  rankdir=LR;"]
    for e in edges:
        if not e.src.startswith(focus_prefix):
            continue
        if not e.dst.startswith(focus_prefix):
            continue
        lines.append(f'  "{e.src}" -> "{e.dst}";')
    lines.append("}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--package-root",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "lmat_cas_client",
        help="Path to the lmat_cas_client package directory",
    )
    parser.add_argument(
        "--format",
        choices=("edges", "dot"),
        default="edges",
        help="Output format",
    )
    parser.add_argument(
        "--focus",
        default="lmat_cas_client.compiling",
        help="Only show edges where both ends start with this prefix",
    )

    args = parser.parse_args()
    pkg_root: Path = args.package_root
    edges = collect_edges(pkg_root)

    if args.format == "dot":
        print(to_dot(edges, args.focus))
        return 0

    for e in edges:
        if e.src.startswith(args.focus) and e.dst.startswith(args.focus):
            print(f"{e.src} -> {e.dst}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

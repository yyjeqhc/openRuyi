#!/usr/bin/env python3
"""Extract common Rust packaging blockers from OBS/build logs.

This helper is intentionally small and best-effort. It does not replace
repo-index, buildinfo, or OBS solver output.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


NOTHING_PROVIDES_RE = re.compile(r"nothing provides (?P<cap>crate\([^)]+\)(?:\s*[<>=]+\s*[^,\s]+)?)")
NO_MATCH_RE = re.compile(r"no matching package (?:named|found).*?[`'](?P<crate>[^`']+)[`']", re.I)
SEARCHED_RE = re.compile(r"searched package name:\s*[`'](?P<crate>[^`']+)[`']", re.I)
REQUIRED_BY_RE = re.compile(r"required by package [`']?(?P<package>[^`'\n]+)[`']?", re.I)


def classify_line(line: str) -> tuple[str, dict[str, str]] | None:
    match = NOTHING_PROVIDES_RE.search(line)
    if match:
        return "buildinfo_unresolvable", {"capability": match.group("cap").strip()}

    match = NO_MATCH_RE.search(line) or SEARCHED_RE.search(line)
    if match:
        return "cargo_offline_missing_crate", {"crate": match.group("crate").strip()}

    match = REQUIRED_BY_RE.search(line)
    if match:
        return "required_by", {"package": match.group("package").strip()}

    return None


def parse_paths(paths: list[Path]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for path in paths:
        try:
            lines = path.read_text(errors="replace").splitlines()
        except OSError as exc:
            findings.append({
                "type": "read_error",
                "path": str(path),
                "error": str(exc),
            })
            continue

        pending_missing: dict[str, str] | None = None
        for lineno, line in enumerate(lines, 1):
            parsed = classify_line(line)
            if not parsed:
                continue

            kind, payload = parsed
            item = {"type": kind, "path": str(path), "line": str(lineno), **payload}

            if kind == "cargo_offline_missing_crate":
                pending_missing = item
                findings.append(item)
            elif kind == "required_by" and pending_missing and "required_by" not in pending_missing:
                pending_missing["required_by"] = payload["package"]
            elif kind != "required_by":
                findings.append(item)

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="Log files to inspect")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    args = parser.parse_args()

    findings = parse_paths(args.paths)
    if args.json:
        json.dump({"findings": findings, "count": len(findings)}, sys.stdout, indent=2, sort_keys=True)
        sys.stdout.write("\n")
        return 0

    for item in findings:
        bits = [item["type"], item.get("capability") or item.get("crate") or item.get("error", "")]
        if item.get("required_by"):
            bits.append(f"required by {item['required_by']}")
        bits.append(f"({item['path']}:{item.get('line', '?')})")
        print(" - ".join(bit for bit in bits if bit))
    print(f"findings: {len(findings)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

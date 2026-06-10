#!/usr/bin/env python3
"""Best-effort check of crate BuildRequires against a TakoPack repo-index JSON.

The comparison is intentionally conservative and only understands simple
operators used by static crate BuildRequires. Final decisions still belong to
repo-index/buildinfo/OBS.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from itertools import zip_longest


BR_RE = re.compile(
    r"^\s*BuildRequires:\s*(?P<cap>crate\([^)]+\))"
    r"(?:\s*(?P<op>>=|=|>|<=|<)\s*(?P<version>[^\s#]+))?"
)


def split_version(value: str) -> list[object]:
    parts: list[object] = []
    for token in re.split(r"([0-9]+|[A-Za-z]+)", value):
        if not token or token in ".-_+~":
            continue
        if token.isdigit():
            parts.append(int(token))
        elif token.strip(".-_+~"):
            parts.append(token)
    return parts


def compare_versions(left: str, right: str) -> int:
    for a, b in zip_longest(split_version(left), split_version(right), fillvalue=0):
        if type(a) is not type(b):
            a = str(a)
            b = str(b)
        if a < b:
            return -1
        if a > b:
            return 1
    return 0


def satisfies(provider: str, op: str | None, required: str | None) -> bool:
    if not op or not required:
        return True
    cmp_result = compare_versions(provider, required)
    return {
        "=": cmp_result == 0,
        ">=": cmp_result >= 0,
        ">": cmp_result > 0,
        "<=": cmp_result <= 0,
        "<": cmp_result < 0,
    }[op]


def read_buildrequires(spec: Path) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    for lineno, line in enumerate(spec.read_text(errors="replace").splitlines(), 1):
        match = BR_RE.search(line)
        if not match:
            continue
        entries.append({
            "line": str(lineno),
            "capability": match.group("cap"),
            "op": match.group("op") or "",
            "version": match.group("version") or "",
            "raw": line.strip(),
        })
    return entries


def read_capabilities(index: Path) -> dict[str, list[dict[str, str]]]:
    data = json.loads(index.read_text())
    caps = data.get("capabilities")
    if isinstance(caps, dict):
        return {
            cap: [
                {"version": str(item.get("version", "")), "rpm_name": str(item.get("rpm_name", ""))}
                for item in items
            ]
            for cap, items in caps.items()
            if isinstance(items, list)
        }

    out: dict[str, list[dict[str, str]]] = {}
    for package in data.get("packages", []):
        for provide in package.get("provides", []):
            cap = provide.get("cap")
            if not cap:
                continue
            out.setdefault(str(cap), []).append({
                "version": str(provide.get("version", "")),
                "rpm_name": str(package.get("rpm_name", "")),
            })
    return out


def check(spec: Path, index: Path) -> dict[str, object]:
    entries = read_buildrequires(spec)
    caps = read_capabilities(index)
    unsatisfied: list[dict[str, object]] = []

    for entry in entries:
        providers = caps.get(entry["capability"], [])
        matching = [
            provider for provider in providers
            if satisfies(provider["version"], entry["op"] or None, entry["version"] or None)
        ]
        if matching:
            continue
        unsatisfied.append({**entry, "providers": providers})

    return {
        "spec": str(spec),
        "index": str(index),
        "checked": len(entries),
        "unsatisfied_count": len(unsatisfied),
        "unsatisfied": unsatisfied,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec", required=True, type=Path, help="Spec file to check")
    parser.add_argument("--index", required=True, type=Path, help="TakoPack repo-index JSON")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    args = parser.parse_args()

    result = check(args.spec, args.index)
    if args.json:
        json.dump(result, sys.stdout, indent=2, sort_keys=True)
        sys.stdout.write("\n")
        return 0 if result["unsatisfied_count"] == 0 else 1

    print(f"checked: {result['checked']}")
    print(f"unsatisfied: {result['unsatisfied_count']}")
    for item in result["unsatisfied"]:
        providers = item["providers"]
        versions = ", ".join(f"{p['rpm_name']}={p['version']}" for p in providers) or "none"
        constraint = f"{item['capability']} {item['op']} {item['version']}".strip()
        print(f"{item['line']}: {constraint} provider_versions: {versions}")
    return 0 if result["unsatisfied_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

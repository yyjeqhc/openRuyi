#!/usr/bin/env python3
"""Batch convert perl packages to BuildSystem via cpan2spec.

Generates specs WITHOUT preserving SPDX headers (will be added later).
"""

import subprocess
import sys
import shutil
from pathlib import Path

REPO_ROOT = Path("/root/git/openruyi-repo")
SPECS_DIR = REPO_ROOT / "SPECS"
CPAN2SPEC = Path("/root/git/cpan2spec/cpan2spec")
WORK_DIR = Path("/tmp/perl-convert-work")


def pkg_to_module(pkg_name: str) -> str:
    name = pkg_name[5:] if pkg_name.startswith("perl-") else pkg_name
    return name.replace("-", "::")


def has_buildsystem(spec_path: Path) -> bool:
    with open(spec_path) as f:
        for line in f:
            if line.startswith("BuildSystem:"):
                return True
    return False


def convert_one(pkg_name: str) -> str:
    spec_path = SPECS_DIR / pkg_name / f"{pkg_name}.spec"
    if not spec_path.exists():
        return "NO_SPEC"
    if has_buildsystem(spec_path):
        return "SKIP"

    module = pkg_to_module(pkg_name)
    work_dir = WORK_DIR / pkg_name
    work_dir.mkdir(parents=True, exist_ok=True)

    lib_dir = work_dir / "library-perl"
    if lib_dir.exists():
        shutil.rmtree(lib_dir)

    r = subprocess.run(
        ["perl", str(CPAN2SPEC), "--verbose", "--no-cleanup-source", module],
        cwd=str(work_dir), capture_output=True, text=True, timeout=300,
    )
    if r.returncode != 0:
        return f"ERROR: {r.stderr[-200:]}" if r.stderr else "ERROR: unknown"

    pkg_dir_name = f"perl-{module.replace('::', '-')}"
    gen_spec = lib_dir / pkg_dir_name / f"{pkg_dir_name}.spec"
    if not gen_spec.exists():
        return "ERROR: no output spec"

    shutil.copy2(gen_spec, spec_path)
    return "OK"


def main():
    pkgs = sorted([
        d.name for d in SPECS_DIR.iterdir()
        if d.is_dir() and d.name.startswith("perl-")
        and (d / f"{d.name}.spec").exists()
        and not has_buildsystem(d / f"{d.name}.spec")
    ])
    print(f"Packages to convert: {len(pkgs)}")

    ok = err = skip = 0
    errors = []
    for i, pkg in enumerate(pkgs, 1):
        print(f"[{i}/{len(pkgs)}] {pkg}...", end=" ", flush=True)
        status = convert_one(pkg)
        if status == "OK":
            ok += 1
            print("✓")
        elif status == "SKIP":
            skip += 1
            print("-")
        elif status == "NO_SPEC":
            err += 1
            print("✗ no spec")
        else:
            err += 1
            errors.append((pkg, status))
            print(f"✗ {status[:80]}")

    print(f"\nDone: {ok} converted, {err} errors, {skip} skipped")
    if errors:
        print("\nErrors:")
        for pkg, e in errors:
            print(f"  {pkg}: {e[:120]}")
    return 0 if err == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

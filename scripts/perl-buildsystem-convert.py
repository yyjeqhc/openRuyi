#!/usr/bin/env python3
"""Convert perl packages to use BuildSystem via cpan2spec.

This script:
1. Iterates perl-* packages without BuildSystem tag
2. Runs cpan2spec to generate new spec with BuildSystem
3. Preserves SPDX header from existing spec
4. Compares License fields (existing vs cpan2spec)
5. Merges: SPDX header + new spec body
6. Records results for review

Usage:
    python3 scripts/perl-buildsystem-convert.py [--dry-run] [--limit N] [--package PKG]
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional


REPO_ROOT = Path("/root/git/openruyi-repo")
SPECS_DIR = REPO_ROOT / "SPECS"
CPAN2SPEC = Path("/root/git/cpan2spec/cpan2spec")
WORK_DIR = Path("/tmp/perl-convert-work")


@dataclass
class ConversionResult:
    package: str
    module_name: str
    status: str = ""
    old_license: str = ""
    new_license: str = ""
    license_match: bool = True
    has_buildsystem_before: bool = False
    error: str = ""
    notes: str = ""


@dataclass
class ConversionReport:
    total: int = 0
    converted: int = 0
    license_mismatch: int = 0
    errors: int = 0
    skipped: int = 0
    results: list = field(default_factory=list)


def pkg_to_module(pkg_name: str) -> str:
    """Convert perl-Foo-Bar to Foo::Bar."""
    if pkg_name.startswith("perl-"):
        name = pkg_name[5:]
    else:
        name = pkg_name
    return name.replace("-", "::")


def extract_spdx_header(spec_path: Path) -> str:
    """Extract SPDX header lines from a spec file."""
    lines = []
    with open(spec_path, "r") as f:
        for line in f:
            stripped = line.rstrip()
            if stripped.startswith("# SPDX-") or stripped == "#":
                lines.append(stripped)
            elif stripped.startswith("#!RemoteAsset"):
                lines.append(stripped)
            elif lines:
                break
    return "\n".join(lines)


def extract_license(spec_path: Path) -> str:
    """Extract License field from spec file."""
    with open(spec_path, "r") as f:
        for line in f:
            if line.startswith("License:"):
                return line.split(":", 1)[1].strip()
    return ""


def has_buildsystem(spec_path: Path) -> bool:
    """Check if spec already has BuildSystem tag."""
    with open(spec_path, "r") as f:
        for line in f:
            if line.startswith("BuildSystem:"):
                return True
    return False


def run_cpan2spec(module_name: str, work_dir: Path) -> Optional[Path]:
    """Run cpan2spec and return path to generated spec."""
    lib_dir = work_dir / "library-perl"
    if lib_dir.exists():
        shutil.rmtree(lib_dir)

    cmd = [
        "perl", str(CPAN2SPEC),
        "--verbose",
        "--no-cleanup-source",
        module_name,
    ]

    result = subprocess.run(
        cmd,
        cwd=str(work_dir),
        capture_output=True,
        text=True,
        timeout=300,
    )

    if result.returncode != 0:
        return None

    pkg_name = f"perl-{module_name.replace('::', '-')}"
    spec_path = lib_dir / pkg_name / f"{pkg_name}.spec"
    if spec_path.exists():
        return spec_path
    return None


def merge_spec(spdx_header: str, new_spec_path: Path, output_path: Path):
    """Merge SPDX header with new spec body."""
    with open(new_spec_path, "r") as f:
        new_content = f.read()

    lines = new_content.split("\n")
    body_start = 0
    for i, line in enumerate(lines):
        if line.startswith("Name:"):
            body_start = i
            break

    body = "\n".join(lines[body_start:])

    with open(output_path, "w") as f:
        f.write(spdx_header + "\n")
        f.write("\n")
        f.write(body)
        f.write("\n")


def convert_package(pkg_name: str, dry_run: bool = False) -> ConversionResult:
    """Convert a single perl package to use BuildSystem."""
    result = ConversionResult(
        package=pkg_name,
        module_name=pkg_to_module(pkg_name),
    )

    spec_path = SPECS_DIR / pkg_name / f"{pkg_name}.spec"
    if not spec_path.exists():
        result.status = "error"
        result.error = f"Spec file not found: {spec_path}"
        return result

    if has_buildsystem(spec_path):
        result.status = "skipped"
        result.has_buildsystem_before = True
        result.notes = "Already has BuildSystem tag"
        return result

    result.old_license = extract_license(spec_path)
    spdx_header = extract_spdx_header(spec_path)

    work_dir = WORK_DIR / pkg_name
    work_dir.mkdir(parents=True, exist_ok=True)

    try:
        new_spec_path = run_cpan2spec(result.module_name, work_dir)
    except subprocess.TimeoutExpired:
        result.status = "error"
        result.error = "cpan2spec timed out (5 min)"
        return result
    except Exception as e:
        result.status = "error"
        result.error = str(e)
        return result

    if new_spec_path is None:
        result.status = "error"
        result.error = "cpan2spec failed to generate spec"
        return result

    result.new_license = extract_license(new_spec_path)
    result.license_match = (
        result.old_license.lower().strip() == result.new_license.lower().strip()
    )

    if not result.license_match:
        result.status = "license_mismatch"
        result.notes = f"Old: {result.old_license} | New: {result.new_license}"
    else:
        result.status = "converted"

    if not dry_run:
        merge_spec(spdx_header, new_spec_path, spec_path)
    else:
        dry_path = WORK_DIR / "dry-run" / pkg_name / f"{pkg_name}.spec"
        dry_path.parent.mkdir(parents=True, exist_ok=True)
        merge_spec(spdx_header, new_spec_path, dry_path)

    return result


def find_packages_to_convert(limit: Optional[int] = None) -> list[str]:
    """Find perl packages without BuildSystem tag."""
    packages = []
    for entry in sorted(SPECS_DIR.iterdir()):
        if not entry.is_dir():
            continue
        if not entry.name.startswith("perl-"):
            continue
        spec_path = entry / f"{entry.name}.spec"
        if not spec_path.exists():
            continue
        if has_buildsystem(spec_path):
            continue
        packages.append(entry.name)
        if limit and len(packages) >= limit:
            break
    return packages


def main():
    parser = argparse.ArgumentParser(description="Convert perl packages to BuildSystem")
    parser.add_argument("--dry-run", action="store_true", help="Don't modify specs")
    parser.add_argument("--limit", type=int, help="Max packages to process")
    parser.add_argument("--package", type=str, help="Convert single package")
    parser.add_argument("--output", type=str, default="reports/perl-conversion.json",
                        help="Output report path")
    args = parser.parse_args()

    WORK_DIR.mkdir(parents=True, exist_ok=True)
    (WORK_DIR / "dry-run").mkdir(parents=True, exist_ok=True)

    if args.package:
        packages = [args.package]
    else:
        packages = find_packages_to_convert(args.limit)

    print(f"Found {len(packages)} packages to convert")

    report = ConversionReport(total=len(packages))

    for i, pkg in enumerate(packages, 1):
        print(f"[{i}/{len(packages)}] Converting {pkg}...", end=" ", flush=True)
        result = convert_package(pkg, dry_run=args.dry_run)
        report.results.append(result)

        if result.status == "converted":
            report.converted += 1
            print("✓")
        elif result.status == "license_mismatch":
            report.license_mismatch += 1
            print(f"⚠ License mismatch: {result.notes}")
        elif result.status == "error":
            report.errors += 1
            print(f"✗ {result.error}")
        elif result.status == "skipped":
            report.skipped += 1
            print("- skipped")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(asdict(report), f, indent=2, ensure_ascii=False)

    print(f"\n=== Summary ===")
    print(f"Total: {report.total}")
    print(f"Converted: {report.converted}")
    print(f"License mismatch: {report.license_mismatch}")
    print(f"Errors: {report.errors}")
    print(f"Skipped: {report.skipped}")

    if report.license_mismatch > 0:
        print(f"\nLicense mismatches need review:")
        for r in report.results:
            if r.status == "license_mismatch":
                print(f"  {r.package}: {r.notes}")

    if report.errors > 0:
        print(f"\nErrors:")
        for r in report.results:
            if r.status == "error":
                print(f"  {r.package}: {r.error}")

    return 0 if report.errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

# Rust Packaging Overview

Use the package type to choose the build system:

```text
Rust application        -> BuildSystem: rust
Rust crate provider     -> BuildSystem: rustcrates
Python/Rust extension   -> BuildSystem: pyproject
```

Rules of thumb:

- A Rust application must not be migrated to `BuildSystem: rustcrates`.
- A Python/Rust extension must stay `BuildSystem: pyproject`; do not change it
  to `rust` or `rustcrates`.
- Only crate provider packages use `BuildSystem: rustcrates`.
- Do not blindly preserve upstream `Cargo.lock`, `--locked`, or `--frozen`.
  Ruyi packaging normally resolves through the repository-provided offline
  registry.
- Do not commit generated `Cargo.lock`, `target`, RPM/SRPM, generated lock, or
  buildroot files.
- Root crates and local/path crates are part of the source package. Do not
  create providers for them.
- Git dependencies are usually source-policy blockers. Either replace them with
  packaged sources and a local path patch, or stop and report.
- `cloud-hypervisor` has a known exception: `micro-http` is handled as Source1
  plus a local path patch.

Recommended starting point:

1. Start from `rust-packaging-stable-base`.
2. Classify the package type before editing.
3. Audit source dependencies before touching providers.
4. Use static crate BuildRequires for Rust applications.
5. Use provider packages only for crates that are externally resolved through
   the offline registry.
6. Validate with repo-index, repo-plan, buildreqs, buildinfo, smoke build, and
   OBS as appropriate.

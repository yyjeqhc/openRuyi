# Rust Application Packaging

Use this workflow for Rust applications, not crate providers and not
Python/Rust extensions.

Start:

1. Start from `rust-packaging-stable-base`.
2. Create a focused branch for the application.
3. Check `/root/git/ruyia`, `/root/git/TakoPack`, and
   `/root/git/rust-rpm-macros` for unexpected tracked or staged changes.

Source audit:

- Inspect source `Cargo.toml` files.
- Decide whether upstream `Cargo.lock` is policy-compatible. Do not default to
  committing it.
- Identify git dependencies, path dependencies, vendor config, local workspace
  crates, target-specific dependencies, dev/test/fuzz dependencies, and native
  dependencies.
- Local/path workspace crates stay in the source tree and do not become
  providers.
- Normal-build git dependencies are blockers unless handled by source packaging
  and a local path patch.

Static BuildRequires:

- Rust applications use static crate BuildRequires.
- Do not use `%cargo_buildrequires`.
- Avoid `%generate_buildrequires` for the Rust app dependency closure once the
  static list is known.
- Keep static BuildRequires aligned with provider capabilities. If providers
  expose `crate(foo-1) = 1.2.3`, the app should not require
  `1.2.3+spec-*` or another full-version suffix.

Smoke progression:

1. Generate or draft a trial spec.
2. Run buildinfo.
3. Handle solver blockers as provider waves.
4. Run `%prep`; confirm source unpack and source patches.
5. Run cargo offline resolver.
6. Handle resolver missing-crate blockers as provider/source tail waves.
7. Continue until real compilation starts.
8. Formalize the package only after a meaningful smoke pass reaches real
   compilation.
9. Trigger OBS full build.
10. Run final merge-readiness audit.

Important distinctions:

- Buildinfo passing does not mean the cargo offline resolver passes.
- Resolver passing does not mean real compilation passes.
- A local build that reaches real compilation and is then stopped or times out
  for resource reasons is a useful smoke pass, but record the stop point.

Target-specific dependencies:

- Do not drop a dependency only because x86_64 smoke does not use it.
- If the package target set includes riscv64, riscv64 target-specific
  dependencies belong in the supported dependency closure.
- `cloud-hypervisor` showed this with `fdt 0.1.5` and `vm-fdt 0.3.0`: both
  are target-specific, but still required for the intended architecture set.

Stop and report:

- New normal-build git dependency that has not been classified.
- Cargo.lock or vendor policy conflict.
- Native/system dependency blocker.
- Source unpack failure.
- Required path patch failure.
- repo-plan or buildreqs not clean.
- High-risk provider refresh with exact pins or upper-bound conflicts.
- Rust compile error before meaningful real compilation starts.

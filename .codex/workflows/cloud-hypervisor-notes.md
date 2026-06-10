# cloud-hypervisor Notes

Known successful package line:

- Package: `SPECS/cloud-hypervisor`
- Formal branch: `cloud-hypervisor-vendor-to-crates`
- Successful commit: `3e5abb1197b6c6ffc0e9071c1dd1c2e3e0f2fd20`
- OBS project: `home:yyjeqhc:n`
- OBS x64/x86_64: `succeeded`

Source facts:

- Selected upstream commit:
  `829676e6403ff3fa711c9e901f90f05737c08b88`
- `micro-http` commit:
  `876f3feccc30e09225f2c77bf95a6b2d46a9259e`

Packaging strategy:

- `cloud-hypervisor` is a Rust application.
- It uses `BuildSystem: rust`, not `rustcrates`.
- It uses static crate BuildRequires.
- It does not commit upstream or generated `Cargo.lock`.
- It does not use `--locked` or `--frozen`.
- It sets `OPENSSL_NO_VENDOR=1`.

`micro-http` exception:

- Package `micro-http` as Source1.
- Unpack it into `deps/micro-http`.
- Create `deps/micro-http/.cargo-checksum.json`.
- Patch `vmm/Cargo.toml` so the `micro_http` git dependency becomes:
  `path = "../deps/micro-http"`.
- Treat any other normal-build git dependency as a new blocker until audited.

Build features:

- x86_64:
  `--no-default-features --features "mshv,kvm" -p cloud-hypervisor`
- riscv64:
  `--no-default-features --features "kvm" -p cloud-hypervisor`

Build targets:

- `cloud-hypervisor`
- `vhost_user_net`
- `vhost_user_block`

Provider closure lessons:

- Buildinfo passing only proves OBS solver resolution. Cargo offline resolver
  may still expose source/provider tail blockers.
- Target-specific dependencies for supported architectures are real
  dependencies. The `fdt` and `vm-fdt` blockers came from riscv64/aarch64
  target-specific sections and were not false positives.
- Final static BuildRequires must match provider capability versions. Providers
  expose ordinary `%{version}` capabilities; application BuildRequires should
  not continue to ask for `+spec-*`, `+zstd-*`, or other full-version strings
  unless the provider deliberately exposes that version.
- riscv64 is disabled in the current OBS result, but the dependency closure was
  included. Future riscv64 enablement may still reveal compile-time issues.

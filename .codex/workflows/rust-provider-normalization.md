# Rust Provider Normalization

Provider work covers four common cases:

- Missing provider: no policy provider exists for a required crate/version.
- Old-style provider: a directory exists, but capabilities are unversioned or
  feature capabilities are incomplete.
- Version-too-low provider: OBS or repo checks need a higher version than the
  current provider offers.
- Missing feature capability: base capability exists, but required features do
  not.

Provider naming policy:

- `0.x` crates keep the minor version in the provider name.
  Example: `vm-memory 0.17.x -> rust-vm-memory-0.17`.
- `1.x+` crates use the major version in the provider name.
  Example: `winnow 1.x -> rust-winnow-1`.
- Do not generate dotted or full-version providers such as
  `rust-winnow-1.0` or `rust-fdt-0.1.5`.
- Preserve the existing provider version unless the solver or dependency
  closure requires a refresh.

Generation rule:

- Use TakoPack to generate or refresh providers.
- Do not edit `Provides` or `Requires` with `sed` or manual string patches.
- Do not hand-add capability aliases.
- Do not modify TakoPack or rust-rpm-macros during provider waves.

Capability validation:

1. Check `Version:` equals the intended target version.
2. Confirm the base capability exists, for example:
   `crate(vm-fdt-0.3) = 0.3.0`.
3. Confirm the default feature capability exists when the crate has a default
   feature, for example:
   `crate(vm-fdt-0.3/default) = 0.3.0`.
4. Confirm required feature capabilities exist.
5. Confirm no wrong dotted capability exists, for example:
   `crate(vm-fdt-0.3.0)`.
6. Confirm provider capability versions use `%{version}` unless there is a
   deliberate policy reason otherwise. `full_version` may still be used for
   Source URLs.

Repository validation:

```bash
cd /root/git/TakoPack
cargo run -- cargo repo-index --ruyispec --output /tmp/provider-index.json
cargo run -- cargo repo-plan \
  /root/git/ruyia/SPECS/cargo-c/Cargo.toml \
  --index /tmp/provider-index.json \
  --check-transitive \
  --json > /tmp/provider-cargo-c-plan.json
cargo run -- cargo buildreqs \
  -f /root/git/ruyia/SPECS/cargo-c/Cargo.toml \
  --index /tmp/provider-index.json \
  --kind app \
  --json > /tmp/provider-cargo-c-buildreqs.json
```

OBS validation:

- Repo-index satisfaction does not mean the OBS solver can see the package.
- After adding or refreshing a provider, trigger the provider build in
  `home:yyjeqhc:n` and confirm x64/x86_64 `succeeded`.
- Only rerun the application smoke after the provider is visible in OBS.

Autonomy:

- Same-kind provider/source tail blockers can be handled in waves.
- Stop and report when the version source is unclear, a high-impact refresh has
  exact pins or upper-bound conflicts, repo checks are not clean, or TakoPack
  generation fails.

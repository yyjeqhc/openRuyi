# Python/Rust Extension Packaging

Python/Rust extension packages stay in the Python packaging path:

```text
Python/Rust extension -> BuildSystem: pyproject
```

Do not change these packages to `BuildSystem: rust` or `BuildSystem:
rustcrates`.

Backend notes:

- `maturin` normally drives a Rust extension build from pyproject metadata.
- `pyo3` is a Rust/Python binding layer used by many maturin projects.
- `setuptools-rust` is another Python build backend path for Rust extensions.
- `%generate_buildrequires` and `%pyproject_buildrequires` can be normal for
  Python packages. Do not confuse this with the Rust application rule that
  avoids `%cargo_buildrequires`.

Dependency handling:

- Root crates and local workspace crates are part of the Python source package;
  do not generate providers for them.
- Do not automatically add dev/test dependencies unless the package build or
  chosen check phase requires them.
- Prefer import checks or minimal smoke checks over full pytest when tests need
  network, optional services, or broad runtime fixtures.
- If cargo metadata fails during pyproject buildrequires generation, inspect the
  missing crate and add only the required static crate BuildRequires when a
  provider already exists.

Recent rebuild lessons:

- `python-jiter` failed during pyproject dynamic buildrequires generation
  because cargo metadata could not find `autocfg`.
- `python-outlines-core` failed because cargo metadata could not find
  `winapi-i686-pc-windows-gnu`.
- `python-uuid-utils` failed for the same Windows target crate.
- These were application spec dependency gaps, not provider capability bugs.
  The minimal fix was to add the static crate BuildRequires to the Python
  package specs while keeping `BuildSystem: pyproject`.

When to stop:

- A provider is missing a capability that should exist.
- A required provider is absent from OBS even though the repo-index sees it.
- The build fails in native compilation or Python backend code.
- The fix would require changing provider capabilities by hand.

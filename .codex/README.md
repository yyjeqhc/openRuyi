# Local Codex Workflows

This directory contains local Codex workflows for Rust packaging work in the
ruyia repository. Treat these files as working guides, not upstream policy.

Default baseline for new Rust packaging work:

- Start from `rust-packaging-stable-base`.
- Do not start new tasks from old single-package branches such as
  `cloud-hypervisor-vendor-to-crates` or `python-rust-extension-rebuild-fix`.
- Create a focused task branch from the stable base, then validate and push.

Fixed local paths:

- ruyia: `/root/git/ruyia`
- TakoPack: `/root/git/TakoPack`
- rust-rpm-macros: `/root/git/rust-rpm-macros`
- OBS project: `home:yyjeqhc:n`

Common entry points:

- Rust application packaging: `workflows/rust-app-packaging.md`
- Rust crate provider normalization: `workflows/rust-provider-normalization.md`
- Python/Rust extension packaging: `workflows/python-rust-extension-packaging.md`
- Final merge-readiness audit: `workflows/final-merge-readiness-audit.md`
- cloud-hypervisor notes: `workflows/cloud-hypervisor-notes.md`

Local execution logs under `.codex/jobs/` are intentionally ignored and should
not be committed.

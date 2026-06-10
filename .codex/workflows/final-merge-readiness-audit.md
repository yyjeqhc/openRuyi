# Final Merge-Readiness Audit

Run this before asking to merge a Rust packaging branch.

Worktree and branch:

- Fetch origin.
- Switch to the final branch.
- Confirm the expected HEAD.
- Confirm no unexpected tracked or staged changes.
- Untracked `.codex/` logs are acceptable only if they are not part of the
  merge.
- Confirm TakoPack and rust-rpm-macros have no tracked changes.

Commit coverage:

- Verify required provider wave commits are ancestors of HEAD, or document why
  they are provided through another branch already present in the target OBS
  project.
- Verify final application and follow-up fix commits are included.

Package content:

- Check package files.
- Confirm correct `BuildSystem`.
- Confirm no package was accidentally changed to `rustcrates`.
- Confirm `Cargo.toml` is present when the final app spec expects it.
- Confirm `Cargo.lock`, `target`, RPM/SRPM, generated lock, and buildroot files
  are absent.

Rust application checks:

- `BuildSystem: rust` is present.
- `BuildSystem: rustcrates` is absent.
- `%cargo_buildrequires` is absent.
- Dynamic Rust dependency generation is absent when static BuildRequires are
  intended.
- `--locked` and `--frozen` are absent unless explicitly justified.
- Source/path patches are present and scoped.

Python/Rust extension checks:

- `BuildSystem: pyproject` remains present.
- `%generate_buildrequires` and `%pyproject_buildrequires` may be expected.
- The package is not migrated to `rust` or `rustcrates`.

Static BuildRequires:

- Count total and crate BuildRequires.
- Check duplicate BuildRequires.
- Compare all crate BuildRequires against repo-index provider capabilities.
- Unsatisfied count must be zero for merge-ready Rust application branches.

Repository checks:

```bash
cd /root/git/TakoPack
cargo run -- cargo repo-index --ruyispec --output /tmp/final-audit-index.json
cargo run -- cargo repo-plan \
  /root/git/ruyia/SPECS/cargo-c/Cargo.toml \
  --index /tmp/final-audit-index.json \
  --check-transitive \
  --json > /tmp/final-audit-cargo-c-plan.json
cargo run -- cargo buildreqs \
  -f /root/git/ruyia/SPECS/cargo-c/Cargo.toml \
  --index /tmp/final-audit-index.json \
  --kind app \
  --json > /tmp/final-audit-cargo-c-buildreqs.json
```

OBS checks:

- Read `osc results` for the package set.
- Confirm x64/x86_64 succeeded for packages that were rebuilt.
- Record disabled, unbuilt, or failed architectures.
- Do not trigger builds during an audit-only task.

Diff scope:

- Inspect `git show --stat`.
- Inspect changed paths.
- Confirm no temporary files or unrelated package changes are included.

Verdict:

`MERGE_READY=yes` only when:

- OBS x64/x86_64 succeeded where required.
- Package content is clean.
- Correct BuildSystem is present.
- Dynamic macros match the package type.
- Static BuildRequires are satisfied.
- repo-index, repo-plan, and buildreqs are clean or only known global noise.
- No forbidden files are committed.
- No unexpected tracked modifications remain.

Otherwise report `MERGE_READY=no` with blockers and risks.

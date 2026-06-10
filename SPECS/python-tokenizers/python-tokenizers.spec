# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tokenizers

Name:           python-%{srcname}
Version:        0.22.2
Release:        %autorelease
Summary:        Fast, state-of-the-art tokenizers optimized for research and production
License:        Apache-2.0
URL:            https://pypi.org/project/tokenizers/
VCS:            git:https://github.com/huggingface/tokenizers
#!RemoteAsset:  sha256:473b83b915e547aa366d1eee11806deaf419e17be16310ac0a14077f1e28f917
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(maturin)
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(ahash-0.8) >= 0.8.11
BuildRequires:  crate(ahash-0.8/default)
BuildRequires:  crate(ahash-0.8/serde)
BuildRequires:  crate(aho-corasick-1) >= 1.1
BuildRequires:  crate(aho-corasick-1/default)
BuildRequires:  crate(compact-str-0.9) >= 0.9
BuildRequires:  crate(compact-str-0.9/default)
BuildRequires:  crate(compact-str-0.9/serde)
BuildRequires:  crate(dary-heap-0.3) >= 0.3.6
BuildRequires:  crate(dary-heap-0.3/default)
BuildRequires:  crate(dary-heap-0.3/serde)
BuildRequires:  crate(derive-builder-0.20) >= 0.20
BuildRequires:  crate(derive-builder-0.20/default)
BuildRequires:  crate(env-logger-0.11) >= 0.11
BuildRequires:  crate(env-logger-0.11/default)
BuildRequires:  crate(esaxx-rs-0.1) >= 0.1.10
BuildRequires:  crate(esaxx-rs-0.1/cpp)
BuildRequires:  crate(fancy-regex-0.14) >= 0.14
BuildRequires:  crate(fancy-regex-0.14/default)
BuildRequires:  crate(getrandom-0.3) >= 0.3
BuildRequires:  crate(getrandom-0.3/default)
BuildRequires:  crate(hf-hub-0.4) >= 0.4.1
BuildRequires:  crate(hf-hub-0.4/ureq)
BuildRequires:  crate(indicatif-0.18) >= 0.18
BuildRequires:  crate(indicatif-0.18/default)
BuildRequires:  crate(itertools-0.14) >= 0.14
BuildRequires:  crate(itertools-0.14/default)
BuildRequires:  crate(libc-0.2) >= 0.2
BuildRequires:  crate(libc-0.2/default)
BuildRequires:  crate(log-0.4) >= 0.4
BuildRequires:  crate(log-0.4/default)
BuildRequires:  crate(macro-rules-attribute-0.2) >= 0.2.0
BuildRequires:  crate(macro-rules-attribute-0.2/default)
BuildRequires:  crate(monostate-0.1) >= 0.1.12
BuildRequires:  crate(monostate-0.1/default)
BuildRequires:  crate(ndarray-0.16) >= 0.16
BuildRequires:  crate(ndarray-0.16/default)
BuildRequires:  crate(numpy-0.26) >= 0.26
BuildRequires:  crate(numpy-0.26/default)
BuildRequires:  crate(onig-6) >= 6.5.1
BuildRequires:  crate(onig-6/default)
BuildRequires:  crate(once-cell-1) >= 1.19.0
BuildRequires:  crate(once-cell-1/default)
BuildRequires:  crate(paste-1) >= 1.0.14
BuildRequires:  crate(paste-1/default)
BuildRequires:  crate(pyo3-0.26) >= 0.26
BuildRequires:  crate(pyo3-0.26/abi3)
BuildRequires:  crate(pyo3-0.26/abi3-py39)
BuildRequires:  crate(pyo3-0.26/default)
BuildRequires:  crate(pyo3-0.26/py-clone)
BuildRequires:  crate(pyo3-async-runtimes-0.26) >= 0.26
BuildRequires:  crate(pyo3-async-runtimes-0.26/default)
BuildRequires:  crate(pyo3-async-runtimes-0.26/tokio-runtime)
BuildRequires:  crate(pkg-config-0.3/default) >= 0.3.33
BuildRequires:  crate(rand-0.9) >= 0.9
BuildRequires:  crate(rand-0.9/default)
BuildRequires:  crate(rayon-1) >= 1.10
BuildRequires:  crate(rayon-1/default)
BuildRequires:  crate(rayon-cond-0.4) >= 0.4
BuildRequires:  crate(rayon-cond-0.4/default)
BuildRequires:  crate(regex-1) >= 1.10
BuildRequires:  crate(regex-1/default)
BuildRequires:  crate(regex-syntax-0.8) >= 0.8
BuildRequires:  crate(regex-syntax-0.8/default)
BuildRequires:  crate(serde-1) >= 1.0
BuildRequires:  crate(serde-1/default)
BuildRequires:  crate(serde-1/derive)
BuildRequires:  crate(serde-1/rc)
BuildRequires:  crate(serde-json-1) >= 1.0
BuildRequires:  crate(serde-json-1/default)
BuildRequires:  crate(spm-precompiled-0.1) >= 0.1.3
BuildRequires:  crate(spm-precompiled-0.1/default)
BuildRequires:  crate(thiserror-2) >= 2
BuildRequires:  crate(thiserror-2/default)
BuildRequires:  crate(tokio-1) >= 1.47.1
BuildRequires:  crate(tokio-1/default)
BuildRequires:  crate(tokio-1/macros)
BuildRequires:  crate(tokio-1/rt)
BuildRequires:  crate(tokio-1/rt-multi-thread)
BuildRequires:  crate(tokio-1/signal)
BuildRequires:  crate(unicode-categories-0.1) >= 0.1
BuildRequires:  crate(unicode-categories-0.1/default)
BuildRequires:  crate(unicode-normalization-alignments-0.1) >= 0.1
BuildRequires:  crate(unicode-normalization-alignments-0.1/default)
BuildRequires:  crate(unicode-segmentation-1) >= 1.11
BuildRequires:  crate(unicode-segmentation-1/default)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Tokenizers provides fast and production-ready tokenization implementations for
modern natural language processing workloads.

%prep -a
rm -f bindings/python/Cargo.lock
python3 - <<'PY'
from pathlib import Path

for rel in ("bindings/python/Cargo.toml", "tokenizers/Cargo.toml"):
    path = Path(rel)
    lines = path.read_text().splitlines()
    out = []
    skipping = False
    for line in lines:
        stripped = line.strip()
        if stripped == "[dev-dependencies]":
            skipping = True
            continue
        if skipping and stripped.startswith("[") and stripped.endswith("]"):
            skipping = False
        if not skipping:
            out.append(line)
    path.write_text("\n".join(out) + "\n")
PY
mkdir -p .cargo ~/.cargo
cat > .cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "system-registry"

[source.system-registry]
directory = "/usr/share/cargo/registry"
EOF
cp .cargo/config.toml ~/.cargo/config.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc tokenizers/README.md
%license tokenizers/LICENSE

%changelog
%autochangelog

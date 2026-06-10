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
BuildRequires:  crate(env-logger-0.11) >= 0.11
BuildRequires:  crate(env-logger-0.11/default)
BuildRequires:  crate(itertools-0.14) >= 0.14
BuildRequires:  crate(itertools-0.14/default)
BuildRequires:  crate(libc-0.2) >= 0.2
BuildRequires:  crate(libc-0.2/default)
BuildRequires:  crate(ndarray-0.16) >= 0.16
BuildRequires:  crate(ndarray-0.16/default)
BuildRequires:  crate(numpy-0.26) >= 0.26
BuildRequires:  crate(numpy-0.26/default)
BuildRequires:  crate(once-cell-1) >= 1.19.0
BuildRequires:  crate(once-cell-1/default)
BuildRequires:  crate(pyo3-0.26) >= 0.26
BuildRequires:  crate(pyo3-0.26/abi3)
BuildRequires:  crate(pyo3-0.26/abi3-py39)
BuildRequires:  crate(pyo3-0.26/default)
BuildRequires:  crate(pyo3-0.26/py-clone)
BuildRequires:  crate(pyo3-async-runtimes-0.26) >= 0.26
BuildRequires:  crate(pyo3-async-runtimes-0.26/default)
BuildRequires:  crate(pyo3-async-runtimes-0.26/tokio-runtime)
BuildRequires:  crate(rayon-1) >= 1.10
BuildRequires:  crate(rayon-1/default)
BuildRequires:  crate(serde-1) >= 1.0
BuildRequires:  crate(serde-1/default)
BuildRequires:  crate(serde-1/derive)
BuildRequires:  crate(serde-1/rc)
BuildRequires:  crate(serde-json-1) >= 1.0
BuildRequires:  crate(serde-json-1/default)
BuildRequires:  crate(tokio-1) >= 1.47.1
BuildRequires:  crate(tokio-1/default)
BuildRequires:  crate(tokio-1/macros)
BuildRequires:  crate(tokio-1/rt)
BuildRequires:  crate(tokio-1/rt-multi-thread)
BuildRequires:  crate(tokio-1/signal)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Tokenizers provides fast and production-ready tokenization implementations for
modern natural language processing workloads.

%prep -a
rm -f bindings/python/Cargo.lock
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

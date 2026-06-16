# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname watchfiles

Name:           python-%{srcname}
Version:        1.2.0
Release:        %autorelease
Summary:        Simple, modern and high performance file watching and code reload in python.
License:        MIT
URL:            https://github.com/samuelcolvin/watchfiles
#!RemoteAsset:  sha256:a173cb5c16c4f40ab19cecf48a534c409f7ea983ab8fed0741304a1c0a31b3f2
Source0:        https://files.pythonhosted.org/packages/source/w/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  python3dist(maturin)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(puccinialin)
BuildRequires:  python3dist(anyio)
BuildRequires:  crate(crossbeam-channel-0.5) >= 0.5.15
BuildRequires:  crate(crossbeam-channel-0.5/default) >= 0.5.15
BuildRequires:  crate(crossbeam-utils-0.8) >= 0.8.21
BuildRequires:  crate(crossbeam-utils-0.8/std) >= 0.8.21
BuildRequires:  crate(notify-8) >= 8.0.0
BuildRequires:  crate(notify-8/default) >= 8.0.0
BuildRequires:  crate(notify-8/fsevent-sys) >= 8.0.0
BuildRequires:  crate(notify-8/mio) >= 8.0.0
BuildRequires:  crate(bitflags-2/default) >= 2.7.0
BuildRequires:  crate(cfg-if-1/default)
BuildRequires:  crate(filetime-0.2/default)
BuildRequires:  crate(fsevent-sys-4/default) >= 4.0.0
BuildRequires:  crate(inotify-0.11) >= 0.11.0
BuildRequires:  crate(inotify-0.11/default) >= 0.11.0
BuildRequires:  crate(inotify-sys-0.1/default)
BuildRequires:  crate(kqueue-1/default) >= 1.1.1
BuildRequires:  crate(kqueue-sys-1/default)
BuildRequires:  crate(libc-0.2/default)
BuildRequires:  crate(libredox-0.1/default)
BuildRequires:  crate(log-0.4/default) >= 0.4.17
BuildRequires:  crate(mio-1/default) >= 1.0.0
BuildRequires:  crate(mio-1/os-ext) >= 1.0.0
BuildRequires:  crate(notify-types-2/default) >= 2.0.0
BuildRequires:  crate(pyo3-0.28/default) >= 0.28.3
BuildRequires:  crate(pyo3-0.28/extension-module) >= 0.28.3
BuildRequires:  crate(pyo3-0.28/generate-import-lib) >= 0.28.3
BuildRequires:  crate(pyo3-macros-0.28/default) >= 0.28.3
BuildRequires:  crate(pyo3-build-config-0.28/default) >= 0.28.3
BuildRequires:  crate(pyo3-build-config-0.28/resolve-config) >= 0.28.3
BuildRequires:  crate(pyo3-ffi-0.28/default) >= 0.28.3
BuildRequires:  crate(pyo3-ffi-0.28/extension-module) >= 0.28.3
BuildRequires:  crate(pyo3-ffi-0.28/generate-import-lib) >= 0.28.3
BuildRequires:  crate(walkdir-2/default) >= 2.4.0
BuildRequires:  crate(same-file-1/default)
BuildRequires:  crate(winapi-util-0.1/default)
BuildRequires:  crate(wasi-0.11/default)
BuildRequires:  crate(windows-sys-0.52/default)
BuildRequires:  crate(windows-sys-0.59/default)
BuildRequires:  crate(windows-sys-0.60/default)
BuildRequires:  crate(windows-sys-0.61/default)
BuildRequires:  crate(windows-sys-0.61/win32-foundation)
BuildRequires:  crate(windows-sys-0.61/win32-storage-filesystem)
BuildRequires:  crate(windows-sys-0.61/win32-system-console)
BuildRequires:  crate(windows-sys-0.61/win32-system-systeminformation)
BuildRequires:  crate(windows-targets-0.52/default)
BuildRequires:  crate(windows-targets-0.53/default)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Simple, modern and high performance file watching and code reload in python.

%prep -a
mkdir -p ~/.cargo
cat > ~/.cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "system-registry"

[source.system-registry]
directory = "/usr/share/cargo/registry"
EOF
rm -f Cargo.lock

%build -p
%ifarch riscv64
# Work around rustc ICE on rva23 while optimizing pyo3 0.28.x
# in release mode. The failure happens in rustc MIR optimization with
# -C opt-level=3, before package-specific code is relevant.
export RUST_MIN_STACK=16777216
export CARGO_PROFILE_RELEASE_OPT_LEVEL=2
export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=256
%endif

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/watchfiles

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustc-demangle
%global full_version 0.1.24
%global pkgname rustc-demangle-0.1

Name:           rust-rustc-demangle-0.1
Version:        0.1.24
Release:        %autorelease
Summary:        Rust crate "rustc-demangle"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/rustc-demangle
#!RemoteAsset:  sha256:719b953e2095829ee67db738b3bfa9fa368c94900df327b3f07fe6e794d2fe1f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "rustc-demangle"

%package     -n %{name}+compiler-builtins
Summary:        Rust compiler symbol demangling - feature "compiler_builtins"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(compiler-builtins-0.1/default) >= 0.1.2
Provides:       crate(%{pkgname}/compiler-builtins) = %{version}

%description -n %{name}+compiler-builtins
This metapackage enables feature "compiler_builtins" for the Rust rustc-demangle crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+core
Summary:        Rust compiler symbol demangling - feature "core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustc-std-workspace-core-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/core) = %{version}

%description -n %{name}+core
This metapackage enables feature "core" for the Rust rustc-demangle crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Rust compiler symbol demangling - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/compiler-builtins) = %{version}
Requires:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust rustc-demangle crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

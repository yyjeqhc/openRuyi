# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cfg-if
%global full_version 1.0.0
%global pkgname cfg-if-1

Name:           rust-cfg-if-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "cfg-if"
License:        MIT OR Apache-2.0
URL:            https://github.com/alexcrichton/cfg-if
#!RemoteAsset:  sha256:baf1de4339761588bc0619e3cbc0120ee582ebb74b53b4efbf79117bd2da40fd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Structured like an if-else chain, the first matching branch is the item that gets emitted.
Source code for takopackized Rust crate "cfg-if"

%package     -n %{name}+compiler-builtins
Summary:        Macro to ergonomically define an item depending on a large number of #[cfg] parameters - feature "compiler_builtins"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(compiler-builtins-0.1/default) >= 0.1.2
Provides:       crate(%{pkgname}/compiler-builtins) = %{version}

%description -n %{name}+compiler-builtins
Structured like an if-else chain, the first matching branch is the item that gets emitted.
This metapackage enables feature "compiler_builtins" for the Rust cfg-if crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+core
Summary:        Macro to ergonomically define an item depending on a large number of #[cfg] parameters - feature "core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustc-std-workspace-core-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/core) = %{version}

%description -n %{name}+core
Structured like an if-else chain, the first matching branch is the item that gets emitted.
This metapackage enables feature "core" for the Rust cfg-if crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Macro to ergonomically define an item depending on a large number of #[cfg] parameters - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/compiler-builtins) = %{version}
Requires:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description -n %{name}+rustc-dep-of-std
Structured like an if-else chain, the first matching branch is the item that gets emitted.
This metapackage enables feature "rustc-dep-of-std" for the Rust cfg-if crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode-width
%global full_version 0.2.0
%global pkgname unicode-width-0.2

Name:           rust-unicode-width-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "unicode-width"
License:        MIT OR Apache-2.0
URL:            https://github.com/unicode-rs/unicode-width
#!RemoteAsset:  sha256:1fc81956842c57dac11422a97c3b8195a1ff727f06e85c84ed2e8aa277c9a0fd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/cjk) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/no-std) = %{version}

%description
Source code for takopackized Rust crate "unicode-width"

%package     -n %{name}+compiler-builtins
Summary:        Determine displayed width of `char` and `str` types according to Unicode Standard Annex #11 rules - feature "compiler_builtins"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(compiler-builtins-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/compiler-builtins) = %{version}

%description -n %{name}+compiler-builtins
This metapackage enables feature "compiler_builtins" for the Rust unicode-width crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+core
Summary:        Determine displayed width of `char` and `str` types according to Unicode Standard Annex #11 rules - feature "core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustc-std-workspace-core-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/core) = %{version}

%description -n %{name}+core
This metapackage enables feature "core" for the Rust unicode-width crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Determine displayed width of `char` and `str` types according to Unicode Standard Annex #11 rules - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/compiler-builtins) = %{version}
Requires:       crate(%{pkgname}/core) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust unicode-width crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Determine displayed width of `char` and `str` types according to Unicode Standard Annex #11 rules - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustc-std-workspace-std-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust unicode-width crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

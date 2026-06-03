# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num_enum_derive
%global full_version 0.7.6
%global pkgname num-enum-derive-0.7

Name:           rust-num-enum-derive-0.7
Version:        0.7.6
Release:        %autorelease
Summary:        Rust crate "num_enum_derive"
License:        BSD-3-Clause OR MIT OR Apache-2.0
URL:            https://github.com/illicitonion/num_enum
#!RemoteAsset:  sha256:680998035259dcfcafe653688bf2aa6d3e2dc05e98be6ab46afb089dc84f1df8
Source:         https://static.crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/derive) >= 2.0.117
Requires:       crate(syn-2.0/extra-traits) >= 2.0.117
Requires:       crate(syn-2.0/parsing) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/external-doc)

%description
Source code for takopackized Rust crate "num_enum_derive"

%package     -n %{name}+complex-expressions
Summary:        Internal implementation details for ::num_enum (Procedural macros to make inter-operation between primitives and enums easier) - feature "complex-expressions"
Requires:       crate(%{pkgname})
Requires:       crate(syn-2.0/derive) >= 2.0.117
Requires:       crate(syn-2.0/extra-traits) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Requires:       crate(syn-2.0/parsing) >= 2.0.117
Provides:       crate(%{pkgname}/complex-expressions)

%description -n %{name}+complex-expressions
This metapackage enables feature "complex-expressions" for the Rust num_enum_derive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proc-macro-crate
Summary:        Internal implementation details for ::num_enum (Procedural macros to make inter-operation between primitives and enums easier) - feature "proc-macro-crate" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(proc-macro-crate-3.0/default) >= 3.5.0
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/proc-macro-crate)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+proc-macro-crate
This metapackage enables feature "proc-macro-crate" for the Rust num_enum_derive crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "std" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

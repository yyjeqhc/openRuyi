# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zvariant_derive
%global full_version 5.12.0
%global pkgname zvariant-derive-5.0

Name:           rust-zvariant-derive-5.0
Version:        5.12.0
Release:        %autorelease
Summary:        Rust crate "zvariant_derive"
License:        MIT
URL:            https://github.com/z-galaxy/zbus/
#!RemoteAsset:  sha256:90bc6cde9c01c511074be97f7ccb6c19d0da89e3f8662e812e999dcfd4638737
Source:         https://static.crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro-crate-3.0/default) >= 3.5.0
Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/extra-traits) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Requires:       crate(zvariant-utils-3.0/default) >= 3.4.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "zvariant_derive"

%package     -n %{name}+gvariant
Summary:        D-Bus & GVariant encoding & decoding - feature "gvariant"
Requires:       crate(%{pkgname})
Requires:       crate(zvariant-utils-3.0/gvariant) >= 3.4.0
Provides:       crate(%{pkgname}/gvariant)

%description -n %{name}+gvariant
This metapackage enables feature "gvariant" for the Rust zvariant_derive crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zbus_macros
%global full_version 5.16.0
%global pkgname zbus-macros-5.0

Name:           rust-zbus-macros-5.0
Version:        5.16.0
Release:        %autorelease
Summary:        Rust crate "zbus_macros"
License:        MIT
URL:            https://github.com/z-galaxy/zbus/
#!RemoteAsset:  sha256:adf1bd45a81a103745b1757754762a26e8cd01e4532e4d6c8ec431624b80d1d6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro-crate-3.0/default) >= 3.5.0
Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/extra-traits) >= 2.0.117
Requires:       crate(syn-2.0/fold) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Requires:       crate(zbus-names-4.0/default) >= 4.3.2
Requires:       crate(zvariant-5.0/default) >= 5.12.0
Requires:       crate(zvariant-utils-3.0/default) >= 3.4.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/blocking-api)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "zbus_macros"

%package     -n %{name}+gvariant
Summary:        Proc-macros for zbus - feature "gvariant"
Requires:       crate(%{pkgname})
Requires:       crate(zvariant-5.0/gvariant) >= 5.12.0
Requires:       crate(zvariant-utils-3.0/gvariant) >= 3.4.0
Provides:       crate(%{pkgname}/gvariant)

%description -n %{name}+gvariant
This metapackage enables feature "gvariant" for the Rust zbus_macros crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

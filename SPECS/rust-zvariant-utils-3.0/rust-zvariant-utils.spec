# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zvariant_utils
%global full_version 3.3.1
%global pkgname zvariant-utils-3.0

Name:           rust-zvariant-utils-3.0
Version:        3.3.1
Release:        %autorelease
Summary:        Rust crate "zvariant_utils"
License:        MIT
URL:            https://github.com/z-galaxy/zbus/
#!RemoteAsset:  sha256:6d464f5733ffa07a3164d656f18533caace9d0638596721355d73256a410d691
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(syn-2/default) >= 2.0.117
Requires:       crate(syn-2/extra-traits) >= 2.0.117
Requires:       crate(syn-2/full) >= 2.0.117
Requires:       crate(winnow-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/gvariant)

%description
Source code for takopackized Rust crate "zvariant_utils"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

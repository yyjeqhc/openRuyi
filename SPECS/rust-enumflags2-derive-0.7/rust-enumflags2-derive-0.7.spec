# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name enumflags2_derive
%global full_version 0.7.12
%global pkgname enumflags2-derive-0.7

Name:           rust-enumflags2-derive-0.7
Version:        0.7.12
Release:        %autorelease
Summary:        Rust crate "enumflags2_derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/meithecatte/enumflags2
#!RemoteAsset:  sha256:67c78a4d8fdf9953a5c9d458f9efe940fd97a0cab0941c075a813ac594733827
Source:         https://static.crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/derive) >= 2.0.117
Requires:       crate(syn-2.0/parsing) >= 2.0.117
Requires:       crate(syn-2.0/printing) >= 2.0.117
Requires:       crate(syn-2.0/proc-macro) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
This allows for better compatibility across versions.
Source code for takopackized Rust crate "enumflags2_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

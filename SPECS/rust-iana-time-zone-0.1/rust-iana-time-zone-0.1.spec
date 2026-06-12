# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name iana-time-zone
%global full_version 0.1.65
%global pkgname iana-time-zone-0.1

Name:           rust-iana-time-zone-0.1
Version:        0.1.65
Release:        %autorelease
Summary:        Rust crate "iana-time-zone"
License:        MIT OR Apache-2.0
URL:            https://github.com/strawlab/iana-time-zone
#!RemoteAsset:  sha256:e31bc9ad994ba00e440a8aa5c9ef0ec67d5cb5e5cb0cc7f8b744a35b389cc470
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/fallback) = %{version}

%description
Source code for takopackized Rust crate "iana-time-zone"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

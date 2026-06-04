# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fdt
%global full_version 0.2.0-alpha2
%global pkgname fdt-0.2.0-alpha2

Name:           rust-fdt-0.2.0-alpha2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "fdt"
License:        MPL-2.0
URL:            https://github.com/repnop/fdt
#!RemoteAsset:  sha256:c8ccfb5c9d9425b2191070f0435636f4a9cdfedd107e33b15f861622b222726a
Source:         https://static.crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/linux-dt-bindings)
Provides:       crate(%{pkgname}/pretty-printing)

%description
Source code for takopackized Rust crate "fdt"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

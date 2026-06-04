# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name acpi_tables
%global full_version 0.2.1
%global pkgname acpi-tables-0.2

Name:           rust-acpi-tables-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "acpi_tables"
License:        Apache-2.0
URL:            https://github.com/rust-vmm/acpi_tables
#!RemoteAsset:  sha256:ce821f856a3eb1d033287f2dcfcdf94276d7895dd5bdd8ca45ae17e7d33d4dd9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(zerocopy-0.8/default) >= 0.8.50
Requires:       crate(zerocopy-0.8/derive) >= 0.8.50
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "acpi_tables"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

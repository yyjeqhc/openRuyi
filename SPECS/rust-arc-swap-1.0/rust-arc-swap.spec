# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arc-swap
%global full_version 1.9.1
%global pkgname arc-swap-1.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-arc-swap-1.0
Version:        1.9.1
Release:        %autorelease
Summary:        Rust crate "arc-swap"
License:        MIT OR Apache-2.0
URL:            https://github.com/vorner/arc-swap
#!RemoteAsset:  sha256:6a3a1fd6f75306b68087b831f025c712524bcb19aad54e557b1129cfa0a2b207
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(rustversion-1.0/default) >= 1.0.22
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/experimental-strategies)
Provides:       crate(%{pkgname}/experimental-thread-local)
Provides:       crate(%{pkgname}/internal-test-strategies)
Provides:       crate(%{pkgname}/weak)

%description
Source code for takopackized Rust crate "arc-swap"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

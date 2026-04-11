# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name openssl-src
%global full_version 300.6.0+3.6.2
%global pkgname openssl-src-300.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-openssl-src-300.0
Version:        300.6.0
Release:        %autorelease
Summary:        Rust crate "openssl-src"
License:        MIT/Apache-2.0
URL:            https://github.com/alexcrichton/openssl-src-rs
#!RemoteAsset:  sha256:a8e8cbfd3a4a8c8f089147fd7aaa33cf8c7450c4d09f8f80698a0cf093abeff4
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(cc-1.0/default) >= 1.2.60
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/camellia)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/force-engine)
Provides:       crate(%{pkgname}/idea)
Provides:       crate(%{pkgname}/ktls)
Provides:       crate(%{pkgname}/legacy)
Provides:       crate(%{pkgname}/no-dso)
Provides:       crate(%{pkgname}/seed)
Provides:       crate(%{pkgname}/ssl3)
Provides:       crate(%{pkgname}/weak-crypto)

%description
Source code for takopackized Rust crate "openssl-src"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

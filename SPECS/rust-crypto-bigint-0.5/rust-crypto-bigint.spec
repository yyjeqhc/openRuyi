# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crypto-bigint
%global full_version 0.5.5
%global pkgname crypto-bigint-0.5

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-crypto-bigint-0.5
Version:        0.5.5
Release:        %autorelease
Summary:        Rust crate "crypto-bigint"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/crypto-bigint
#!RemoteAsset:  sha256:0dc92fb57ca44df6db8059111ab3af99a63d5d0f8375d9972e319a379c6bab76
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(subtle-2.0) >= 2.6.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/extra-sizes)

%description
Provides constant-time, no_std-friendly implementations of modern formulas using const generics.
Source code for takopackized Rust crate "crypto-bigint"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

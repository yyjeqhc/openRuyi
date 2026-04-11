# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zlib-rs
%global full_version 0.6.3
%global pkgname zlib-rs-0.6

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-zlib-rs-0.6
Version:        0.6.3
Release:        %autorelease
Summary:        Rust crate "zlib-rs"
License:        Zlib
URL:            https://github.com/trifectatechfoundation/zlib-rs
#!RemoteAsset:  sha256:3be3d40e40a133f9c916ee3f9f4fa2d9d63435b5fbe1bfc6d9dae0aa0ada1513
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/zlib-debug)
Provides:       crate(%{pkgname}/internal-api)
Provides:       crate(%{pkgname}/internal-fuzz-disable-checksum)
Provides:       crate(%{pkgname}/avx512)
Provides:       crate(%{pkgname}/c-allocator)
Provides:       crate(%{pkgname}/rust-allocator)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/vpclmulqdq)

%description
Source code for takopackized Rust crate "zlib-rs"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

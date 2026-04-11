# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name flate2
%global full_version 1.1.9
%global pkgname flate2-1.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-flate2-1.0
Version:        1.1.9
Release:        %autorelease
Summary:        Rust crate "flate2"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/flate2-rs
#!RemoteAsset:  sha256:843fba2746e448b37e26a819579957415c8cef339bf08564fe8b7ddbd959573c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(miniz-oxide-0.8/simd) >= 0.8.9
Requires:       crate(miniz-oxide-0.8/with-alloc) >= 0.8.9
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/any-c-zlib)
Provides:       crate(%{pkgname}/any-impl)
Provides:       crate(%{pkgname}/any-zlib)

%description
Supports miniz_oxide and multiple zlib implementations. Supports zlib, gzip, and raw deflate streams.
Source code for takopackized Rust crate "flate2"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

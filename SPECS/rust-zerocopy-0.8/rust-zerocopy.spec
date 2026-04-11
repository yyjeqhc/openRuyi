# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zerocopy
%global full_version 0.8.48
%global pkgname zerocopy-0.8

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-zerocopy-0.8
Version:        0.8.48
Release:        %autorelease
Summary:        Rust crate "zerocopy"
License:        BSD-2-Clause OR Apache-2.0 OR MIT
URL:            https://github.com/google/zerocopy
#!RemoteAsset:  sha256:eed437bf9d6692032087e337407a86f04cd8d6a16a37199ed57949d415bd68e9
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(zerocopy-derive-0.8/default) >= 0.8.48
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/float-nightly)
Provides:       crate(%{pkgname}/simd)
Provides:       crate(%{pkgname}/simd-nightly)
Provides:       crate(%{pkgname}/std)

%description
We write "unsafe" so you don't have to.
Source code for takopackized Rust crate "zerocopy"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

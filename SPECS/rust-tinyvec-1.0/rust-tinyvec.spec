# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tinyvec
%global full_version 1.11.0
%global pkgname tinyvec-1.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-tinyvec-1.0
Version:        1.11.0
Release:        %autorelease
Summary:        Rust crate "tinyvec"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/Lokathor/tinyvec
#!RemoteAsset:  sha256:3e61e67053d25a4e82c844e8424039d9745781b3fc4f32b8d55ed50f5f667ef3
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/debugger-visualizer)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/experimental-write-impl)
Provides:       crate(%{pkgname}/grab-spare-slice)
Provides:       crate(%{pkgname}/latest-stable-rust)
Provides:       crate(%{pkgname}/nightly-slice-partition-dedup)
Provides:       crate(%{pkgname}/real-blackbox)
Provides:       crate(%{pkgname}/rustc-1-40)
Provides:       crate(%{pkgname}/rustc-1-55)
Provides:       crate(%{pkgname}/rustc-1-57)
Provides:       crate(%{pkgname}/rustc-1-61)

%description
Source code for takopackized Rust crate "tinyvec"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

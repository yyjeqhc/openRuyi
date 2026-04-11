# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name typenum
%global full_version 1.19.0
%global pkgname typenum-1.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-typenum-1.0
Version:        1.19.0
Release:        %autorelease
Summary:        Rust crate "typenum"
License:        MIT OR Apache-2.0
URL:            https://github.com/paholg/typenum
#!RemoteAsset:  sha256:562d481066bde0658276a35467c4af00bdc6ee726305698a55b86e61d7ad82bb
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/const-generics)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/force-unix-path-separator)
Provides:       crate(%{pkgname}/i128)
Provides:       crate(%{pkgname}/no-std)
Provides:       crate(%{pkgname}/strict)

%description
It currently supports bits, unsigned integers, and signed     integers. It also provides a type-level array of type-level numbers, but its     implementation is incomplete.
Source code for takopackized Rust crate "typenum"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

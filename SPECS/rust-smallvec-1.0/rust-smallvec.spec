# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name smallvec
%global full_version 1.15.1
%global pkgname smallvec-1.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-smallvec-1.0
Version:        1.15.1
Release:        %autorelease
Summary:        Rust crate "smallvec"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/rust-smallvec
#!RemoteAsset:  sha256:67b1b7a3b5fe4f1376887184045fcf45c69e92af734b7aaddc05fb777b6fbd03
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/const-generics)
Provides:       crate(%{pkgname}/const-new)
Provides:       crate(%{pkgname}/debugger-visualizer)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/drain-filter)
Provides:       crate(%{pkgname}/drain-keep-rest)
Provides:       crate(%{pkgname}/may-dangle)
Provides:       crate(%{pkgname}/specialization)
Provides:       crate(%{pkgname}/union)
Provides:       crate(%{pkgname}/write)

%description
Source code for takopackized Rust crate "smallvec"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name portable-atomic
%global full_version 1.13.1
%global pkgname portable-atomic-1.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-portable-atomic-1.0
Version:        1.13.1
Release:        %autorelease
Summary:        Rust crate "portable-atomic"
License:        Apache-2.0 OR MIT
URL:            https://github.com/taiki-e/portable-atomic
#!RemoteAsset:  sha256:c33a9471896f1c69cecef8d20cbe2f7accd12527ce60845ff44c153bb2a21b49
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/disable-fiq)
Provides:       crate(%{pkgname}/fallback)
Provides:       crate(%{pkgname}/float)
Provides:       crate(%{pkgname}/force-amo)
Provides:       crate(%{pkgname}/require-cas)
Provides:       crate(%{pkgname}/s-mode)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unsafe-assume-privileged)
Provides:       crate(%{pkgname}/unsafe-assume-single-core)

%description
Source code for takopackized Rust crate "portable-atomic"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

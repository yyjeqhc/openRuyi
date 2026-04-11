# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name erased-serde
%global full_version 0.4.10
%global pkgname erased-serde-0.4

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-erased-serde-0.4
Version:        0.4.10
Release:        %autorelease
Summary:        Rust crate "erased-serde"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/erased-serde
#!RemoteAsset:  sha256:d2add8a07dd6a8d93ff627029c51de145e12686fbc36ecb298ac22e74cf02dec
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(serde-1.0) >= 1.0.228
Requires:       crate(serde-core-1.0) >= 1.0.228
Requires:       crate(typeid-1.0/default) >= 1.0.3
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/unstable-debug)

%description
Source code for takopackized Rust crate "erased-serde"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

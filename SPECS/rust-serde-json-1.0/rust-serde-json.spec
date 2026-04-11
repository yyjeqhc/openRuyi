# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_json
%global full_version 1.0.149
%global pkgname serde-json-1.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-serde-json-1.0
Version:        1.0.149
Release:        %autorelease
Summary:        Rust crate "serde_json"
License:        MIT OR Apache-2.0
URL:            https://github.com/serde-rs/json
#!RemoteAsset:  sha256:83fc039473c5595ace860d8c4fafa220ff474b3fc6bfdb4293327f1a37e94d86
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(itoa-1.0/default) >= 1.0.18
Requires:       crate(memchr-2.0) >= 2.8.0
Requires:       crate(serde-1.0) >= 1.0.228
Requires:       crate(serde-core-1.0) >= 1.0.228
Requires:       crate(zmij-1.0/default) >= 1.0.21
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/arbitrary-precision)
Provides:       crate(%{pkgname}/float-roundtrip)
Provides:       crate(%{pkgname}/raw-value)
Provides:       crate(%{pkgname}/unbounded-depth)

%description
Source code for takopackized Rust crate "serde_json"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

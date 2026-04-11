# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name icu_properties
%global full_version 2.2.0
%global pkgname icu-properties-2.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-icu-properties-2.0
Version:        2.2.0
Release:        %autorelease
Summary:        Rust crate "icu_properties"
License:        Unicode-3.0
URL:            https://icu4x.unicode.org
#!RemoteAsset:  sha256:bee3b67d0ea5c2cca5003417989af8996f8604e34fb9ddf96208a033901e70de
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(icu-collections-2.0) >= 2.2.0
Requires:       crate(icu-locale-core-2.0/zerovec) >= 2.2.0
Requires:       crate(icu-provider-2.0) >= 2.2.0
Requires:       crate(zerotrie-0.2/yoke) >= 0.2.4
Requires:       crate(zerotrie-0.2/zerofrom) >= 0.2.4
Requires:       crate(zerovec-0.11/derive) >= 0.11.6
Requires:       crate(zerovec-0.11/yoke) >= 0.11.6
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "icu_properties"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

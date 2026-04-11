# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zerofrom-derive
%global full_version 0.1.7
%global pkgname zerofrom-derive-0.1

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-zerofrom-derive-0.1
Version:        0.1.7
Release:        %autorelease
Summary:        Rust crate "zerofrom-derive"
License:        Unicode-3.0
URL:            https://github.com/unicode-org/icu4x
#!RemoteAsset:  sha256:11532158c46691caf0f2593ea8358fed6bbf68a0315e80aae9bd41fbade684a1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/fold) >= 2.0.117
Requires:       crate(synstructure-0.13/default) >= 0.13.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "zerofrom-derive"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

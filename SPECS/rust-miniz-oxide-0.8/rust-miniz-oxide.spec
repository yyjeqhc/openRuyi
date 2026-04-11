# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name miniz_oxide
%global full_version 0.8.9
%global pkgname miniz-oxide-0.8

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-miniz-oxide-0.8
Version:        0.8.9
Release:        %autorelease
Summary:        Rust crate "miniz_oxide"
License:        MIT OR Zlib OR Apache-2.0
URL:            https://github.com/Frommi/miniz_oxide/tree/master/miniz_oxide
#!RemoteAsset:  sha256:1fa76a2c86f704bdb222d66965fb3d63269ce38518b83cb0575fca855ebb6316
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(adler2-2.0) >= 2.0.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/block-boundary)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/with-alloc)

%description
Source code for takopackized Rust crate "miniz_oxide"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

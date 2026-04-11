# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-object
%global full_version 0.58.0
%global pkgname gix-object-0.58

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-gix-object-0.58
Version:        0.58.0
Release:        %autorelease
Summary:        Rust crate "gix-object"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:cafb802bb688a7c1e69ef965612ff5ff859f046bfb616377e4a0ba4c01e43d47
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(bstr-1.0/unicode) >= 1.12.1
Requires:       crate(gix-actor-0.40/default) >= 0.40.0
Requires:       crate(gix-date-0.15/default) >= 0.15.1
Requires:       crate(gix-features-0.46/default) >= 0.46.2
Requires:       crate(gix-features-0.46/progress) >= 0.46.2
Requires:       crate(gix-hash-0.23/default) >= 0.23.0
Requires:       crate(gix-hashtable-0.13/default) >= 0.13.0
Requires:       crate(gix-path-0.11/default) >= 0.11.2
Requires:       crate(gix-utils-0.3/default) >= 0.3.1
Requires:       crate(gix-validate-0.11/default) >= 0.11.0
Requires:       crate(itoa-1.0/default) >= 1.0.18
Requires:       crate(smallvec-1.0/default) >= 1.15.1
Requires:       crate(smallvec-1.0/write) >= 1.15.1
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Requires:       crate(winnow-0.7/default) >= 0.7.15
Requires:       crate(winnow-0.7/simd) >= 0.7.15
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-object"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

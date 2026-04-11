# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-attributes
%global full_version 0.29.0
%global pkgname gix-attributes-0.29

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-gix-attributes-0.29
Version:        0.29.0
Release:        %autorelease
Summary:        Rust crate "gix-attributes"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:f47dabf8a50f1558c3a55d978440c7c4f22f87ac897bef03b4edbc96f6115966
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(bstr-1.0/unicode) >= 1.12.1
Requires:       crate(gix-glob-0.23/default) >= 0.23.0
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(gix-quote-0.6/default) >= 0.6.2
Requires:       crate(gix-trace-0.1/default) >= 0.1.18
Requires:       crate(kstring-2.0/default) >= 2.0.2
Requires:       crate(smallvec-1.0/default) >= 1.15.1
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Requires:       crate(unicode-bom-2.0/default) >= 2.0.3
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-attributes"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

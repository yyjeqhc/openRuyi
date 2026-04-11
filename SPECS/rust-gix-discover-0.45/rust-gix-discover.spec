# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-discover
%global full_version 0.45.0
%global pkgname gix-discover-0.45

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-gix-discover-0.45
Version:        0.45.0
Release:        %autorelease
Summary:        Rust crate "gix-discover"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:42ce096dc132533802a09d6fd5d4008858f2038341dfe2e69e0d0239edb359de
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(bstr-1.0/unicode) >= 1.12.1
Requires:       crate(dunce-1.0/default) >= 1.0.5
Requires:       crate(gix-fs-0.18/default) >= 0.18.2
Requires:       crate(gix-hash-0.21/default) >= 0.21.2
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(gix-ref-0.57/default) >= 0.57.0
Requires:       crate(gix-sec-0.12/default) >= 0.12.2
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-discover"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

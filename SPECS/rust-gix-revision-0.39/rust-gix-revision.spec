# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-revision
%global full_version 0.39.0
%global pkgname gix-revision-0.39

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-gix-revision-0.39
Version:        0.39.0
Release:        %autorelease
Summary:        Rust crate "gix-revision"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:91898c83b18c635696f7355d171cfa74a52f38022ff89581f567768935ebc4c8
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(gix-commitgraph-0.31/default) >= 0.31.0
Requires:       crate(gix-date-0.12/default) >= 0.12.1
Requires:       crate(gix-hash-0.21/default) >= 0.21.2
Requires:       crate(gix-object-0.54/default) >= 0.54.1
Requires:       crate(gix-revwalk-0.25/default) >= 0.25.0
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "gix-revision"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

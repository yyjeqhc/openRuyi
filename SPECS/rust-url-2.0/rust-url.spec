# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name url
%global full_version 2.5.8
%global pkgname url-2.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-url-2.0
Version:        2.5.8
Release:        %autorelease
Summary:        Rust crate "url"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/rust-url
#!RemoteAsset:  sha256:ff67a8a4397373c3ef660812acab3268222035010ab8680ec4215f38ba3d0eed
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(form-urlencoded-1.0/alloc) >= 1.2.2
Requires:       crate(idna-1.0/alloc) >= 1.1.0
Requires:       crate(idna-1.0/compiled-data) >= 1.1.0
Requires:       crate(percent-encoding-2.0/alloc) >= 2.3.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/debugger-visualizer)
Provides:       crate(%{pkgname}/expose-internals)

%description
Source code for takopackized Rust crate "url"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

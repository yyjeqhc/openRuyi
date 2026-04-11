# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde-untagged
%global full_version 0.1.9
%global pkgname serde-untagged-0.1

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-serde-untagged-0.1
Version:        0.1.9
Release:        %autorelease
Summary:        Rust crate "serde-untagged"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/serde-untagged
#!RemoteAsset:  sha256:f9faf48a4a2d2693be24c6289dbe26552776eb7737074e6722891fadbe6c5058
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(erased-serde-0.4/alloc) >= 0.4.10
Requires:       crate(serde-1.0) >= 1.0.228
Requires:       crate(serde-core-1.0/alloc) >= 1.0.228
Requires:       crate(typeid-1.0/default) >= 1.0.3
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "serde-untagged"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dashmap
%global full_version 6.1.0
%global pkgname dashmap-6.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-dashmap-6.0
Version:        6.1.0
Release:        %autorelease
Summary:        Rust crate "dashmap"
License:        MIT
URL:            https://github.com/xacrimon/dashmap
#!RemoteAsset:  sha256:5041cc499144891f3790297212f32a74fb938e5136a14943f338ef9e0ae276cf
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(crossbeam-utils-0.8/default) >= 0.8.21
Requires:       crate(hashbrown-0.14/raw) >= 0.14.5
Requires:       crate(lock-api-0.4/default) >= 0.4.14
Requires:       crate(once-cell-1.0/default) >= 1.21.4
Requires:       crate(parking-lot-core-0.9/default) >= 0.9.12
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/raw-api)

%description
Source code for takopackized Rust crate "dashmap"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

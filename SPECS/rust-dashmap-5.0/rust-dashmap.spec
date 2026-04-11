# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dashmap
%global full_version 5.5.3
%global pkgname dashmap-5.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-dashmap-5.0
Version:        5.5.3
Release:        %autorelease
Summary:        Rust crate "dashmap"
License:        MIT
URL:            https://github.com/xacrimon/dashmap
#!RemoteAsset:  sha256:978747c1d849a7d2ee5e8adc0159961c48fb7e5db2f06af6723b80123bb53856
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(hashbrown-0.14) >= 0.14.5
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

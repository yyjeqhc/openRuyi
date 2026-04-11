# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-config
%global full_version 0.50.0
%global pkgname gix-config-0.50

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-gix-config-0.50
Version:        0.50.0
Release:        %autorelease
Summary:        Rust crate "gix-config"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:b58e2ff8eef96b71f2c5e260f02ca0475caff374027c5cc5a29bda69fac67404
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(gix-config-value-0.16/default) >= 0.16.0
Requires:       crate(gix-features-0.45/default) >= 0.45.2
Requires:       crate(gix-glob-0.23/default) >= 0.23.0
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(gix-ref-0.57/default) >= 0.57.0
Requires:       crate(gix-sec-0.12/default) >= 0.12.2
Requires:       crate(memchr-2.0/default) >= 2.8.0
Requires:       crate(smallvec-1.0/default) >= 1.15.1
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Requires:       crate(unicode-bom-2.0/default) >= 2.0.3
Requires:       crate(winnow-0.7/default) >= 0.7.15
Requires:       crate(winnow-0.7/simd) >= 0.7.15
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-config"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

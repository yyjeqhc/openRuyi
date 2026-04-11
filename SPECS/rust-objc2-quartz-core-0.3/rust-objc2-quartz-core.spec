# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-quartz-core
%global full_version 0.3.2
%global pkgname objc2-quartz-core-0.3

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-objc2-quartz-core-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "objc2-quartz-core"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:96c1358452b371bf9f104e21ec536d37a650eb10f7ee379fff67d2e08d537f1f
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(objc2-0.6/std) >= 0.6.4
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/cabase)
Provides:       crate(%{pkgname}/caeagllayer)
Provides:       crate(%{pkgname}/caframeraterange)
Provides:       crate(%{pkgname}/caremotelayerclient)
Provides:       crate(%{pkgname}/caremotelayerserver)
Provides:       crate(%{pkgname}/coreanimation)
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/gnustep-1-7)
Provides:       crate(%{pkgname}/gnustep-1-8)
Provides:       crate(%{pkgname}/gnustep-1-9)
Provides:       crate(%{pkgname}/gnustep-2-0)
Provides:       crate(%{pkgname}/gnustep-2-1)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unstable-darwin-objc)

%description
Source code for takopackized Rust crate "objc2-quartz-core"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

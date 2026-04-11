# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-core-graphics
%global full_version 0.3.2
%global pkgname objc2-core-graphics-0.3

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-objc2-core-graphics-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "objc2-core-graphics"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:e022c9d066895efa1345f8e33e584b9f958da2fd4cd116792e15e07e4720a807
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(objc2-core-foundation-0.3) >= 0.3.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/cgbase)
Provides:       crate(%{pkgname}/cgdirectdisplaymetal)
Provides:       crate(%{pkgname}/cgdirectpalette)
Provides:       crate(%{pkgname}/cgdisplayfade)
Provides:       crate(%{pkgname}/cgerror)
Provides:       crate(%{pkgname}/cgitutonemapping)
Provides:       crate(%{pkgname}/cgpdfoperatortable)
Provides:       crate(%{pkgname}/cgwindowlevel)
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unstable-darwin-objc)

%description
Source code for takopackized Rust crate "objc2-core-graphics"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

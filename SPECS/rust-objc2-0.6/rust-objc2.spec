# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2
%global full_version 0.6.4
%global pkgname objc2-0.6

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-objc2-0.6
Version:        0.6.4
Release:        %autorelease
Summary:        Rust crate "objc2"
License:        MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:3a12a8ed07aefc768292f076dc3ac8c48f3781c8f2d5851dd3d98950e8c5a89f
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(objc2-encode-4.0) >= 4.1.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/disable-encoding-assertions)
Provides:       crate(%{pkgname}/objc2-proc-macros)
Provides:       crate(%{pkgname}/relax-sign-encoding)
Provides:       crate(%{pkgname}/relax-void-encoding)
Provides:       crate(%{pkgname}/unstable-apple-new)
Provides:       crate(%{pkgname}/unstable-arbitrary-self-types)
Provides:       crate(%{pkgname}/unstable-autoreleasesafe)
Provides:       crate(%{pkgname}/unstable-coerce-pointee)
Provides:       crate(%{pkgname}/unstable-darwin-objc)
Provides:       crate(%{pkgname}/unstable-objfw)
Provides:       crate(%{pkgname}/unstable-requires-macos)
Provides:       crate(%{pkgname}/verify)

%description
Source code for takopackized Rust crate "objc2"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

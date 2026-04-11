# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-core-foundation
%global full_version 0.3.2
%global pkgname objc2-core-foundation-0.3

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-objc2-core-foundation-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "objc2-core-foundation"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:2a180dd8642fa45cdb7dd721cd4c11b1cadd4929ce112ebd8b9f5803cc79d536
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/cfarray)
Provides:       crate(%{pkgname}/cfattributedstring)
Provides:       crate(%{pkgname}/cfavailability)
Provides:       crate(%{pkgname}/cfbag)
Provides:       crate(%{pkgname}/cfbase)
Provides:       crate(%{pkgname}/cfbinaryheap)
Provides:       crate(%{pkgname}/cfbitvector)
Provides:       crate(%{pkgname}/cfbundle)
Provides:       crate(%{pkgname}/cfbyteorder)
Provides:       crate(%{pkgname}/cfcgtypes)
Provides:       crate(%{pkgname}/cfcharacterset)
Provides:       crate(%{pkgname}/cfdictionary)
Provides:       crate(%{pkgname}/cferror)
Provides:       crate(%{pkgname}/cffiledescriptor)
Provides:       crate(%{pkgname}/cflocale)
Provides:       crate(%{pkgname}/cfmachport)
Provides:       crate(%{pkgname}/cfmessageport)
Provides:       crate(%{pkgname}/cfnotificationcenter)
Provides:       crate(%{pkgname}/cfnumber)
Provides:       crate(%{pkgname}/cfplugin)
Provides:       crate(%{pkgname}/cfplugincom)
Provides:       crate(%{pkgname}/cfpreferences)
Provides:       crate(%{pkgname}/cfset)
Provides:       crate(%{pkgname}/cfstringencodingext)
Provides:       crate(%{pkgname}/cftimezone)
Provides:       crate(%{pkgname}/cftree)
Provides:       crate(%{pkgname}/cfurlaccess)
Provides:       crate(%{pkgname}/cfuuid)
Provides:       crate(%{pkgname}/cfusernotification)
Provides:       crate(%{pkgname}/cfutilities)
Provides:       crate(%{pkgname}/cfxmlnode)
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unstable-coerce-pointee)
Provides:       crate(%{pkgname}/unstable-darwin-objc)

%description
Source code for takopackized Rust crate "objc2-core-foundation"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

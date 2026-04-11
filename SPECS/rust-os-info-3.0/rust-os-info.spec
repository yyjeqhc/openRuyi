# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name os_info
%global full_version 3.14.0
%global pkgname os-info-3.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-os-info-3.0
Version:        3.14.0
Release:        %autorelease
Summary:        Rust crate "os_info"
License:        MIT
URL:            https://github.com/stanislav-tkach/os_info
#!RemoteAsset:  sha256:e4022a17595a00d6a369236fdae483f0de7f0a339960a53118b818238e132224
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(android-system-properties-0.1/default) >= 0.1.5
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(nix-0.30/default) >= 0.30.1
Requires:       crate(nix-0.30/feature) >= 0.30.1
Requires:       crate(objc2-0.6/default) >= 0.6.4
Requires:       crate(objc2-foundation-0.3/default) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsenumerator) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-ui-kit-0.3/default) >= 0.3.2
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-libraryloader) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-registry) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-systeminformation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-systemservices) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-threading) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-ui-windowsandmessaging) >= 0.61.2
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "os_info"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

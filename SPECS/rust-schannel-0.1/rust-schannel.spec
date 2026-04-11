# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name schannel
%global full_version 0.1.29
%global pkgname schannel-0.1

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-schannel-0.1
Version:        0.1.29
Release:        %autorelease
Summary:        Rust crate "schannel"
License:        MIT
URL:            https://github.com/steffengy/schannel-rs
#!RemoteAsset:  sha256:91c1b7e4904c873ef0710c1f407dde2e6287de2bebc1bbbf7d430bb7cbffd939
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-security-authentication-identity) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-security-credentials) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-security-cryptography) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-libraryloader) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-memory) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-systeminformation) >= 0.61.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
https) without openssl
Source code for takopackized Rust crate "schannel"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

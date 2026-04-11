# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name curl-sys
%global full_version 0.4.87+curl-8.19.0
%global pkgname curl-sys-0.4

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-curl-sys-0.4
Version:        0.4.87
Release:        %autorelease
Summary:        Rust crate "curl-sys"
License:        MIT
URL:            https://github.com/alexcrichton/curl-rust
#!RemoteAsset:  sha256:61a460380f0ef783703dcbe909107f39c162adeac050d73c850055118b5b6327
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(cc-1.0/default) >= 1.2.60
Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(libz-sys-1.0/libc) >= 1.1.28
Requires:       crate(pkg-config-0.3/default) >= 0.3.32
Requires:       crate(vcpkg-0.2/default) >= 0.2.15
Requires:       crate(windows-sys-0.59/default) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-networking-winsock) >= 0.59.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/force-system-lib-on-osx)
Provides:       crate(%{pkgname}/mesalink)
Provides:       crate(%{pkgname}/ntlm)
Provides:       crate(%{pkgname}/poll-7-68-0)
Provides:       crate(%{pkgname}/protocol-ftp)
Provides:       crate(%{pkgname}/spnego)
Provides:       crate(%{pkgname}/static-curl)
Provides:       crate(%{pkgname}/upkeep-7-62-0)
Provides:       crate(%{pkgname}/windows-static-ssl)

%description
Source code for takopackized Rust crate "curl-sys"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

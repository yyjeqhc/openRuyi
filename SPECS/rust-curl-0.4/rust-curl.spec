# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name curl
%global full_version 0.4.49
%global pkgname curl-0.4

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-curl-0.4
Version:        0.4.49
Release:        %autorelease
Summary:        Rust crate "curl"
License:        MIT
URL:            https://github.com/alexcrichton/curl-rust
#!RemoteAsset:  sha256:79fc3b6dd0b87ba36e565715bf9a2ced221311db47bd18011676f24a6066edbc
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(curl-sys-0.4) >= 0.4.87
Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(schannel-0.1/default) >= 0.1.29
Requires:       crate(socket2-0.6/default) >= 0.6.3
Requires:       crate(windows-sys-0.59/default) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-foundation) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-security-cryptography) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-libraryloader) >= 0.59.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "curl"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

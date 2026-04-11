# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name getrandom
%global full_version 0.2.17
%global pkgname getrandom-0.2

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-getrandom-0.2
Version:        0.2.17
Release:        %autorelease
Summary:        Rust crate "getrandom"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-random/getrandom
#!RemoteAsset:  sha256:ff2abc00be7fca6ebc474524697ae276ad847ad0a6b3faa4bcb027e9a4614ad0
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(libc-0.2) >= 0.2.184
Requires:       crate(wasi-0.11) >= 0.11.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/custom)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/linux-disable-fallback)
Provides:       crate(%{pkgname}/rdrand)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/test-in-browser)

%description
Source code for takopackized Rust crate "getrandom"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

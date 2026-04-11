# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name security-framework
%global full_version 3.7.0
%global pkgname security-framework-3.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-security-framework-3.0
Version:        3.7.0
Release:        %autorelease
Summary:        Rust crate "security-framework"
License:        MIT OR Apache-2.0
URL:            https://lib.rs/crates/security_framework
#!RemoteAsset:  sha256:b7f4bc775c73d9a02cde8bf7b2ec4c9d12743edf609006c7facc23998404cd1d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bitflags-2.0/default) >= 2.11.0
Requires:       crate(core-foundation-0.10/default) >= 0.10.1
Requires:       crate(core-foundation-sys-0.8/default) >= 0.8.7
Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(security-framework-sys-2.0) >= 2.17.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/osx-10-12)
Provides:       crate(%{pkgname}/osx-10-13)
Provides:       crate(%{pkgname}/osx-10-14)
Provides:       crate(%{pkgname}/alpn)
Provides:       crate(%{pkgname}/job-bless)
Provides:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/session-tickets)
Provides:       crate(%{pkgname}/sync-keychain)

%description
Source code for takopackized Rust crate "security-framework"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

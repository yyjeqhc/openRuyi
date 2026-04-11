# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ed25519-compact
%global full_version 2.2.0
%global pkgname ed25519-compact-2.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-ed25519-compact-2.0
Version:        2.2.0
Release:        %autorelease
Summary:        Rust crate "ed25519-compact"
License:        MIT
URL:            https://github.com/jedisct1/rust-ed25519-compact
#!RemoteAsset:  sha256:33ce99a9e19c84beb4cc35ece85374335ccc398240712114c85038319ed709bd
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/blind-keys)
Provides:       crate(%{pkgname}/disable-signatures)
Provides:       crate(%{pkgname}/opt-size)
Provides:       crate(%{pkgname}/self-verify)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/x25519)

%description
Source code for takopackized Rust crate "ed25519-compact"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name openssl
%global full_version 0.10.76
%global pkgname openssl-0.10

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-openssl-0.10
Version:        0.10.76
Release:        %autorelease
Summary:        Rust crate "openssl"
License:        Apache-2.0
URL:            https://github.com/rust-openssl/rust-openssl
#!RemoteAsset:  sha256:951c002c75e16ea2c65b8c7e4d3d51d5530d8dfa7d060b4776828c88cfb18ecf
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bitflags-2.0/default) >= 2.11.0
Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(foreign-types-0.3/default) >= 0.3.2
Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(once-cell-1.0/default) >= 1.21.4
Requires:       crate(openssl-macros-0.1/default) >= 0.1.1
Requires:       crate(openssl-sys-0.9/default) >= 0.9.112
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/v101)
Provides:       crate(%{pkgname}/v102)
Provides:       crate(%{pkgname}/v110)
Provides:       crate(%{pkgname}/v111)

%description
Source code for takopackized Rust crate "openssl"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

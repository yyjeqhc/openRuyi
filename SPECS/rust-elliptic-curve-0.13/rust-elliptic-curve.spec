# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name elliptic-curve
%global full_version 0.13.8
%global pkgname elliptic-curve-0.13

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-elliptic-curve-0.13
Version:        0.13.8
Release:        %autorelease
Summary:        Rust crate "elliptic-curve"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/traits/tree/master/elliptic-curve
#!RemoteAsset:  sha256:b5e6043086bf7973472e0c7dff2142ea0b680d30e18d9cc40f267efbf222bd47
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(base16ct-0.2/default) >= 0.2.0
Requires:       crate(crypto-bigint-0.5/generic-array) >= 0.5.5
Requires:       crate(crypto-bigint-0.5/rand-core) >= 0.5.5
Requires:       crate(crypto-bigint-0.5/zeroize) >= 0.5.5
Requires:       crate(generic-array-0.14/zeroize) >= 0.14.9
Requires:       crate(rand-core-0.6) >= 0.6.4
Requires:       crate(subtle-2.0) >= 2.6.1
Requires:       crate(zeroize-1.0) >= 1.8.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/hazmat)

%description
Source code for takopackized Rust crate "elliptic-curve"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

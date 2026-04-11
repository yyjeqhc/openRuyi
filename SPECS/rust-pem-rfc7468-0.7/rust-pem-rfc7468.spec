# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pem-rfc7468
%global full_version 0.7.0
%global pkgname pem-rfc7468-0.7

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-pem-rfc7468-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "pem-rfc7468"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/pem-rfc7468
#!RemoteAsset:  sha256:88b39c9bfcfc231068454382784bb460aae594343fb030d46e9f50a645418412
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(base64ct-1.0/default) >= 1.8.3
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Provides a no_std-friendly, constant-time implementation suitable for use with cryptographic private keys.
Source code for takopackized Rust crate "pem-rfc7468"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

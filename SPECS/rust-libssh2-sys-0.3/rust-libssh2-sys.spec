# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libssh2-sys
%global full_version 0.3.1
%global pkgname libssh2-sys-0.3

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-libssh2-sys-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "libssh2-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/alexcrichton/ssh2-rs
#!RemoteAsset:  sha256:220e4f05ad4a218192533b300327f5150e809b54c4ec83b5a1d91833601811b9
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(cc-1.0/default) >= 1.2.60
Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(libz-sys-1.0/libc) >= 1.1.28
Requires:       crate(openssl-sys-0.9/default) >= 0.9.112
Requires:       crate(pkg-config-0.3/default) >= 0.3.32
Requires:       crate(vcpkg-0.2/default) >= 0.2.15
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "libssh2-sys"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

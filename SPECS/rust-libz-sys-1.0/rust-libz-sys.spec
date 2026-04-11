# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libz-sys
%global full_version 1.1.28
%global pkgname libz-sys-1.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-libz-sys-1.0
Version:        1.1.28
Release:        %autorelease
Summary:        Rust crate "libz-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/libz-sys
#!RemoteAsset:  sha256:fc3a226e576f50782b3305c5ccf458698f92798987f551c6a02efe8276721e22
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(cc-1.0/default) >= 1.2.60
Requires:       crate(pkg-config-0.3/default) >= 0.3.32
Requires:       crate(vcpkg-0.2/default) >= 0.2.15
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/asm)
Provides:       crate(%{pkgname}/static)
Provides:       crate(%{pkgname}/stock-zlib)

%description
Source code for takopackized Rust crate "libz-sys"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

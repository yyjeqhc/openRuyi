# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wit-parser
%global full_version 0.244.0
%global pkgname wit-parser-0.244

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-wit-parser-0.244
Version:        0.244.0
Release:        %autorelease
Summary:        Rust crate "wit-parser"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/wasm-tools/tree/main/crates/wit-parser
#!RemoteAsset:  sha256:ecc8ac4bc1dc3381b7f59c34f00b67e18f910c2c0f50015669dde7def656a736
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(anyhow-1.0/default) >= 1.0.102
Requires:       crate(id-arena-2.0/default) >= 2.3.0
Requires:       crate(indexmap-2.0/std) >= 2.14.0
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(semver-1.0) >= 1.0.28
Requires:       crate(unicode-xid-0.2/default) >= 0.2.6
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "wit-parser"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

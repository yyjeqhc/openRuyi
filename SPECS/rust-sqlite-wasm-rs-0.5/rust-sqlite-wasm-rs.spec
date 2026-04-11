# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sqlite-wasm-rs
%global full_version 0.5.2
%global pkgname sqlite-wasm-rs-0.5

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-sqlite-wasm-rs-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "sqlite-wasm-rs"
License:        MIT
URL:            https://github.com/Spxg/sqlite-wasm-rs
#!RemoteAsset:  sha256:2f4206ed3a67690b9c29b77d728f6acc3ce78f16bf846d83c94f76400320181b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(cc-1.0/default) >= 1.2.60
Requires:       crate(js-sys-0.3) >= 0.3.95
Requires:       crate(rsqlite-vfs-0.1/default) >= 0.1.0
Requires:       crate(wasm-bindgen-0.2) >= 0.2.118
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/sqlite3mc)

%description
Source code for takopackized Rust crate "sqlite-wasm-rs"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

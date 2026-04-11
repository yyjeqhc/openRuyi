# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wit-component
%global full_version 0.244.0
%global pkgname wit-component-0.244

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-wit-component-0.244
Version:        0.244.0
Release:        %autorelease
Summary:        Rust crate "wit-component"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/wasm-tools/tree/main/crates/wit-component
#!RemoteAsset:  sha256:9d66ea20e9553b30172b5e831994e35fbde2d165325bec84fc43dbf6f4eb9cb2
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(anyhow-1.0/default) >= 1.0.102
Requires:       crate(bitflags-2.0/default) >= 2.11.0
Requires:       crate(indexmap-2.0) >= 2.14.0
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(serde-1.0/alloc) >= 1.0.228
Requires:       crate(serde-derive-1.0/default) >= 1.0.228
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Requires:       crate(wasm-encoder-0.244/std) >= 0.244.0
Requires:       crate(wasm-encoder-0.244/wasmparser) >= 0.244.0
Requires:       crate(wasm-metadata-0.244) >= 0.244.0
Requires:       crate(wasmparser-0.244/component-model) >= 0.244.0
Requires:       crate(wasmparser-0.244/simd) >= 0.244.0
Requires:       crate(wasmparser-0.244/std) >= 0.244.0
Requires:       crate(wit-parser-0.244/decoding) >= 0.244.0
Requires:       crate(wit-parser-0.244/default) >= 0.244.0
Requires:       crate(wit-parser-0.244/serde) >= 0.244.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "wit-component"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

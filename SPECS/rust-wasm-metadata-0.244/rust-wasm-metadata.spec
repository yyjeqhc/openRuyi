# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasm-metadata
%global full_version 0.244.0
%global pkgname wasm-metadata-0.244

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-wasm-metadata-0.244
Version:        0.244.0
Release:        %autorelease
Summary:        Rust crate "wasm-metadata"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/wasm-tools/tree/main/crates/wasm-metadata
#!RemoteAsset:  sha256:bb0e353e6a2fbdc176932bbaab493762eb1255a7900fe0fea1a2f96c296cc909
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(anyhow-1.0/default) >= 1.0.102
Requires:       crate(indexmap-2.0/serde) >= 2.14.0
Requires:       crate(wasm-encoder-0.244/component-model) >= 0.244.0
Requires:       crate(wasm-encoder-0.244/std) >= 0.244.0
Requires:       crate(wasmparser-0.244/component-model) >= 0.244.0
Requires:       crate(wasmparser-0.244/hash-collections) >= 0.244.0
Requires:       crate(wasmparser-0.244/simd) >= 0.244.0
Requires:       crate(wasmparser-0.244/std) >= 0.244.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "wasm-metadata"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

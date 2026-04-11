# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wit-bindgen-rust
%global full_version 0.51.0
%global pkgname wit-bindgen-rust-0.51

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-wit-bindgen-rust-0.51
Version:        0.51.0
Release:        %autorelease
Summary:        Rust crate "wit-bindgen-rust"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/wit-bindgen
#!RemoteAsset:  sha256:b7c566e0f4b284dd6561c786d9cb0142da491f46a9fbed79ea69cdad5db17f21
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(anyhow-1.0/default) >= 1.0.102
Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(indexmap-2.0/default) >= 2.14.0
Requires:       crate(prettyplease-0.2/default) >= 0.2.37
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/printing) >= 2.0.117
Requires:       crate(wasm-metadata-0.244) >= 0.244.0
Requires:       crate(wit-bindgen-core-0.51/default) >= 0.51.0
Requires:       crate(wit-component-0.244/default) >= 0.244.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "wit-bindgen-rust"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

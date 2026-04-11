# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasm-bindgen
%global full_version 0.2.118
%global pkgname wasm-bindgen-0.2

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-wasm-bindgen-0.2
Version:        0.2.118
Release:        %autorelease
Summary:        Rust crate "wasm-bindgen"
License:        MIT OR Apache-2.0
URL:            https://wasm-bindgen.github.io/wasm-bindgen
#!RemoteAsset:  sha256:0bf938a0bacb0469e83c1e148908bd7d5a6010354cf4fb73279b7447422e3a89
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(once-cell-1.0) >= 1.21.4
Requires:       crate(rustversion-1.0/default) >= 1.0.22
Requires:       crate(wasm-bindgen-macro-0.2/default) >= 0.2.118
Requires:       crate(wasm-bindgen-shared-0.2/default) >= 0.2.118
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/enable-interning)
Provides:       crate(%{pkgname}/gg-alloc)
Provides:       crate(%{pkgname}/msrv)
Provides:       crate(%{pkgname}/rustversion)
Provides:       crate(%{pkgname}/spans)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/xxx-debug-only-print-generated-code)

%description
Source code for takopackized Rust crate "wasm-bindgen"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

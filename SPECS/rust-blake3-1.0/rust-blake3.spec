# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name blake3
%global full_version 1.8.4
%global pkgname blake3-1.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-blake3-1.0
Version:        1.8.4
Release:        %autorelease
Summary:        Rust crate "blake3"
License:        CC0-1.0 OR Apache-2.0 OR Apache-2.0 WITH LLVM-exception
URL:            https://github.com/BLAKE3-team/BLAKE3
#!RemoteAsset:  sha256:4d2d5991425dfd0785aed03aedcf0b321d61975c9b5b3689c774a2610ae0b51e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(arrayref-0.3/default) >= 0.3.9
Requires:       crate(arrayvec-0.7) >= 0.7.6
Requires:       crate(cc-1.0/default) >= 1.2.60
Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(constant-time-eq-0.4) >= 0.4.2
Requires:       crate(cpufeatures-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/neon)
Provides:       crate(%{pkgname}/no-avx2)
Provides:       crate(%{pkgname}/no-avx512)
Provides:       crate(%{pkgname}/no-neon)
Provides:       crate(%{pkgname}/no-sse2)
Provides:       crate(%{pkgname}/no-sse41)
Provides:       crate(%{pkgname}/prefer-intrinsics)
Provides:       crate(%{pkgname}/pure)
Provides:       crate(%{pkgname}/wasm32-simd)

%description
Source code for takopackized Rust crate "blake3"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name encoding_rs
%global full_version 0.8.35
%global pkgname encoding-rs-0.8

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-encoding-rs-0.8
Version:        0.8.35
Release:        %autorelease
Summary:        Rust crate "encoding_rs"
License:        (Apache-2.0 OR MIT) AND BSD-3-Clause
URL:            https://docs.rs/encoding_rs/
#!RemoteAsset:  sha256:75030f3c4f45dafd7586dd6780965a8c7e8e285a5ecb86713e63a79c5b2766f3
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/fast-big5-hanzi-encode)
Provides:       crate(%{pkgname}/fast-gb-hanzi-encode)
Provides:       crate(%{pkgname}/fast-hangul-encode)
Provides:       crate(%{pkgname}/fast-hanja-encode)
Provides:       crate(%{pkgname}/fast-kanji-encode)
Provides:       crate(%{pkgname}/less-slow-big5-hanzi-encode)
Provides:       crate(%{pkgname}/less-slow-gb-hanzi-encode)
Provides:       crate(%{pkgname}/less-slow-kanji-encode)

%description
Source code for takopackized Rust crate "encoding_rs"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

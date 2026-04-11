# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name syn
%global full_version 2.0.117
%global pkgname syn-2.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-syn-2.0
Version:        2.0.117
Release:        %autorelease
Summary:        Rust crate "syn"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/syn
#!RemoteAsset:  sha256:e665b8803e7b1d2a727f4023456bbbbe74da67099c585258af0ad9c5013b9b99
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(proc-macro2-1.0) >= 1.0.106
Requires:       crate(unicode-ident-1.0/default) >= 1.0.24
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/clone-impls)
Provides:       crate(%{pkgname}/derive)
Provides:       crate(%{pkgname}/extra-traits)
Provides:       crate(%{pkgname}/fold)
Provides:       crate(%{pkgname}/full)
Provides:       crate(%{pkgname}/parsing)
Provides:       crate(%{pkgname}/test)
Provides:       crate(%{pkgname}/visit)
Provides:       crate(%{pkgname}/visit-mut)

%description
Source code for takopackized Rust crate "syn"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

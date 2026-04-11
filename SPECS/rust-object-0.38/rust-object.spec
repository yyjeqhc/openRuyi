# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name object
%global full_version 0.38.1
%global pkgname object-0.38

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-object-0.38
Version:        0.38.1
Release:        %autorelease
Summary:        Rust crate "object"
License:        Apache-2.0 OR MIT
URL:            https://github.com/gimli-rs/object
#!RemoteAsset:  sha256:271638cd5fa9cca89c4c304675ca658efc4e64a66c716b7cfe1afb4b9611dbbc
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(memchr-2.0) >= 2.8.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/archive)
Provides:       crate(%{pkgname}/cargo-all)
Provides:       crate(%{pkgname}/coff)
Provides:       crate(%{pkgname}/elf)
Provides:       crate(%{pkgname}/macho)
Provides:       crate(%{pkgname}/pe)
Provides:       crate(%{pkgname}/read-core)
Provides:       crate(%{pkgname}/unaligned)
Provides:       crate(%{pkgname}/unstable)
Provides:       crate(%{pkgname}/xcoff)

%description
Source code for takopackized Rust crate "object"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

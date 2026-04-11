# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libsqlite3-sys
%global full_version 0.36.0
%global pkgname libsqlite3-sys-0.36

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-libsqlite3-sys-0.36
Version:        0.36.0
Release:        %autorelease
Summary:        Rust crate "libsqlite3-sys"
License:        MIT
URL:            https://github.com/rusqlite/rusqlite
#!RemoteAsset:  sha256:95b4103cffefa72eb8428cb6b47d6627161e51c2739fc5e3b734584157bc642a
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/bundled-bindings)
Provides:       crate(%{pkgname}/column-metadata)
Provides:       crate(%{pkgname}/in-gecko)
Provides:       crate(%{pkgname}/sqlcipher)
Provides:       crate(%{pkgname}/unlock-notify)
Provides:       crate(%{pkgname}/wasm32-wasi-vfs)
Provides:       crate(%{pkgname}/with-asan)

%description
Source code for takopackized Rust crate "libsqlite3-sys"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

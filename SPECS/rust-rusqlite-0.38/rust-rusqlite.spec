# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rusqlite
%global full_version 0.38.0
%global pkgname rusqlite-0.38

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-rusqlite-0.38
Version:        0.38.0
Release:        %autorelease
Summary:        Rust crate "rusqlite"
License:        MIT
URL:            https://github.com/rusqlite/rusqlite
#!RemoteAsset:  sha256:f1c93dd1c9683b438c392c492109cb702b8090b2bfc8fed6f6e4eb4523f17af3
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bitflags-2.0/default) >= 2.11.0
Requires:       crate(fallible-iterator-0.3/default) >= 0.3.0
Requires:       crate(fallible-streaming-iterator-0.1/default) >= 0.1.9
Requires:       crate(libsqlite3-sys-0.36/default) >= 0.36.0
Requires:       crate(smallvec-1.0/default) >= 1.15.1
Requires:       crate(sqlite-wasm-rs-0.5) >= 0.5.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/array)
Provides:       crate(%{pkgname}/backup)
Provides:       crate(%{pkgname}/blob)
Provides:       crate(%{pkgname}/collation)
Provides:       crate(%{pkgname}/column-decltype)
Provides:       crate(%{pkgname}/extra-check)
Provides:       crate(%{pkgname}/fallible-uint)
Provides:       crate(%{pkgname}/functions)
Provides:       crate(%{pkgname}/hooks)
Provides:       crate(%{pkgname}/i128-blob)
Provides:       crate(%{pkgname}/limits)
Provides:       crate(%{pkgname}/load-extension)
Provides:       crate(%{pkgname}/serialize)
Provides:       crate(%{pkgname}/series)
Provides:       crate(%{pkgname}/trace)
Provides:       crate(%{pkgname}/vtab)
Provides:       crate(%{pkgname}/window)

%description
Source code for takopackized Rust crate "rusqlite"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

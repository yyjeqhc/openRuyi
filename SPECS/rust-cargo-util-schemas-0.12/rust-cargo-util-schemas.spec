# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo-util-schemas
%global full_version 0.12.0
%global pkgname cargo-util-schemas-0.12

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-cargo-util-schemas-0.12
Version:        0.12.0
Release:        %autorelease
Summary:        Rust crate "cargo-util-schemas"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/cargo
#!RemoteAsset:  sha256:74b5c24ba23f6d05b6cb15946d08bb6dd61b96ae920f17b33b17d4e7b1e76555
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(jiff-0.2/serde) >= 0.2.23
Requires:       crate(jiff-0.2/std) >= 0.2.23
Requires:       crate(semver-1.0/default) >= 1.0.28
Requires:       crate(semver-1.0/serde) >= 1.0.28
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Requires:       crate(serde-untagged-0.1/default) >= 0.1.9
Requires:       crate(serde-value-0.7/default) >= 0.7.0
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Requires:       crate(toml-0.9/serde) >= 0.9.12
Requires:       crate(unicode-ident-1.0/default) >= 1.0.24
Requires:       crate(url-2.0/default) >= 2.5.8
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "cargo-util-schemas"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap_builder
%global full_version 4.6.0
%global pkgname clap-builder-4.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-clap-builder-4.0
Version:        4.6.0
Release:        %autorelease
Summary:        Rust crate "clap_builder"
License:        MIT OR Apache-2.0
URL:            https://github.com/clap-rs/clap
#!RemoteAsset:  sha256:714a53001bf66416adb0e2ef5ac857140e7dc3a0c48fb28b2f10762fc4b5069f
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(anstyle-1.0/default) >= 1.0.14
Requires:       crate(clap-lex-1.0/default) >= 1.1.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/cargo)
Provides:       crate(%{pkgname}/deprecated)
Provides:       crate(%{pkgname}/env)
Provides:       crate(%{pkgname}/error-context)
Provides:       crate(%{pkgname}/help)
Provides:       crate(%{pkgname}/string)
Provides:       crate(%{pkgname}/unstable-ext)
Provides:       crate(%{pkgname}/unstable-v5)
Provides:       crate(%{pkgname}/usage)

%description
Source code for takopackized Rust crate "clap_builder"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

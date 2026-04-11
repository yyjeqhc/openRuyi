# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tracing
%global full_version 0.1.44
%global pkgname tracing-0.1

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-tracing-0.1
Version:        0.1.44
Release:        %autorelease
Summary:        Rust crate "tracing"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:63e71662fa4b2a2c3a26f570f037eb95bb1f85397f3cd8076caed2f026a6d100
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(pin-project-lite-0.2/default) >= 0.2.17
Requires:       crate(tracing-core-0.1) >= 0.1.36
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/async-await)
Provides:       crate(%{pkgname}/max-level-debug)
Provides:       crate(%{pkgname}/max-level-error)
Provides:       crate(%{pkgname}/max-level-info)
Provides:       crate(%{pkgname}/max-level-off)
Provides:       crate(%{pkgname}/max-level-trace)
Provides:       crate(%{pkgname}/max-level-warn)
Provides:       crate(%{pkgname}/release-max-level-debug)
Provides:       crate(%{pkgname}/release-max-level-error)
Provides:       crate(%{pkgname}/release-max-level-info)
Provides:       crate(%{pkgname}/release-max-level-off)
Provides:       crate(%{pkgname}/release-max-level-trace)
Provides:       crate(%{pkgname}/release-max-level-warn)

%description
Source code for takopackized Rust crate "tracing"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

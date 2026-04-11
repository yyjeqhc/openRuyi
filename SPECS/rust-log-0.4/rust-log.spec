# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name log
%global full_version 0.4.29
%global pkgname log-0.4

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-log-0.4
Version:        0.4.29
Release:        %autorelease
Summary:        Rust crate "log"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/log
#!RemoteAsset:  sha256:5e5032e24019045c762d3c0f28f5b6b8bbf38563a65908389bf7978758920897
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/kv)
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
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "log"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

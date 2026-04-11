# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tracing-log
%global full_version 0.2.0
%global pkgname tracing-log-0.2

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-tracing-log-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "tracing-log"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:ee855f1f400bd0e5c02d150ae5de3840039a3f54b025156404e34c23c03f47c3
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(once-cell-1.0/default) >= 1.21.4
Requires:       crate(tracing-core-0.1/default) >= 0.1.36
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/log-tracer)

%description
Source code for takopackized Rust crate "tracing-log"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

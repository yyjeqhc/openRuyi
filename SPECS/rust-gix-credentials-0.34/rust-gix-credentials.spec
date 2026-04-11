# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-credentials
%global full_version 0.34.1
%global pkgname gix-credentials-0.34

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-gix-credentials-0.34
Version:        0.34.1
Release:        %autorelease
Summary:        Rust crate "gix-credentials"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:316a12842fb761a7a6e9ae963d7bae9f0f4c433f242282df91192ef084b1891c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(gix-command-0.6/default) >= 0.6.5
Requires:       crate(gix-config-value-0.16/default) >= 0.16.0
Requires:       crate(gix-date-0.12/default) >= 0.12.1
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(gix-prompt-0.12/default) >= 0.12.0
Requires:       crate(gix-sec-0.12/default) >= 0.12.2
Requires:       crate(gix-trace-0.1/default) >= 0.1.18
Requires:       crate(gix-url-0.34/default) >= 0.34.0
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-credentials"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

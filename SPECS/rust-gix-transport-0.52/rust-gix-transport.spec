# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-transport
%global full_version 0.52.1
%global pkgname gix-transport-0.52

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-gix-transport-0.52
Version:        0.52.1
Release:        %autorelease
Summary:        Rust crate "gix-transport"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:a4d4ed02a2ebe771a26111896ecda0b98b58ed35e1d9c0ccf07251c1abb4918d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(bstr-1.0/unicode) >= 1.12.1
Requires:       crate(gix-command-0.6/default) >= 0.6.5
Requires:       crate(gix-features-0.45/default) >= 0.45.2
Requires:       crate(gix-packetline-0.20/default) >= 0.20.0
Requires:       crate(gix-quote-0.6/default) >= 0.6.2
Requires:       crate(gix-sec-0.12/default) >= 0.12.2
Requires:       crate(gix-url-0.34/default) >= 0.34.0
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/http-client-insecure-credentials)

%description
Source code for takopackized Rust crate "gix-transport"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

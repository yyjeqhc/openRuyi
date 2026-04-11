# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-filter
%global full_version 0.24.1
%global pkgname gix-filter-0.24

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-gix-filter-0.24
Version:        0.24.1
Release:        %autorelease
Summary:        Rust crate "gix-filter"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:10c02464962482570c1f94ad451a608c4391514f803e8074662d02c5629a25dc
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(encoding-rs-0.8/default) >= 0.8.35
Requires:       crate(gix-attributes-0.29/default) >= 0.29.0
Requires:       crate(gix-command-0.6/default) >= 0.6.5
Requires:       crate(gix-hash-0.21/default) >= 0.21.2
Requires:       crate(gix-object-0.54/default) >= 0.54.1
Requires:       crate(gix-packetline-0.20/blocking-io) >= 0.20.0
Requires:       crate(gix-packetline-0.20/default) >= 0.20.0
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(gix-quote-0.6/default) >= 0.6.2
Requires:       crate(gix-trace-0.1/default) >= 0.1.18
Requires:       crate(gix-utils-0.3/default) >= 0.3.1
Requires:       crate(smallvec-1.0/default) >= 1.15.1
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-filter"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

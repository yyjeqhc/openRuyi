# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-filter
%global full_version 0.28.0
%global pkgname gix-filter-0.28

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-gix-filter-0.28
Version:        0.28.0
Release:        %autorelease
Summary:        Rust crate "gix-filter"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:d37598282a6566da6fb52667570c7fe0aedcb122ac886724a9e62a2180523e35
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(encoding-rs-0.8/default) >= 0.8.35
Requires:       crate(gix-attributes-0.31/default) >= 0.31.0
Requires:       crate(gix-command-0.8/default) >= 0.8.0
Requires:       crate(gix-hash-0.23/default) >= 0.23.0
Requires:       crate(gix-object-0.58/default) >= 0.58.0
Requires:       crate(gix-packetline-0.21/blocking-io) >= 0.21.2
Requires:       crate(gix-packetline-0.21/default) >= 0.21.2
Requires:       crate(gix-path-0.11/default) >= 0.11.2
Requires:       crate(gix-quote-0.7/default) >= 0.7.0
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

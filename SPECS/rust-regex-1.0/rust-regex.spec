# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name regex
%global full_version 1.12.3
%global pkgname regex-1.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-regex-1.0
Version:        1.12.3
Release:        %autorelease
Summary:        Rust crate "regex"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/regex
#!RemoteAsset:  sha256:e10754a14b9137dd7b1e3e5b0493cc9171fdd105e0ab477f51b72e7f3ac0e276
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(regex-automata-0.4/alloc) >= 0.4.14
Requires:       crate(regex-automata-0.4/meta) >= 0.4.14
Requires:       crate(regex-automata-0.4/nfa-pikevm) >= 0.4.14
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.14
Requires:       crate(regex-syntax-0.8) >= 0.8.10
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/pattern)
Provides:       crate(%{pkgname}/perf-cache)
Provides:       crate(%{pkgname}/unstable)

%description
This implementation uses finite automata and guarantees linear time matching on all inputs.
Source code for takopackized Rust crate "regex"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

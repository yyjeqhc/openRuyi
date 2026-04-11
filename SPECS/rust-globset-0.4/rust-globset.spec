# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name globset
%global full_version 0.4.18
%global pkgname globset-0.4

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-globset-0.4
Version:        0.4.18
Release:        %autorelease
Summary:        Rust crate "globset"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/ripgrep/tree/master/crates/globset
#!RemoteAsset:  sha256:52dfc19153a48bde0cbd630453615c8151bce3a5adfac7a0aebfbf0a1e1f57e3
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(aho-corasick-1.0/default) >= 1.1.4
Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.14
Requires:       crate(regex-automata-0.4/meta) >= 0.4.14
Requires:       crate(regex-automata-0.4/nfa) >= 0.4.14
Requires:       crate(regex-automata-0.4/perf) >= 0.4.14
Requires:       crate(regex-automata-0.4/std) >= 0.4.14
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.14
Requires:       crate(regex-syntax-0.8/std) >= 0.8.10
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/simd-accel)

%description
Glob set matching is the process of matching one or more glob patterns against a single candidate path simultaneously, and returning all of the globs that matched.
Source code for takopackized Rust crate "globset"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

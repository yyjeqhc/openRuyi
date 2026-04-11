# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ignore
%global full_version 0.4.25
%global pkgname ignore-0.4

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-ignore-0.4
Version:        0.4.25
Release:        %autorelease
Summary:        Rust crate "ignore"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/ripgrep/tree/master/crates/ignore
#!RemoteAsset:  sha256:d3d782a365a015e0f5c04902246139249abf769125006fbe7649e2ee88169b4a
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(crossbeam-deque-0.8/default) >= 0.8.6
Requires:       crate(globset-0.4/default) >= 0.4.18
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(memchr-2.0/default) >= 2.8.0
Requires:       crate(regex-automata-0.4/dfa-onepass) >= 0.4.14
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.14
Requires:       crate(regex-automata-0.4/meta) >= 0.4.14
Requires:       crate(regex-automata-0.4/nfa) >= 0.4.14
Requires:       crate(regex-automata-0.4/perf) >= 0.4.14
Requires:       crate(regex-automata-0.4/std) >= 0.4.14
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.14
Requires:       crate(same-file-1.0/default) >= 1.0.6
Requires:       crate(walkdir-2.0/default) >= 2.5.0
Requires:       crate(winapi-util-0.1/default) >= 0.1.11
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/simd-accel)

%description
Source code for takopackized Rust crate "ignore"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

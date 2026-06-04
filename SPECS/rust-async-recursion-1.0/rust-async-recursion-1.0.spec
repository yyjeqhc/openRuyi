# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-recursion
%global full_version 1.1.1
%global pkgname async-recursion-1.0

Name:           rust-async-recursion-1.0
Version:        1.1.1
Release:        %autorelease
Summary:        Rust crate "async-recursion"
License:        MIT OR Apache-2.0
URL:            https://github.com/dcchut/async-recursion
#!RemoteAsset:  sha256:3b43422f69d8ff38f95f1b2bb76517c91589a924d1559a0e935d7c8ce0274c11
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0) >= 1.0.106
Requires:       crate(quote-1.0) >= 1.0.45
Requires:       crate(syn-2.0/clone-impls) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Requires:       crate(syn-2.0/parsing) >= 2.0.117
Requires:       crate(syn-2.0/printing) >= 2.0.117
Requires:       crate(syn-2.0/proc-macro) >= 2.0.117
Requires:       crate(syn-2.0/visit-mut) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "async-recursion"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

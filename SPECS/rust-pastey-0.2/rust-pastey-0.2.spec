# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pastey
%global full_version 0.2.3
%global pkgname pastey-0.2

Name:           rust-pastey-0.2
Version:        0.2.3
Release:        %autorelease
Summary:        Rust crate "pastey"
License:        MIT OR Apache-2.0
URL:            https://github.com/as1100k/pastey
#!RemoteAsset:  sha256:2ee67f1008b1ba2321834326597b8e186293b049a023cdef258527550b9935b4
Source:         https://static.crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Successor of paste.
Source code for takopackized Rust crate "pastey"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

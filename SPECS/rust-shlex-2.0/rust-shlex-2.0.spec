# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name shlex
%global full_version 2.0.1
%global pkgname shlex-2.0

Name:           rust-shlex-2.0
Version:        2.0.1
Release:        %autorelease
Summary:        Rust crate "shlex"
License:        MIT OR Apache-2.0
URL:            https://github.com/comex/rust-shlex
#!RemoteAsset:  sha256:f8fadd59c855ef2080decdef8ff161eb6661b86933c9d82e5ba29dc602a55aba
Source:         https://static.crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "shlex"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

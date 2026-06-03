# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name epoll
%global full_version 4.4.0
%global pkgname epoll-4.0

Name:           rust-epoll-4.0
Version:        4.4.0
Release:        %autorelease
Summary:        Rust crate "epoll"
License:        MPL-2.0
URL:            https://github.com/nathansizemore/epoll
#!RemoteAsset:  sha256:e74d68fe2927dbf47aa976d14d93db9b23dced457c7bb2bdc6925a16d31b736e
Source:         https://static.crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.12.1
Requires:       crate(libc-0.2/default) >= 0.2.186
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "epoll"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

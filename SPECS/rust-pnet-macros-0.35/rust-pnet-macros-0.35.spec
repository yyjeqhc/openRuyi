# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pnet_macros
%global full_version 0.35.0
%global pkgname pnet-macros-0.35

Name:           rust-pnet-macros-0.35
Version:        0.35.0
Release:        %autorelease
Summary:        Rust crate "pnet_macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/libpnet/libpnet
#!RemoteAsset:  sha256:13325ac86ee1a80a480b0bc8e3d30c25d133616112bb16e86f712dcf8a71c863
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(regex-1.0/default) >= 1.12.3
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/travis)

%description
Source code for takopackized Rust crate "pnet_macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

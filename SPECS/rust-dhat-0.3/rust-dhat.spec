# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dhat
%global full_version 0.3.3
%global pkgname dhat-0.3

Name:           rust-dhat-0.3
Version:        0.3.3
Release:        %autorelease
Summary:        Rust crate "dhat"
License:        MIT OR Apache-2.0
URL:            https://github.com/nnethercote/dhat-rs
#!RemoteAsset:  sha256:98cd11d84628e233de0ce467de10b8633f4ddaecafadefc86e13b84b8739b827
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(backtrace-0.3/default) >= 0.3.76
Requires:       crate(lazy-static-1.0/default) >= 1.5.0
Requires:       crate(mintex-0.1/default) >= 0.1.4
Requires:       crate(parking-lot-0.12/default) >= 0.12.5
Requires:       crate(rustc-hash-1.0/default) >= 1.1.0
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(serde-json-1/default) >= 1.0.149
Requires:       crate(thousands-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "dhat"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

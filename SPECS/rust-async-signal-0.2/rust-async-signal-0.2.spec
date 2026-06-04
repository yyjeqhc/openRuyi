# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-signal
%global full_version 0.2.14
%global pkgname async-signal-0.2

Name:           rust-async-signal-0.2
Version:        0.2.14
Release:        %autorelease
Summary:        Rust crate "async-signal"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/async-signal
#!RemoteAsset:  sha256:52b5aaafa020cf5053a01f2a60e8ff5dccf550f0f77ec54a4e47285ac2bab485
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-io-2.0/default) >= 2.6.0
Requires:       crate(async-lock-3.0/default) >= 3.4.2
Requires:       crate(atomic-waker-1.0/default) >= 1.1.2
Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(futures-core-0.3/default) >= 0.3.32
Requires:       crate(futures-io-0.3/default) >= 0.3.32
Requires:       crate(rustix-1.0/process) >= 1.1.4
Requires:       crate(rustix-1.0/std) >= 1.1.4
Requires:       crate(signal-hook-registry-1.0/default) >= 1.4.8
Requires:       crate(slab-0.4/default) >= 0.4.12
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-console) >= 0.61.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "async-signal"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

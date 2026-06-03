# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-process
%global full_version 2.5.0
%global pkgname async-process-2.0

Name:           rust-async-process-2.0
Version:        2.5.0
Release:        %autorelease
Summary:        Rust crate "async-process"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/async-process
#!RemoteAsset:  sha256:fc50921ec0055cdd8a16de48773bfeec5c972598674347252c0399676be7da75
Source:         https://static.crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-channel-2.0/default) >= 2.5.0
Requires:       crate(async-io-2.0/default) >= 2.6.0
Requires:       crate(async-lock-3.0/default) >= 3.4.2
Requires:       crate(async-signal-0.2/default) >= 0.2.14
Requires:       crate(async-task-4.0/default) >= 4.7.1
Requires:       crate(blocking-1.0/default) >= 1.6.2
Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(event-listener-5.0/default) >= 5.4.1
Requires:       crate(futures-lite-2.0/default) >= 2.6.1
Requires:       crate(rustix-1.0/fs) >= 1.1.4
Requires:       crate(rustix-1.0/process) >= 1.1.4
Requires:       crate(rustix-1.0/std) >= 1.1.4
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "async-process"

%package     -n %{name}+tracing
Summary:        Async interface for working with processes - feature "tracing"
Requires:       crate(%{pkgname})
Requires:       crate(tracing-0.1) >= 0.1.40
Provides:       crate(%{pkgname}/tracing)

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust async-process crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

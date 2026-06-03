# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name polling
%global full_version 3.11.0
%global pkgname polling-3.0

Name:           rust-polling-3.0
Version:        3.11.0
Release:        %autorelease
Summary:        Rust crate "polling"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/polling
#!RemoteAsset:  sha256:5d0e4f59085d47d8241c88ead0f274e8a0cb551f3625263c05eb8dd897c34218
Source:         https://static.crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(concurrent-queue-2.0/default) >= 2.5.0
Requires:       crate(hermit-abi-0.5/default) >= 0.5.2
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.17
Requires:       crate(rustix-1.0/event) >= 1.1.4
Requires:       crate(rustix-1.0/fs) >= 1.1.4
Requires:       crate(rustix-1.0/pipe) >= 1.1.4
Requires:       crate(rustix-1.0/process) >= 1.1.4
Requires:       crate(rustix-1.0/std) >= 1.1.4
Requires:       crate(rustix-1.0/time) >= 1.1.4
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/wdk-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/wdk-storage-filesystem) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-networking-winsock) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-security) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-storage-filesystem) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-io) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-libraryloader) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-threading) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-windowsprogramming) >= 0.61.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "polling"

%package     -n %{name}+tracing
Summary:        Portable interface to epoll, kqueue, event ports, and IOCP - feature "tracing"
Requires:       crate(%{pkgname})
Requires:       crate(tracing-0.1) >= 0.1.37
Provides:       crate(%{pkgname}/tracing)

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust polling crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

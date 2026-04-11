# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustix
%global full_version 1.1.4
%global pkgname rustix-1.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-rustix-1.0
Version:        1.1.4
Release:        %autorelease
Summary:        Rust crate "rustix"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/rustix
#!RemoteAsset:  sha256:b6fe4565b9518b83ef4f91bb47ce29620ca828bd32cb7e408f0062e9930ba190
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bitflags-2.0) >= 2.11.0
Requires:       crate(errno-0.3) >= 0.3.14
Requires:       crate(libc-0.2) >= 0.2.184
Requires:       crate(linux-raw-sys-0.12/auxvec) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/elf) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/errno) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/general) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/ioctl) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/no-std) >= 0.12.1
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-networking-winsock) >= 0.61.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/event)
Provides:       crate(%{pkgname}/fs)
Provides:       crate(%{pkgname}/linux-4-11)
Provides:       crate(%{pkgname}/linux-5-1)
Provides:       crate(%{pkgname}/linux-5-11)
Provides:       crate(%{pkgname}/linux-latest)
Provides:       crate(%{pkgname}/mm)
Provides:       crate(%{pkgname}/mount)
Provides:       crate(%{pkgname}/param)
Provides:       crate(%{pkgname}/pipe)
Provides:       crate(%{pkgname}/pty)
Provides:       crate(%{pkgname}/rand)
Provides:       crate(%{pkgname}/shm)
Provides:       crate(%{pkgname}/stdio)
Provides:       crate(%{pkgname}/termios)
Provides:       crate(%{pkgname}/time)
Provides:       crate(%{pkgname}/try-close)
Provides:       crate(%{pkgname}/use-explicitly-provided-auxv)
Provides:       crate(%{pkgname}/use-libc-auxv)

%description
Source code for takopackized Rust crate "rustix"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

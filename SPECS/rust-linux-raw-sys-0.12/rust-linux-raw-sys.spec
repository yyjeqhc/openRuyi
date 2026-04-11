# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name linux-raw-sys
%global full_version 0.12.1
%global pkgname linux-raw-sys-0.12

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-linux-raw-sys-0.12
Version:        0.12.1
Release:        %autorelease
Summary:        Rust crate "linux-raw-sys"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/sunfishcode/linux-raw-sys
#!RemoteAsset:  sha256:32a66949e030da00e8c7d4434b251670a91556f4144941d37452769c25d58a53
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/auxvec)
Provides:       crate(%{pkgname}/bootparam)
Provides:       crate(%{pkgname}/btrfs)
Provides:       crate(%{pkgname}/elf)
Provides:       crate(%{pkgname}/elf-uapi)
Provides:       crate(%{pkgname}/errno)
Provides:       crate(%{pkgname}/general)
Provides:       crate(%{pkgname}/if-arp)
Provides:       crate(%{pkgname}/if-ether)
Provides:       crate(%{pkgname}/if-packet)
Provides:       crate(%{pkgname}/if-tun)
Provides:       crate(%{pkgname}/image)
Provides:       crate(%{pkgname}/io-uring)
Provides:       crate(%{pkgname}/ioctl)
Provides:       crate(%{pkgname}/landlock)
Provides:       crate(%{pkgname}/loop-device)
Provides:       crate(%{pkgname}/mempolicy)
Provides:       crate(%{pkgname}/net)
Provides:       crate(%{pkgname}/netlink)
Provides:       crate(%{pkgname}/no-std)
Provides:       crate(%{pkgname}/prctl)
Provides:       crate(%{pkgname}/ptrace)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/system)
Provides:       crate(%{pkgname}/vm-sockets)
Provides:       crate(%{pkgname}/xdp)

%description
Source code for takopackized Rust crate "linux-raw-sys"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

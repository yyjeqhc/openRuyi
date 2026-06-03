# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name virtio-queue
%global full_version 0.17.0
%global pkgname virtio-queue-0.17

Name:           rust-virtio-queue-0.17
Version:        0.17.0
Release:        %autorelease
Summary:        Rust crate "virtio-queue"
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/rust-vmm/vm-virtio
#!RemoteAsset:  sha256:e358084f32ed165fddb41d98ff1b7ff3c08b9611d8d6114a1b422e2e85688baf
Source:         https://static.crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.186
Requires:       crate(log-0.4/default) >= 0.4.31
Requires:       crate(virtio-bindings-0.2/default) >= 0.2.7
Requires:       crate(vm-memory-0.17/backend-mmap) >= 0.17.1
Requires:       crate(vm-memory-0.17/default) >= 0.17.1
Requires:       crate(vmm-sys-util-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/test-utils)

%description
Source code for takopackized Rust crate "virtio-queue"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

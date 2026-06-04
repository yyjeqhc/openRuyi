# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gdbstub_arch
%global full_version 0.3.3
%global pkgname gdbstub-arch-0.3

Name:           rust-gdbstub-arch-0.3
Version:        0.3.3
Release:        %autorelease
Summary:        Rust crate "gdbstub_arch"
License:        MIT OR Apache-2.0
URL:            https://github.com/daniel5151/gdbstub
#!RemoteAsset:  sha256:6c02bfe7bd65f42bcda751456869dfa1eb2bd1c36e309b9ec27f4888d41cf258
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gdbstub-0.7) >= 0.7.10
Requires:       crate(num-traits-0.2) >= 0.2.19
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gdbstub_arch"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

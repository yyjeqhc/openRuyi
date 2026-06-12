# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name signal-hook-registry
%global full_version 1.4.8
%global pkgname signal-hook-registry-1

Name:           rust-signal-hook-registry-1
Version:        1.4.8
Release:        %autorelease
Summary:        Rust crate "signal-hook-registry"
License:        MIT OR Apache-2.0
URL:            https://github.com/vorner/signal-hook
#!RemoteAsset:  sha256:c4db69cba1110affc0e9f7bcd48bbf87b3f4fc7c61fc9155afd4c469eb3d6c1b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

# manual change to 0.3. see the cargo.toml,maybe we can change cargo.toml to regenerate it.
# for now, we just change the spec directly.
Requires:       crate(errno-0.3/default) >= 0.3.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "signal-hook-registry"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

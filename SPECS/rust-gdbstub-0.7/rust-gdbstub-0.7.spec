# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gdbstub
%global full_version 0.7.10
%global pkgname gdbstub-0.7

Name:           rust-gdbstub-0.7
Version:        0.7.10
Release:        %autorelease
Summary:        Rust crate "gdbstub"
License:        MIT OR Apache-2.0
URL:            https://github.com/daniel5151/gdbstub
#!RemoteAsset:  sha256:5bafc7e33650ab9f05dcc16325f05d56b8d10393114e31a19a353b86fa60cfe7
Source:         https://static.crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.12.1
Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(log-0.4/default) >= 0.4.31
Requires:       crate(managed-0.8) >= 0.8.0
Requires:       crate(num-traits-0.2) >= 0.2.19
Requires:       crate(pastey-0.2/default) >= 0.2.3
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/dead-code-marker)
Provides:       crate(%{pkgname}/core-error)
Provides:       crate(%{pkgname}/paranoid-unsafe)

%description
Source code for takopackized Rust crate "gdbstub"

%package     -n %{name}+alloc
Summary:        The GDB Remote Serial Protocol in Rust - feature "alloc" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(managed-0.8/alloc) >= 0.8.0
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/trace-pkt)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust gdbstub crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "std", and "trace-pkt" features.

%package     -n %{name}+default
Summary:        The GDB Remote Serial Protocol in Rust - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/trace-pkt)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust gdbstub crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

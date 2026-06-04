# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name iced-x86
%global full_version 1.21.0
%global pkgname iced-x86-1.0

Name:           rust-iced-x86-1.0
Version:        1.21.0
Release:        %autorelease
Summary:        Rust crate "iced-x86"
License:        MIT
URL:            https://github.com/icedland/iced
#!RemoteAsset:  sha256:7c447cff8c7f384a7d4f741cfcff32f75f3ad02b406432e8d6c878d56b1edf6b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/internal-flip)
Provides:       crate(%{pkgname}/block-encoder)
Provides:       crate(%{pkgname}/code-asm)
Provides:       crate(%{pkgname}/db)
Provides:       crate(%{pkgname}/decoder)
Provides:       crate(%{pkgname}/encoder)
Provides:       crate(%{pkgname}/exhaustive-enums)
Provides:       crate(%{pkgname}/fast-fmt)
Provides:       crate(%{pkgname}/gas)
Provides:       crate(%{pkgname}/instr-info)
Provides:       crate(%{pkgname}/intel)
Provides:       crate(%{pkgname}/masm)
Provides:       crate(%{pkgname}/mvex)
Provides:       crate(%{pkgname}/nasm)
Provides:       crate(%{pkgname}/no-d3now)
Provides:       crate(%{pkgname}/no-evex)
Provides:       crate(%{pkgname}/no-vex)
Provides:       crate(%{pkgname}/no-xop)
Provides:       crate(%{pkgname}/op-code-info)

%description
Source code for takopackized Rust crate "iced-x86"

%package     -n %{name}+default
Summary:        Blazing fast and correct x86/x64 disassembler, assembler and instruction decoder written in Rust - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/block-encoder)
Requires:       crate(%{pkgname}/decoder)
Requires:       crate(%{pkgname}/encoder)
Requires:       crate(%{pkgname}/fast-fmt)
Requires:       crate(%{pkgname}/gas)
Requires:       crate(%{pkgname}/instr-info)
Requires:       crate(%{pkgname}/intel)
Requires:       crate(%{pkgname}/masm)
Requires:       crate(%{pkgname}/nasm)
Requires:       crate(%{pkgname}/op-code-info)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust iced-x86 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lazy-static
Summary:        Blazing fast and correct x86/x64 disassembler, assembler and instruction decoder written in Rust - feature "lazy_static" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(lazy-static-1.0/default) >= 1.5.0
Provides:       crate(%{pkgname}/lazy-static)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+lazy-static
This metapackage enables feature "lazy_static" for the Rust iced-x86 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "std" feature.

%package     -n %{name}+no-std
Summary:        Blazing fast and correct x86/x64 disassembler, assembler and instruction decoder written in Rust - feature "no_std"
Requires:       crate(%{pkgname})
Requires:       crate(lazy-static-1.0/spin-no-std) >= 1.5.0
Provides:       crate(%{pkgname}/no-std)

%description -n %{name}+no-std
This metapackage enables feature "no_std" for the Rust iced-x86 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Blazing fast and correct x86/x64 disassembler, assembler and instruction decoder written in Rust - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.16
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust iced-x86 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zstd
%global full_version 0.13.3
%global pkgname zstd-0.13

Name:           rust-zstd-0.13
Version:        0.13.3
Release:        %autorelease
Summary:        Rust crate "zstd"
License:        MIT
URL:            https://github.com/gyscos/zstd-rs
#!RemoteAsset:  sha256:e91ee311a569c327171651566e07972200e76fcfe2242a4fa446149a3881c08a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(zstd-safe-7.0/std) >= 7.2.4
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/doc-cfg)
Provides:       crate(%{pkgname}/wasm)

%description
Source code for takopackized Rust crate "zstd"

%package     -n %{name}+arrays
Summary:        Binding for the zstd compression library - feature "arrays"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-7.0/arrays) >= 7.2.4
Requires:       crate(zstd-safe-7.0/std) >= 7.2.4
Provides:       crate(%{pkgname}/arrays)

%description -n %{name}+arrays
This metapackage enables feature "arrays" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bindgen
Summary:        Binding for the zstd compression library - feature "bindgen"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-7.0/bindgen) >= 7.2.4
Requires:       crate(zstd-safe-7.0/std) >= 7.2.4
Provides:       crate(%{pkgname}/bindgen)

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+debug
Summary:        Binding for the zstd compression library - feature "debug"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-7.0/debug) >= 7.2.4
Requires:       crate(zstd-safe-7.0/std) >= 7.2.4
Provides:       crate(%{pkgname}/debug)

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Binding for the zstd compression library - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arrays)
Requires:       crate(%{pkgname}/legacy)
Requires:       crate(%{pkgname}/zdict-builder)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+experimental
Summary:        Binding for the zstd compression library - feature "experimental"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-7.0/experimental) >= 7.2.4
Requires:       crate(zstd-safe-7.0/std) >= 7.2.4
Provides:       crate(%{pkgname}/experimental)

%description -n %{name}+experimental
This metapackage enables feature "experimental" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fat-lto
Summary:        Binding for the zstd compression library - feature "fat-lto"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-7.0/fat-lto) >= 7.2.4
Requires:       crate(zstd-safe-7.0/std) >= 7.2.4
Provides:       crate(%{pkgname}/fat-lto)

%description -n %{name}+fat-lto
This metapackage enables feature "fat-lto" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+legacy
Summary:        Binding for the zstd compression library - feature "legacy"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-7.0/legacy) >= 7.2.4
Requires:       crate(zstd-safe-7.0/std) >= 7.2.4
Provides:       crate(%{pkgname}/legacy)

%description -n %{name}+legacy
This metapackage enables feature "legacy" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+no-asm
Summary:        Binding for the zstd compression library - feature "no_asm"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-7.0/no-asm) >= 7.2.4
Requires:       crate(zstd-safe-7.0/std) >= 7.2.4
Provides:       crate(%{pkgname}/no-asm)

%description -n %{name}+no-asm
This metapackage enables feature "no_asm" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkg-config
Summary:        Binding for the zstd compression library - feature "pkg-config"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-7.0/pkg-config) >= 7.2.4
Requires:       crate(zstd-safe-7.0/std) >= 7.2.4
Provides:       crate(%{pkgname}/pkg-config)

%description -n %{name}+pkg-config
This metapackage enables feature "pkg-config" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+thin
Summary:        Binding for the zstd compression library - feature "thin"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-7.0/std) >= 7.2.4
Requires:       crate(zstd-safe-7.0/thin) >= 7.2.4
Provides:       crate(%{pkgname}/thin)

%description -n %{name}+thin
This metapackage enables feature "thin" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+thin-lto
Summary:        Binding for the zstd compression library - feature "thin-lto"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-7.0/std) >= 7.2.4
Requires:       crate(zstd-safe-7.0/thin-lto) >= 7.2.4
Provides:       crate(%{pkgname}/thin-lto)

%description -n %{name}+thin-lto
This metapackage enables feature "thin-lto" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zdict-builder
Summary:        Binding for the zstd compression library - feature "zdict_builder"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-7.0/std) >= 7.2.4
Requires:       crate(zstd-safe-7.0/zdict-builder) >= 7.2.4
Provides:       crate(%{pkgname}/zdict-builder)

%description -n %{name}+zdict-builder
This metapackage enables feature "zdict_builder" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zstdmt
Summary:        Binding for the zstd compression library - feature "zstdmt"
Requires:       crate(%{pkgname})
Requires:       crate(zstd-safe-7.0/std) >= 7.2.4
Requires:       crate(zstd-safe-7.0/zstdmt) >= 7.2.4
Provides:       crate(%{pkgname}/zstdmt)

%description -n %{name}+zstdmt
This metapackage enables feature "zstdmt" for the Rust zstd crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

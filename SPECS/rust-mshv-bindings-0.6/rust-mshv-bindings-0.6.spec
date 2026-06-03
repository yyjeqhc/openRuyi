# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mshv-bindings
%global full_version 0.6.9
%global pkgname mshv-bindings-0.6

Name:           rust-mshv-bindings-0.6
Version:        0.6.9
Release:        %autorelease
Summary:        Rust crate "mshv-bindings"
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/rust-vmm/mshv
#!RemoteAsset:  sha256:83303108160c2b7a7bdd25000ee679384e19471386d23e501ed832574c9229ef
Source:         https://static.crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.186
Requires:       crate(num-enum-0.7) >= 0.7.6
Requires:       crate(vmm-sys-util-0.15/default) >= 0.15.0
Requires:       crate(zerocopy-0.8/default) >= 0.8.50
Requires:       crate(zerocopy-0.8/derive) >= 0.8.50
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/fam-wrappers)

%description
Source code for takopackized Rust crate "mshv-bindings"

%package     -n %{name}+serde
Summary:        Rust FFI bindings to MSHV headers generated using Rust bindgen - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.228
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust mshv-bindings crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-derive
Summary:        Rust FFI bindings to MSHV headers generated using Rust bindgen - feature "serde_derive"
Requires:       crate(%{pkgname})
Requires:       crate(serde-derive-1.0/default) >= 1.0.228
Provides:       crate(%{pkgname}/serde-derive)

%description -n %{name}+serde-derive
This metapackage enables feature "serde_derive" for the Rust mshv-bindings crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-serde
Summary:        Rust FFI bindings to MSHV headers generated using Rust bindgen - feature "with-serde"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(%{pkgname}/serde-derive)
Provides:       crate(%{pkgname}/with-serde)

%description -n %{name}+with-serde
This metapackage enables feature "with-serde" for the Rust mshv-bindings crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

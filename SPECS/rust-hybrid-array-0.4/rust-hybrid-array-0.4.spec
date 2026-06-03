# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hybrid-array
%global full_version 0.4.12
%global pkgname hybrid-array-0.4

Name:           rust-hybrid-array-0.4
Version:        0.4.12
Release:        %autorelease
Summary:        Rust crate "hybrid-array"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/hybrid-array
#!RemoteAsset:  sha256:9155a582abd142abc056962c29e3ce5ff2ad5469f4246b537ed42c5deba857da
Source:         https://static.crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(typenum-1.0/const-generics) >= 1.20.1
Requires:       crate(typenum-1.0/default) >= 1.20.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/extra-sizes)

%description
Source code for takopackized Rust crate "hybrid-array"

%package     -n %{name}+arbitrary
Summary:        Hybrid typenum-based and const generic array types designed to provide the flexibility of typenum-based expressions while also allowing interoperability and a transition path to const generics - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(arbitrary-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust hybrid-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytemuck
Summary:        Hybrid typenum-based and const generic array types designed to provide the flexibility of typenum-based expressions while also allowing interoperability and a transition path to const generics - feature "bytemuck"
Requires:       crate(%{pkgname})
Requires:       crate(bytemuck-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/bytemuck)

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust hybrid-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ctutils
Summary:        Hybrid typenum-based and const generic array types designed to provide the flexibility of typenum-based expressions while also allowing interoperability and a transition path to const generics - feature "ctutils"
Requires:       crate(%{pkgname})
Requires:       crate(ctutils-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/ctutils)

%description -n %{name}+ctutils
This metapackage enables feature "ctutils" for the Rust hybrid-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Hybrid typenum-based and const generic array types designed to provide the flexibility of typenum-based expressions while also allowing interoperability and a transition path to const generics - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust hybrid-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+subtle
Summary:        Hybrid typenum-based and const generic array types designed to provide the flexibility of typenum-based expressions while also allowing interoperability and a transition path to const generics - feature "subtle"
Requires:       crate(%{pkgname})
Requires:       crate(subtle-2.0/const-generics) >= 2.0.0
Provides:       crate(%{pkgname}/subtle)

%description -n %{name}+subtle
This metapackage enables feature "subtle" for the Rust hybrid-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zerocopy
Summary:        Hybrid typenum-based and const generic array types designed to provide the flexibility of typenum-based expressions while also allowing interoperability and a transition path to const generics - feature "zerocopy"
Requires:       crate(%{pkgname})
Requires:       crate(zerocopy-0.8/default) >= 0.8.0
Requires:       crate(zerocopy-0.8/derive) >= 0.8.0
Provides:       crate(%{pkgname}/zerocopy)

%description -n %{name}+zerocopy
This metapackage enables feature "zerocopy" for the Rust hybrid-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Hybrid typenum-based and const generic array types designed to provide the flexibility of typenum-based expressions while also allowing interoperability and a transition path to const generics - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(zeroize-1.0) >= 1.8
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust hybrid-array crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

%global crate_name typenum
%global full_version 1.20.0
%global pkgname typenum-1

Name:           rust-typenum-1
Version:        1.20.0
Release:        %autorelease
Summary:        Rust crate "typenum"
License:        MIT OR Apache-2.0
URL:            https://github.com/paholg/typenum
#!RemoteAsset:  sha256:40ce102ab67701b8526c123c1bab5cbe42d7040ccfd0f64af1a385808d2f43de
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/const-generics) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/i128) = %{version}
Provides:       crate(%{pkgname}/strict) = %{version}

%description
It currently supports bits, unsigned integers, and signed     integers. It also provides a type-level array of type-level numbers, but its     implementation is incomplete.
Source code for takopackized Rust crate "typenum"

%package     -n %{name}+scale-info
Summary:        Type-level numbers evaluated at     compile time - feature "scale_info"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(scale-info-1) >= 1.0.0
Requires:       crate(scale-info-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/scale-info) = %{version}

%description -n %{name}+scale-info
It currently supports bits, unsigned integers, and signed     integers. It also provides a type-level array of type-level numbers, but its     implementation is incomplete.
This metapackage enables feature "scale_info" for the Rust typenum crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

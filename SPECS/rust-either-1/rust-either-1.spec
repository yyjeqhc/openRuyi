%global crate_name either
%global full_version 1.15.0
%global pkgname either-1

Name:           rust-either-1
Version:        1.15.0
Release:        %autorelease
Summary:        Rust crate "either"
License:        MIT OR Apache-2.0
URL:            https://github.com/rayon-rs/either
#!RemoteAsset:  sha256:48c757948c5ede0e46177b7add2e67155f70e33c07fea8284df6576da70b3719
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/use-std) = %{version}

%description
Source code for takopackized Rust crate "either"

%package     -n %{name}+serde
Summary:        Enum `Either` with variants `Left` and `Right` is a general purpose sum type with two cases - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.95
Requires:       crate(serde-1/derive) >= 1.0.95
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust either crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

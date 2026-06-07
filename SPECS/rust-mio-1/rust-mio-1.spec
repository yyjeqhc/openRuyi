%global crate_name mio
%global full_version 1.2.0
%global pkgname mio-1

Name:           rust-mio-1
Version:        1.2.0
Release:        %autorelease
Summary:        Rust crate "mio"
License:        MIT
URL:            https://github.com/tokio-rs/mio
#!RemoteAsset:  sha256:50b7e5b27aa02a74bac8c3f23f448f8d87ff11f92d3aac1a6ed369ee08cc56c1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.183
Requires:       crate(wasi-0.11/default) >= 0.11.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/net) = %{version}
Provides:       crate(%{pkgname}/os-ext) = %{version}
Provides:       crate(%{pkgname}/os-poll) = %{version}

%description
Source code for takopackized Rust crate "mio"

%package     -n %{name}+log
Summary:        Lightweight non-blocking I/O - feature "log" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.8
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust mio crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

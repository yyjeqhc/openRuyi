%global crate_name polling
%global full_version 3.11.0
%global pkgname polling-3

Name:           rust-polling-3
Version:        3.11.0
Release:        %autorelease
Summary:        Rust crate "polling"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/polling
#!RemoteAsset:  sha256:5d0e4f59085d47d8241c88ead0f274e8a0cb551f3625263c05eb8dd897c34218
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(hermit-abi-0.5/default) >= 0.5.0
Requires:       crate(rustix-1.0/event) >= 1.0.5
Requires:       crate(rustix-1.0/fs) >= 1.0.5
Requires:       crate(rustix-1.0/pipe) >= 1.0.5
Requires:       crate(rustix-1.0/process) >= 1.0.5
Requires:       crate(rustix-1.0/std) >= 1.0.5
Requires:       crate(rustix-1.0/time) >= 1.0.5
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "polling"

%package     -n %{name}+tracing
Summary:        Portable interface to epoll, kqueue, event ports, and IOCP - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1) >= 0.1.37
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust polling crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

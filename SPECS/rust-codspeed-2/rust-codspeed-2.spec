%global crate_name codspeed
%global full_version 2.10.1
%global pkgname codspeed-2

Name:           rust-codspeed-2
Version:        2.10.1
Release:        %autorelease
Summary:        Rust crate "codspeed"
License:        MIT OR Apache-2.0
URL:            https://codspeed.io
#!RemoteAsset:  sha256:93f4cce9c27c49c4f101fffeebb1826f41a9df2e7498b7cd4d95c0658b796c6c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(colored-2/default) >= 2.0.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(serde-1/default) >= 1.0.217
Requires:       crate(serde-1/derive) >= 1.0.217
Requires:       crate(serde-json-1/default) >= 1.0.138
Requires:       crate(uuid-1/default) >= 1.12.1
Requires:       crate(uuid-1/v4) >= 1.12.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "codspeed"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

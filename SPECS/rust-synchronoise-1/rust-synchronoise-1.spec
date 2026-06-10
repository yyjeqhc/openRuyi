%global crate_name synchronoise
%global full_version 1.0.1
%global pkgname synchronoise-1

Name:           rust-synchronoise-1
Version:        1.0.1
Release:        %autorelease
Summary:        Rust crate "synchronoise"
License:        MIT OR Apache-2.0
URL:            https://github.com/QuietMisdreavus/synchronoise
#!RemoteAsset:  sha256:3dbc01390fc626ce8d1cffe3376ded2b72a11bb70e1c75f404a210e4daa4def2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crossbeam-queue-0.3/default) >= 0.3.5
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "synchronoise"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

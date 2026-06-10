%global crate_name fs2
%global full_version 0.4.3
%global pkgname fs2-0.4

Name:           rust-fs2-0.4
Version:        0.4.3
Release:        %autorelease
Summary:        Rust crate "fs2"
License:        MIT OR Apache-2.0
URL:            https://github.com/danburkert/fs2-rs
#!RemoteAsset:  sha256:9564fc758e15025b46aa6643b1b77d047d1a56a1aea6e01002ac0c7026876213
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.30
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "fs2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

%global crate_name clearscreen
%global full_version 4.0.6
%global pkgname clearscreen-4

Name:           rust-clearscreen-4
Version:        4.0.6
Release:        %autorelease
Summary:        Rust crate "clearscreen"
License:        Apache-2.0 OR MIT
URL:            https://github.com/watchexec/clearscreen
#!RemoteAsset:  sha256:d669bb552908e336ad5681789752033b45566b7e591aeaac7a614e58e5d6d8f2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(nix-0.31/fs) >= 0.31.1
Requires:       crate(nix-0.31/term) >= 0.31.1
Requires:       crate(terminfo-0.9/default) >= 0.9.0
Requires:       crate(thiserror-2.0/default) >= 2.0.11
Requires:       crate(which-8.0/default) >= 8.0.0
Requires:       crate(windows-sys-0.59/win32-foundation) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-networkmanagement-netmanagement) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-console) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-systeminformation) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-systemservices) >= 0.59.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/windows-console) = %{version}

%description
Source code for takopackized Rust crate "clearscreen"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

%global crate_name uds_windows
%global full_version 1.2.1
%global pkgname uds-windows-1.0

Name:           rust-uds-windows-1.0
Version:        1.2.1
Release:        %autorelease
Summary:        Rust crate "uds_windows"
License:        MIT
URL:            https://github.com/haraldh/rust_uds_windows
#!RemoteAsset:  sha256:f2f6fb2847f6742cd76af783a2a2c49e9375d0a111c7bef6f71cd9e738c72d6e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memoffset-0.9/default) >= 0.9.1
Requires:       crate(tempfile-3.0/default) >= 3.27.0
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-networking-winsock) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-io) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-threading) >= 0.61.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "uds_windows"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

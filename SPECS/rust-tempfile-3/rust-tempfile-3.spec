%global crate_name tempfile
%global full_version 3.27.0
%global pkgname tempfile-3

Name:           rust-tempfile-3
Version:        3.27.0
Release:        %autorelease
Summary:        Rust crate "tempfile"
License:        MIT OR Apache-2.0
URL:            https://stebalien.com/projects/tempfile-rs/
#!RemoteAsset:  sha256:32497e9a4c7b38532efcdebeef879707aa9f794296a4f0244f6f69e9bc8574bd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fastrand-2/default) >= 2.1.1
Requires:       crate(once-cell-1.0/std) >= 1.19.0
Requires:       crate(rustix-1.0/default) >= 1.1.4
Requires:       crate(rustix-1.0/fs) >= 1.1.4
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/getrandom) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for takopackized Rust crate "tempfile"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

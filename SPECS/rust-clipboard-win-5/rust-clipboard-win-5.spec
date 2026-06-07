%global crate_name clipboard-win
%global full_version 5.4.1
%global pkgname clipboard-win-5

Name:           rust-clipboard-win-5
Version:        5.4.1
Release:        %autorelease
Summary:        Rust crate "clipboard-win"
License:        BSL-1.0
URL:            https://github.com/DoumanAsh/clipboard-win
#!RemoteAsset:  sha256:bde03770d3df201d4fb868f2c9c59e66a3e4e2bd06692a0fe701e7103c7e84d4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/monitor) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/windows-win) = %{version}

%description
Source code for takopackized Rust crate "clipboard-win"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

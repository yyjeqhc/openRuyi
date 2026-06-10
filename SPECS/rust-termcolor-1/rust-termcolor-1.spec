%global crate_name termcolor
%global full_version 1.4.1
%global pkgname termcolor-1

Name:           rust-termcolor-1
Version:        1.4.1
Release:        %autorelease
Summary:        Rust crate "termcolor"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/termcolor
#!RemoteAsset:  sha256:06794f8f6c5c898b3275aebefa6b8a1cb24cd2c6c79397ab15774837a0bc5755
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "termcolor"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

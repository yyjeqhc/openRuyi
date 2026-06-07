%global crate_name same-file
%global full_version 1.0.6
%global pkgname same-file-1

Name:           rust-same-file-1
Version:        1.0.6
Release:        %autorelease
Summary:        Rust crate "same-file"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/same-file
#!RemoteAsset:  sha256:93fc1dc3aaa9bfed95e02e6eadabb4baf7e3078b0bd1b4d7b6b0b68378900502
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "same-file"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

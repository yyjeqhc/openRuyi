%global crate_name imgref
%global full_version 1.12.1
%global pkgname imgref-1

Name:           rust-imgref-1
Version:        1.12.1
Release:        %autorelease
Summary:        Rust crate "imgref"
License:        CC0-1.0 OR Apache-2.0
URL:            https://lib.rs/crates/imgref
#!RemoteAsset:  sha256:40fac9d56ed6437b198fddba683305e8e2d651aa42647f00f5ae542e7f5c94a2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/deprecated) = %{version}

%description
Source code for takopackized Rust crate "imgref"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

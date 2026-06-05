%global crate_name managed
%global full_version 0.8.0
%global pkgname managed-0.8

Name:           rust-managed-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "managed"
License:        0BSD
URL:            https://github.com/m-labs/rust-managed
#!RemoteAsset:  sha256:0ca88d725a0a943b096803bd34e73a4437208b6077654cc4ecb2947a5f91618d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/map)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "managed"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

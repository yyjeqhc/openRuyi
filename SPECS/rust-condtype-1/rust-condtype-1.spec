%global crate_name condtype
%global full_version 1.3.0
%global pkgname condtype-1

Name:           rust-condtype-1
Version:        1.3.0
Release:        %autorelease
Summary:        Rust crate "condtype"
License:        MIT OR Apache-2.0
URL:            https://github.com/nvzqz/condtype
#!RemoteAsset:  sha256:baf0a07a401f374238ab8e2f11a104d2851bf9ce711ec69804834de8af45c7af
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "condtype"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

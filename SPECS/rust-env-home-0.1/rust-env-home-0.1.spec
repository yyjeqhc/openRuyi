%global crate_name env_home
%global full_version 0.1.0
%global pkgname env-home-0.1

Name:           rust-env-home-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "env_home"
License:        MIT OR Apache-2.0
URL:            https://github.com/notpeter/env-home
#!RemoteAsset:  sha256:c7f84e12ccf0a7ddc17a6c41c93326024c42920d7ee630d04950e6926645c0fe
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "env_home"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

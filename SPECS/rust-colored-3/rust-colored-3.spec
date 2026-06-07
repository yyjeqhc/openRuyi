%global crate_name colored
%global full_version 3.1.1
%global pkgname colored-3

Name:           rust-colored-3
Version:        3.1.1
Release:        %autorelease
Summary:        Rust crate "colored"
License:        MPL-2.0
URL:            https://github.com/mackwic/colored
#!RemoteAsset:  sha256:faf9468729b8cbcea668e36183cb69d317348c2e08e994829fb56ebfdfbaac34
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/no-color) = %{version}

%description
Source code for takopackized Rust crate "colored"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

%global crate_name pest_meta
%global full_version 2.8.6
%global pkgname pest-meta-2

Name:           rust-pest-meta-2
Version:        2.8.6
Release:        %autorelease
Summary:        Rust crate "pest_meta"
License:        MIT OR Apache-2.0
URL:            https://pest.rs/
#!RemoteAsset:  sha256:89815c69d36021a140146f26659a81d6c2afa33d216d736dd4be5381a7362220
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pest-2.0/default) >= 2.8.6
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/grammar-extras) = %{version}
Provides:       crate(%{pkgname}/not-bootstrap-in-src) = %{version}

%description
Source code for takopackized Rust crate "pest_meta"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

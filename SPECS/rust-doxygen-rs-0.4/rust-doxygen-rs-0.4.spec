%global crate_name doxygen-rs
%global full_version 0.4.2
%global pkgname doxygen-rs-0.4

Name:           rust-doxygen-rs-0.4
Version:        0.4.2
Release:        %autorelease
Summary:        Rust crate "doxygen-rs"
License:        BSD-3-Clause
URL:            https://github.com/Techie-Pi/doxygen-rs/
#!RemoteAsset:  sha256:415b6ec780d34dcf624666747194393603d0373b7141eef01d12ee58881507d9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(phf-0.11/default) >= 0.11.0
Requires:       crate(phf-0.11/macros) >= 0.11.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "doxygen-rs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

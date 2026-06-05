%global crate_name serde_with_macros
%global full_version 3.18.0
%global pkgname serde-with-macros-3.0

Name:           rust-serde-with-macros-3.0
Version:        3.18.0
Release:        %autorelease
Summary:        Rust crate "serde_with_macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/jonasbb/serde_with/
#!RemoteAsset:  sha256:d3db8978e608f1fe7357e211969fd9abdcae80bac1ba7a3369bb7eb6b404eb65
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(darling-0.23/default) >= 0.23.0
Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/extra-traits) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Requires:       crate(syn-2.0/parsing) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/schemars-0-8)
Provides:       crate(%{pkgname}/schemars-0-9)
Provides:       crate(%{pkgname}/schemars-1)

%description
Source code for takopackized Rust crate "serde_with_macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

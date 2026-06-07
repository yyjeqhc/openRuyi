%global crate_name remain
%global full_version 0.2.15
%global pkgname remain-0.2

Name:           rust-remain-0.2
Version:        0.2.15
Release:        %autorelease
Summary:        Rust crate "remain"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/remain
#!RemoteAsset:  sha256:d7ef12e84481ab4006cb942f8682bba28ece7270743e649442027c5db87df126
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(syn-2/default) >= 2.0.117
Requires:       crate(syn-2/full) >= 2.0.117
Requires:       crate(syn-2/visit-mut) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "remain"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

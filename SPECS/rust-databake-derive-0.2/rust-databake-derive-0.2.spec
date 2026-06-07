%global crate_name databake-derive
%global full_version 0.2.1
%global pkgname databake-derive-0.2

Name:           rust-databake-derive-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "databake-derive"
License:        Unicode-3.0
URL:            https://github.com/unicode-org/icu4x
#!RemoteAsset:  sha256:72b537745234cbf0e296a3bd836d70a614dff4cb522b14e2680ef006bb1ed5ff
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.61
Requires:       crate(quote-1/default) >= 1.0.44
Requires:       crate(syn-2/default) >= 2.0.21
Requires:       crate(synstructure-0.13/default) >= 0.13.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "databake-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

%global crate_name retry-policies
%global full_version 0.5.1
%global pkgname retry-policies-0.5

Name:           rust-retry-policies-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "retry-policies"
License:        MIT OR Apache-2.0
URL:            https://github.com/TrueLayer/retry-policies
#!RemoteAsset:  sha256:46a4bd6027df676bcb752d3724db0ea3c0c5fc1dd0376fec51ac7dcaf9cc69be
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rand-0.9/default) >= 0.9.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "retry-policies"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

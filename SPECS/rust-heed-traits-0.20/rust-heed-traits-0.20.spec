%global crate_name heed-traits
%global full_version 0.20.0
%global pkgname heed-traits-0.20

Name:           rust-heed-traits-0.20
Version:        0.20.0
Release:        %autorelease
Summary:        Rust crate "heed-traits"
License:        MIT
URL:            https://github.com/Kerollmops/heed
#!RemoteAsset:  sha256:eb3130048d404c57ce5a1ac61a903696e8fcde7e8c2991e9fcfc1f27c3ef74ff
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "heed-traits"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

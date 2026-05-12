%global crate_name unicode-ident
%global full_version 1.0.12
%global pkgname unicode-ident-1.0

Name:           rust-unicode-ident-1.0
Version:        1.0.12
Release:        %autorelease
Summary:        Rust crate "unicode-ident"
License:        (MIT OR Apache-2.0) AND Unicode-DFS-2016
URL:            https://github.com/dtolnay/unicode-ident
#!RemoteAsset:  sha256:3354b9ac3fae1ff6755cb6db53683adb661634f67557942dea4facebec0fee4b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "unicode-ident"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

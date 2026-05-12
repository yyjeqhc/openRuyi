%global crate_name proc-macro2
%global full_version 1.0.81
%global pkgname proc-macro2-1.0

Name:           rust-proc-macro2-1.0
Version:        1.0.81
Release:        %autorelease
Summary:        Rust crate "proc-macro2"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/proc-macro2
#!RemoteAsset:  sha256:3d1597b0c024618f09a9c3b8655b7e430397a36d23fdafec26d6965e9eec3eba
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-ident-1.0/default) >= 1.0.12
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/proc-macro)
Provides:       crate(%{pkgname}/span-locations)

%description
Source code for takopackized Rust crate "proc-macro2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

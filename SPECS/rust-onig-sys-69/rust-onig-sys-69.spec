%global crate_name onig_sys
%global full_version 69.9.3
%global pkgname onig-sys-69

Name:           rust-onig-sys-69
Version:        69.9.3
Release:        %autorelease
Summary:        Rust crate "onig_sys"
License:        MIT
URL:            https://github.com/rust-onig/rust-onig
#!RemoteAsset:  sha256:1e68317604e77e53b85896388e1a803c1d21b74c899ec9e5e1112db90735edd7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/bindgen) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/generate) = %{version}
Provides:       crate(%{pkgname}/posix-api) = %{version}
Provides:       crate(%{pkgname}/print-debug) = %{version}

%description
This crate exposes a set of unsafe functions which can then be used by other crates to create safe wrappers around Oniguruma.
You probably don't want to link to this crate directly; instead check out the `onig` crate.
Source code for takopackized Rust crate "onig_sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

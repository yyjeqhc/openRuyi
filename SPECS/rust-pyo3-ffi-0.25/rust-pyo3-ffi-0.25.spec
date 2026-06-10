%global crate_name pyo3-ffi
%global full_version 0.25.1
%global pkgname pyo3-ffi-0.25

Name:           rust-pyo3-ffi-0.25
Version:        0.25.1
Release:        %autorelease
Summary:        Rust crate "pyo3-ffi"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:7114fe5457c61b276ab77c5055f206295b812608083644a5c5b2640c3102565c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.62
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/abi3) = %{version}
Provides:       crate(%{pkgname}/abi3-py310) = %{version}
Provides:       crate(%{pkgname}/abi3-py311) = %{version}
Provides:       crate(%{pkgname}/abi3-py312) = %{version}
Provides:       crate(%{pkgname}/abi3-py313) = %{version}
Provides:       crate(%{pkgname}/abi3-py314) = %{version}
Provides:       crate(%{pkgname}/abi3-py37) = %{version}
Provides:       crate(%{pkgname}/abi3-py38) = %{version}
Provides:       crate(%{pkgname}/abi3-py39) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/extension-module) = %{version}
Provides:       crate(%{pkgname}/generate-import-lib) = %{version}

%description
Source code for takopackized Rust crate "pyo3-ffi"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

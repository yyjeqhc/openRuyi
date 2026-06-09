%global crate_name zstd-sys
%global full_version 2.0.16+zstd.1.5.7
%global pkgname zstd-sys-2

Name:           rust-zstd-sys-2
Version:        2.0.16
Release:        %autorelease
Summary:        Rust crate "zstd-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/gyscos/zstd-rs
#!RemoteAsset:  sha256:91e19ebc2adc8f83e43039e79776e3fda8ca919132d68a1fed6a5faca2683748
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{full_version}
Provides:       crate(%{pkgname}/bindgen) = %{full_version}
Provides:       crate(%{pkgname}/debug) = %{full_version}
Provides:       crate(%{pkgname}/experimental) = %{full_version}
Provides:       crate(%{pkgname}/fat-lto) = %{full_version}
Provides:       crate(%{pkgname}/legacy) = %{full_version}
Provides:       crate(%{pkgname}/no-asm) = %{full_version}
Provides:       crate(%{pkgname}/no-wasm-shim) = %{full_version}
Provides:       crate(%{pkgname}/non-cargo) = %{full_version}
Provides:       crate(%{pkgname}/pkg-config) = %{full_version}
Provides:       crate(%{pkgname}/seekable) = %{full_version}
Provides:       crate(%{pkgname}/std) = %{full_version}
Provides:       crate(%{pkgname}/thin) = %{full_version}
Provides:       crate(%{pkgname}/thin-lto) = %{full_version}
Provides:       crate(%{pkgname}/zdict-builder) = %{full_version}
Provides:       crate(%{pkgname}/zstdmt) = %{full_version}

%description
Source code for takopackized Rust crate "zstd-sys"

%package     -n %{name}+default
Summary:        Low-level bindings for the zstd compression library - feature "default"
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(%{pkgname}/bindgen) = %{full_version}
Requires:       crate(%{pkgname}/legacy) = %{full_version}
Requires:       crate(%{pkgname}/zdict-builder) = %{full_version}
Provides:       crate(%{pkgname}/default) = %{full_version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust zstd-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

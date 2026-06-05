%global crate_name toml_writer
%global full_version 1.0.7+spec-1.1.0
%global pkgname toml-writer-1

Name:           rust-toml-writer-1
Version:        1.0.7
Release:        %autorelease
Summary:        Rust crate "toml_writer"
License:        MIT OR Apache-2.0
URL:            https://github.com/toml-rs/toml
#!RemoteAsset:  sha256:f17aaa1c6e3dc22b1da4b6bba97d066e354c7945cac2f7852d4e4e7ca7a6b56d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "toml_writer"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

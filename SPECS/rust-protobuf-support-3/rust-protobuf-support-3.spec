%global crate_name protobuf-support
%global full_version 3.7.2
%global pkgname protobuf-support-3

Name:           rust-protobuf-support-3
Version:        3.7.2
Release:        %autorelease
Summary:        Rust crate "protobuf-support"
License:        MIT
URL:            https://github.com/stepancheg/rust-protobuf/
#!RemoteAsset:  sha256:3e36c2f31e0a47f9280fb347ef5e461ffcd2c52dd520d8e216b52f93b0b0d7d6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(thiserror-1/default) >= 1.0.30
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
None of code in this crate is public API.
Source code for takopackized Rust crate "protobuf-support"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

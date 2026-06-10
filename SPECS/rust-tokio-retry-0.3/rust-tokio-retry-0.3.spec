%global crate_name tokio-retry
%global full_version 0.3.0
%global pkgname tokio-retry-0.3

Name:           rust-tokio-retry-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "tokio-retry"
License:        MIT
URL:            https://github.com/srijs/rust-tokio-retry
#!RemoteAsset:  sha256:7f57eb36ecbe0fc510036adff84824dd3c24bb781e21bfa67b69d556aa85214f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pin-project-1/default) >= 1.0.5
Requires:       crate(rand-0.8/default) >= 0.8.3
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tokio-retry"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

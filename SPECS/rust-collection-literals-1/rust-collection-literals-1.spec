%global crate_name collection_literals
%global full_version 1.0.2
%global pkgname collection-literals-1

Name:           rust-collection-literals-1
Version:        1.0.2
Release:        %autorelease
Summary:        Rust crate "collection_literals"
License:        MIT
URL:            https://github.com/staedoix/collection_literals
#!RemoteAsset:  sha256:26b3f65b8fb8e88ba339f7d23a390fe1b0896217da05e2a66c584c9b29a91df8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "collection_literals"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

%global crate_name derive-where
%global full_version 1.6.0
%global pkgname derive-where-1

Name:           rust-derive-where-1
Version:        1.6.0
Release:        %autorelease
Summary:        Rust crate "derive-where"
License:        MIT OR Apache-2.0
URL:            https://github.com/ModProg/derive-where
#!RemoteAsset:  sha256:ef941ded77d15ca19b40374869ac6000af1c9f2a4c0f3d4c70926287e6364a8f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/proc-macro) >= 1.0.0
Requires:       crate(quote-1.0) >= 1.0.0
Requires:       crate(syn-2.0/clone-impls) >= 2.0.0
Requires:       crate(syn-2.0/derive) >= 2.0.0
Requires:       crate(syn-2.0/extra-traits) >= 2.0.0
Requires:       crate(syn-2.0/full) >= 2.0.0
Requires:       crate(syn-2.0/parsing) >= 2.0.0
Requires:       crate(syn-2.0/printing) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/safe) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/zeroize) = %{version}
Provides:       crate(%{pkgname}/zeroize-on-drop) = %{version}

%description
Source code for takopackized Rust crate "derive-where"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

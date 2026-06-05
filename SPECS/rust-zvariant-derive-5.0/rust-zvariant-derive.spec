%global crate_name zvariant_derive
%global full_version 5.10.1
%global pkgname zvariant-derive-5.0

Name:           rust-zvariant-derive-5.0
Version:        5.10.1
Release:        %autorelease
Summary:        Rust crate "zvariant_derive"
License:        MIT
URL:            https://github.com/z-galaxy/zbus/
#!RemoteAsset:  sha256:5b949b639ab1b4bed763aa7481ba0e368af68d8b55532f8ed4bec86a59f2ca98
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro-crate-3.0/default) >= 3.5.0
Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/extra-traits) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Requires:       crate(zvariant-utils-3.0/default) >= 3.3.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "zvariant_derive"

%package     -n %{name}+gvariant
Summary:        D-Bus & GVariant encoding & decoding - feature "gvariant"
Requires:       crate(%{pkgname})
Requires:       crate(zvariant-utils-3.0/gvariant) >= 3.3.1
Provides:       crate(%{pkgname}/gvariant)

%description -n %{name}+gvariant
This metapackage enables feature "gvariant" for the Rust zvariant_derive crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

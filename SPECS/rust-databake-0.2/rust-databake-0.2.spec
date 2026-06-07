%global crate_name databake
%global full_version 0.2.1
%global pkgname databake-0.2

Name:           rust-databake-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "databake"
License:        Unicode-3.0
URL:            https://github.com/unicode-org/icu4x
#!RemoteAsset:  sha256:74d4b1db5ca40636726f1f73daff0d626accbd49bcd8136fcade87d7cf1e6bbb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.61
Requires:       crate(quote-1/default) >= 1.0.44
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "databake"

%package     -n %{name}+derive
Summary:        Trait that lets structs represent themselves as (const) Rust expressions - feature "derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(databake-derive-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust databake crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

%global crate_name zbus_macros
%global full_version 5.15.0
%global pkgname zbus-macros-5.0

Name:           rust-zbus-macros-5.0
Version:        5.15.0
Release:        %autorelease
Summary:        Rust crate "zbus_macros"
License:        MIT
URL:            https://github.com/z-galaxy/zbus/
#!RemoteAsset:  sha256:51fa5406ad9175a8c825a931f8cf347116b531b3634fcb0b627c290f1f2516ff
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro-crate-3/default) >= 3.5.0
Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(syn-2/default) >= 2.0.117
Requires:       crate(syn-2/extra-traits) >= 2.0.117
Requires:       crate(syn-2/fold) >= 2.0.117
Requires:       crate(syn-2/full) >= 2.0.117
Requires:       crate(zbus-names-4.0/default) >= 4.3.2
Requires:       crate(zvariant-5.0/default) >= 5.10.1
Requires:       crate(zvariant-utils-3.0/default) >= 3.3.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/blocking-api)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "zbus_macros"

%package     -n %{name}+gvariant
Summary:        Proc-macros for zbus - feature "gvariant"
Requires:       crate(%{pkgname})
Requires:       crate(zvariant-5.0/gvariant) >= 5.10.1
Requires:       crate(zvariant-utils-3.0/gvariant) >= 3.3.1
Provides:       crate(%{pkgname}/gvariant)

%description -n %{name}+gvariant
This metapackage enables feature "gvariant" for the Rust zbus_macros crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

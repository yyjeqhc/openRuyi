%global crate_name jiff-static
%global full_version 0.2.24
%global pkgname jiff-static-0.2

Name:           rust-jiff-static-0.2
Version:        0.2.24
Release:        %autorelease
Summary:        Rust crate "jiff-static"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/jiff/tree/master/crates/jiff-static
#!RemoteAsset:  sha256:e000de030ff8022ea1da3f466fbb0f3a809f5e51ed31f6dd931c35181ad8e6d7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/perf-inline)
Provides:       crate(%{pkgname}/tz-fat)

%description
Source code for takopackized Rust crate "jiff-static"

%package     -n %{name}+tzdb
Summary:        Create static TimeZone values for Jiff (useful in core-only environments) - feature "tzdb"
Requires:       crate(%{pkgname})
Requires:       crate(jiff-tzdb-0.1/default) >= 0.1.6
Provides:       crate(%{pkgname}/tzdb)

%description -n %{name}+tzdb
This metapackage enables feature "tzdb" for the Rust jiff-static crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

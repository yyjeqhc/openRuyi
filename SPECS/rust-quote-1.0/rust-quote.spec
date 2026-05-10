%global crate_name quote
%global full_version 1.0.36
%global pkgname quote-1.0

Name:           rust-quote-1.0
Version:        1.0.36
Release:        %autorelease
Summary:        Rust crate "quote"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/quote
#!RemoteAsset:  sha256:0fa76aaf39101c457836aec0ce2316dbdc3ab723cdda1c6bd4e6ad4208acaca7
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0) >= 1.0.81
Provides:       crate(%{crate_name}) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "quote"

%package     -n %{name}+proc-macro
Summary:        Quasi-quoting macro quote!(...) - feature "proc-macro" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(proc-macro2-1.0/proc-macro) >= 1.0.81
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/proc-macro)

%description -n %{name}+proc-macro
This metapackage enables feature "proc-macro" for the Rust quote crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%{?autochangelog}

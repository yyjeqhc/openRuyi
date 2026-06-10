%global crate_name typewit
%global full_version 1.14.2
%global pkgname typewit-1

Name:           rust-typewit-1
Version:        1.14.2
Release:        %autorelease
Summary:        Rust crate "typewit"
License:        Zlib
URL:            https://github.com/rodrimati1992/typewit/
#!RemoteAsset:  sha256:f8c1ae7cc0fdb8b842d65d127cb981574b0d2b249b74d1c7a2986863dc134f71
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/adt-const-marker) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/const-marker) = %{version}
Provides:       crate(%{pkgname}/docsrs) = %{version}
Provides:       crate(%{pkgname}/generic-const-exprs) = %{version}
Provides:       crate(%{pkgname}/mut-refs) = %{version}
Provides:       crate(%{pkgname}/nightly-mut-refs) = %{version}
Provides:       crate(%{pkgname}/rust-1-61) = %{version}
Provides:       crate(%{pkgname}/rust-1-65) = %{version}
Provides:       crate(%{pkgname}/rust-1-83) = %{version}
Provides:       crate(%{pkgname}/rust-stable) = %{version}
Provides:       crate(%{pkgname}/test-doc-lints) = %{version}

%description
Source code for takopackized Rust crate "typewit"

%package     -n %{name}+trybuild
Summary:        Type-witness-based abstractions, mostly for emulating polymorphism in const fns - feature "trybuild" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(trybuild-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/trybuild) = %{version}
Provides:       crate(%{pkgname}/ui-tests) = %{version}

%description -n %{name}+trybuild
This metapackage enables feature "trybuild" for the Rust typewit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "__ui_tests" feature.

%package     -n %{name}+typewit-proc-macros
Summary:        Type-witness-based abstractions, mostly for emulating polymorphism in const fns - feature "typewit_proc_macros" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(typewit-proc-macros-1/default) >= 1.8.1
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/proc-macros) = %{version}
Provides:       crate(%{pkgname}/typewit-proc-macros) = %{version}

%description -n %{name}+typewit-proc-macros
This metapackage enables feature "typewit_proc_macros" for the Rust typewit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "proc_macros" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

%global crate_name ulid
%global full_version 1.2.1
%global pkgname ulid-1

Name:           rust-ulid-1
Version:        1.2.1
Release:        %autorelease
Summary:        Rust crate "ulid"
License:        MIT
URL:            https://github.com/dylanhart/ulid-rs
#!RemoteAsset:  sha256:470dbf6591da1b39d43c14523b2b469c86879a53e8b758c8e090a470fe7b1fbe
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(web-time-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "ulid"

%package     -n %{name}+postgres
Summary:        Universally Unique Lexicographically Sortable Identifier implementation - feature "postgres"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-1/default) >= 1.4.0
Requires:       crate(postgres-types-0.2/default) >= 0.2.6
Provides:       crate(%{pkgname}/postgres) = %{version}

%description -n %{name}+postgres
This metapackage enables feature "postgres" for the Rust ulid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Universally Unique Lexicographically Sortable Identifier implementation - feature "rand" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rand) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust ulid crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "std" features.

%package     -n %{name}+rkyv
Summary:        Universally Unique Lexicographically Sortable Identifier implementation - feature "rkyv"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rkyv-0.8/default) >= 0.8.10
Provides:       crate(%{pkgname}/rkyv) = %{version}

%description -n %{name}+rkyv
This metapackage enables feature "rkyv" for the Rust ulid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Universally Unique Lexicographically Sortable Identifier implementation - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ulid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        Universally Unique Lexicographically Sortable Identifier implementation - feature "uuid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uuid-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/uuid) = %{version}

%description -n %{name}+uuid
This metapackage enables feature "uuid" for the Rust ulid crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

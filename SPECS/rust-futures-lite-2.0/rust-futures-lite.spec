%global crate_name futures-lite
%global full_version 2.6.1
%global pkgname futures-lite-2.0

Name:           rust-futures-lite-2.0
Version:        2.6.1
Release:        %autorelease
Summary:        Rust crate "futures-lite"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/futures-lite
#!RemoteAsset:  sha256:f78e10609fe0e0b3f4157ffab1876319b5b0db102a2c60dc4626306dc46b44ad
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-core-0.3) >= 0.3.32
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.17
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)

%description
Source code for takopackized Rust crate "futures-lite"

%package     -n %{name}+default
Summary:        Futures, streams, and async I/O combinators - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/race)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust futures-lite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fastrand
Summary:        Futures, streams, and async I/O combinators - feature "fastrand" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(fastrand-2.0) >= 2.4.1
Provides:       crate(%{pkgname}/fastrand)
Provides:       crate(%{pkgname}/race)

%description -n %{name}+fastrand
This metapackage enables feature "fastrand" for the Rust futures-lite crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "race" feature.

%package     -n %{name}+futures-io
Summary:        Futures, streams, and async I/O combinators - feature "futures-io"
Requires:       crate(%{pkgname})
Requires:       crate(futures-io-0.3/default) >= 0.3.32
Provides:       crate(%{pkgname}/futures-io)

%description -n %{name}+futures-io
This metapackage enables feature "futures-io" for the Rust futures-lite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+memchr
Summary:        Futures, streams, and async I/O combinators - feature "memchr"
Requires:       crate(%{pkgname})
Requires:       crate(memchr-2.0/default) >= 2.3.3
Provides:       crate(%{pkgname}/memchr)

%description -n %{name}+memchr
This metapackage enables feature "memchr" for the Rust futures-lite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parking
Summary:        Futures, streams, and async I/O combinators - feature "parking"
Requires:       crate(%{pkgname})
Requires:       crate(parking-2.0/default) >= 2.2.1
Provides:       crate(%{pkgname}/parking)

%description -n %{name}+parking
This metapackage enables feature "parking" for the Rust futures-lite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Futures, streams, and async I/O combinators - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/futures-io)
Requires:       crate(%{pkgname}/parking)
Requires:       crate(fastrand-2.0/std) >= 2.4.1
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust futures-lite crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

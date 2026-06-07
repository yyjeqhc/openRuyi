%global crate_name io-uring
%global full_version 0.7.12
%global pkgname io-uring-0.7

Name:           rust-io-uring-0.7
Version:        0.7.12
Release:        %autorelease
Summary:        Rust crate "io-uring"
License:        MIT OR Apache-2.0
URL:            https://github.com/tokio-rs/io-uring
#!RemoteAsset:  sha256:4d09b98f7eace8982db770e4408e7470b028ce513ac28fecdc6bf4c30fe92b62
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.11.1
Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(libc-0.2) >= 0.2.186
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/io-safety)

%description
Source code for takopackized Rust crate "io-uring"

%package     -n %{name}+bindgen
Summary:        Low-level `io_uring` userspace interface for Rust - feature "bindgen" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(bindgen-0.69/default) >= 0.69.0
Provides:       crate(%{pkgname}/bindgen)
Provides:       crate(%{pkgname}/overwrite)

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust io-uring crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "overwrite" feature.

%package     -n %{name}+sc
Summary:        Low-level `io_uring` userspace interface for Rust - feature "sc" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(sc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/direct-syscall)
Provides:       crate(%{pkgname}/sc)

%description -n %{name}+sc
This metapackage enables feature "sc" for the Rust io-uring crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "direct-syscall" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

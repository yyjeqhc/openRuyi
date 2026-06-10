%global crate_name prometheus
%global full_version 0.14.0
%global pkgname prometheus-0.14

Name:           rust-prometheus-0.14
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "prometheus"
License:        Apache-2.0
URL:            https://github.com/tikv/rust-prometheus
#!RemoteAsset:  sha256:3ca5326d8d0b950a9acd87e6a3f94745394f62e4dae1b1ee22b2bc0c394af43a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(fnv-1/default) >= 1.0.0
Requires:       crate(lazy-static-1/default) >= 1.4.0
Requires:       crate(memchr-2/default) >= 2.3.0
Requires:       crate(parking-lot-0.12/default) >= 0.12.0
Requires:       crate(thiserror-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/gen) = %{version}
Provides:       crate(%{pkgname}/protobuf-codegen) = %{version}

%description
Source code for takopackized Rust crate "prometheus"

%package     -n %{name}+libc
Summary:        Prometheus instrumentation library for Rust applications - feature "libc" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/libc) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust prometheus crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "nightly" feature.

%package     -n %{name}+process
Summary:        Prometheus instrumentation library for Rust applications - feature "process"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/procfs) = %{version}
Provides:       crate(%{pkgname}/process) = %{version}

%description -n %{name}+process
This metapackage enables feature "process" for the Rust prometheus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+procfs
Summary:        Prometheus instrumentation library for Rust applications - feature "procfs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(procfs-0.17) >= 0.17.0
Provides:       crate(%{pkgname}/procfs) = %{version}

%description -n %{name}+procfs
This metapackage enables feature "procfs" for the Rust prometheus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+protobuf
Summary:        Prometheus instrumentation library for Rust applications - feature "protobuf" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(protobuf-3/default) >= 3.7.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/protobuf) = %{version}

%description -n %{name}+protobuf
This metapackage enables feature "protobuf" for the Rust prometheus crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+push
Summary:        Prometheus instrumentation library for Rust applications - feature "push"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/protobuf) = %{version}
Requires:       crate(%{pkgname}/reqwest) = %{version}
Provides:       crate(%{pkgname}/push) = %{version}

%description -n %{name}+push
This metapackage enables feature "push" for the Rust prometheus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+reqwest
Summary:        Prometheus instrumentation library for Rust applications - feature "reqwest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.12/blocking) >= 0.12.0
Requires:       crate(reqwest-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/reqwest) = %{version}

%description -n %{name}+reqwest
This metapackage enables feature "reqwest" for the Rust prometheus crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

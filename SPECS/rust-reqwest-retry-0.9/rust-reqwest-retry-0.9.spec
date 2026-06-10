%global crate_name reqwest-retry
%global full_version 0.9.1
%global pkgname reqwest-retry-0.9

Name:           rust-reqwest-retry-0.9
Version:        0.9.1
Release:        %autorelease
Summary:        Rust crate "reqwest-retry"
License:        MIT OR Apache-2.0
URL:            https://github.com/TrueLayer/reqwest-middleware
#!RemoteAsset:  sha256:fe2412db2af7d2268e7a5406be0431f37d9eb67ff390f35b395716f5f06c2eaa
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.0
Requires:       crate(async-trait-0.1/default) >= 0.1.51
Requires:       crate(futures-0.3/default) >= 0.3.0
Requires:       crate(getrandom-0.2/default) >= 0.2.0
Requires:       crate(getrandom-0.2/js) >= 0.2.0
Requires:       crate(http-1/default) >= 1.0.0
Requires:       crate(hyper-1/default) >= 1.0.0
Requires:       crate(reqwest-0.13) >= 0.13.1
Requires:       crate(reqwest-middleware-0.5/default) >= 0.5.0
Requires:       crate(retry-policies-0.5/default) >= 0.5.0
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(tokio-1/time) >= 1.6.0
Requires:       crate(wasmtimer-0.4/default) >= 0.4.3
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "reqwest-retry"

%package     -n %{name}+tracing
Summary:        Retry middleware for reqwest - feature "tracing" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1/default) >= 0.1.26
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust reqwest-retry crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

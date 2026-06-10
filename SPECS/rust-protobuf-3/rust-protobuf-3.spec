%global crate_name protobuf
%global full_version 3.7.2
%global pkgname protobuf-3

Name:           rust-protobuf-3
Version:        3.7.2
Release:        %autorelease
Summary:        Rust crate "protobuf"
License:        MIT
URL:            https://github.com/stepancheg/rust-protobuf/
#!RemoteAsset:  sha256:d65a1d4ddae7d8b5de68153b48f6aa3bba8cb002b243dbdbc55a5afbc98f99f4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(once-cell-1/default) >= 1.9.0
Requires:       crate(protobuf-support-3/default) >= 3.7.2
Requires:       crate(thiserror-1/default) >= 1.0.30
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "protobuf"

%package     -n %{name}+bytes
Summary:        Google protocol buffers - feature "bytes" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/bytes) = %{version}
Provides:       crate(%{pkgname}/with-bytes) = %{version}

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust protobuf crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-bytes" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

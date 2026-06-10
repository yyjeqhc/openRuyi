%global crate_name lmdb-master-sys
%global full_version 0.2.5
%global pkgname lmdb-master-sys-0.2

Name:           rust-lmdb-master-sys-0.2
Version:        0.2.5
Release:        %autorelease
Summary:        Rust crate "lmdb-master-sys"
License:        Apache-2.0
URL:            https://github.com/meilisearch/heed/tree/main/lmdb-master-sys
#!RemoteAsset:  sha256:864808e0b19fb6dd3b70ba94ee671b82fce17554cf80aeb0a155c65bb08027df
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.170
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/asan) = %{version}
Provides:       crate(%{pkgname}/bindgen) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/fuzzer) = %{version}
Provides:       crate(%{pkgname}/fuzzer-no-link) = %{version}
Provides:       crate(%{pkgname}/longer-keys) = %{version}
Provides:       crate(%{pkgname}/mdb-idl-logn-10) = %{version}
Provides:       crate(%{pkgname}/mdb-idl-logn-11) = %{version}
Provides:       crate(%{pkgname}/mdb-idl-logn-12) = %{version}
Provides:       crate(%{pkgname}/mdb-idl-logn-13) = %{version}
Provides:       crate(%{pkgname}/mdb-idl-logn-14) = %{version}
Provides:       crate(%{pkgname}/mdb-idl-logn-15) = %{version}
Provides:       crate(%{pkgname}/mdb-idl-logn-16) = %{version}
Provides:       crate(%{pkgname}/mdb-idl-logn-8) = %{version}
Provides:       crate(%{pkgname}/mdb-idl-logn-9) = %{version}
Provides:       crate(%{pkgname}/posix-sem) = %{version}
Provides:       crate(%{pkgname}/use-valgrind) = %{version}

%description
Source code for takopackized Rust crate "lmdb-master-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

%global crate_name igvm
%global full_version 0.4.0
%global pkgname igvm-0.4

Name:           rust-igvm-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "igvm"
License:        MIT
URL:            https://github.com/microsoft/igvm
#!RemoteAsset:  sha256:67578b05ebcdfa1aa0fe13f77a13bdd7d87036128898a327f1bf8e7356cf09cd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitfield-struct-0.10/default) >= 0.10.1
Requires:       crate(crc32fast-1) >= 1.5.0
Requires:       crate(hex-0.4/alloc) >= 0.4.3
Requires:       crate(igvm-defs-0.4/default) >= 0.4.0
Requires:       crate(igvm-defs-0.4/unstable) >= 0.4.0
Requires:       crate(open-enum-0.5/default) >= 0.5.2
Requires:       crate(range-map-vec-0.2/default) >= 0.2.0
Requires:       crate(static-assertions-1.0/default) >= 1.1.0
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Requires:       crate(tracing-0.1/default) >= 0.1.44
Requires:       crate(zerocopy-0.8/alloc) >= 0.8.48
Requires:       crate(zerocopy-0.8/default) >= 0.8.48
Requires:       crate(zerocopy-0.8/derive) >= 0.8.48
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/igvm-c)

%description
Source code for takopackized Rust crate "igvm"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

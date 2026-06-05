%global crate_name async-executor
%global full_version 1.14.0
%global pkgname async-executor-1.0

Name:           rust-async-executor-1.0
Version:        1.14.0
Release:        %autorelease
Summary:        Rust crate "async-executor"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/async-executor
#!RemoteAsset:  sha256:c96bf972d85afc50bf5ab8fe2d54d1586b4e0b46c97c50a0c9e71e2f7bcd812a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-task-4.0/default) >= 4.7.1
Requires:       crate(concurrent-queue-2.0/default) >= 2.5.0
Requires:       crate(fastrand-2.0/default) >= 2.4.1
Requires:       crate(futures-lite-2.0) >= 2.6.1
Requires:       crate(futures-lite-2.0/std) >= 2.6.1
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.17
Requires:       crate(slab-0.4/default) >= 0.4.12
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/static)

%description
Source code for takopackized Rust crate "async-executor"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

%global crate_name vhost
%global full_version 0.16.0
%global pkgname vhost-0.16

Name:           rust-vhost-0.16
Version:        0.16.0
Release:        %autorelease
Summary:        Rust crate "vhost"
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/rust-vmm/vhost
#!RemoteAsset:  sha256:ee90657203a8644e9a0860a0db6a7887d8ef0c7bc09fc22dfa4ae75df65bac86
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.11.1
Requires:       crate(libc-0.2/default) >= 0.2.186
Requires:       crate(uuid-1.0/default) >= 1.23.1
Requires:       crate(uuid-1.0/fast-rng) >= 1.23.1
Requires:       crate(uuid-1.0/v4) >= 1.23.1
Requires:       crate(vm-memory-0.17/backend-mmap) >= 0.17.1
Requires:       crate(vm-memory-0.17/default) >= 0.17.1
Requires:       crate(vmm-sys-util-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/postcopy)
Provides:       crate(%{pkgname}/test-utils)
Provides:       crate(%{pkgname}/vhost-kern)
Provides:       crate(%{pkgname}/vhost-net)
Provides:       crate(%{pkgname}/vhost-user)
Provides:       crate(%{pkgname}/vhost-user-backend)
Provides:       crate(%{pkgname}/vhost-user-frontend)
Provides:       crate(%{pkgname}/vhost-vdpa)
Provides:       crate(%{pkgname}/vhost-vsock)

%description
Source code for takopackized Rust crate "vhost"

%package     -n %{name}+xen
Summary:        Pure rust library for vdpa, vhost and vhost-user - feature "xen"
Requires:       crate(%{pkgname})
Requires:       crate(vm-memory-0.17/backend-mmap) >= 0.17.1
Requires:       crate(vm-memory-0.17/xen) >= 0.17.1
Provides:       crate(%{pkgname}/xen)

%description -n %{name}+xen
This metapackage enables feature "xen" for the Rust vhost crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

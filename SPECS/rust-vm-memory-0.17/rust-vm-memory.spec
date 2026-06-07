%global crate_name vm-memory
%global full_version 0.17.1
%global pkgname vm-memory-0.17

Name:           rust-vm-memory-0.17
Version:        0.17.1
Release:        %autorelease
Summary:        Rust crate "vm-memory"
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/rust-vmm/vm-memory
#!RemoteAsset:  sha256:f39348a049689cabd3377cdd9182bf526ec76a6f823b79903896452e9d7a7380
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(thiserror-2/default) >= 2.0.18
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "vm-memory"

%package     -n %{name}+arc-swap
Summary:        Safe abstractions for accessing the VM physical memory - feature "arc-swap" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(arc-swap-1/default) >= 1.9.1
Provides:       crate(%{pkgname}/arc-swap)
Provides:       crate(%{pkgname}/backend-atomic)

%description -n %{name}+arc-swap
This metapackage enables feature "arc-swap" for the Rust vm-memory crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "backend-atomic" feature.

%package     -n %{name}+backend-bitmap
Summary:        Safe abstractions for accessing the VM physical memory - feature "backend-bitmap" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(libc-0.2/default) >= 0.2.186
Requires:       crate(winapi-0.3/default) >= 0.3.9
Requires:       crate(winapi-0.3/errhandlingapi) >= 0.3.9
Requires:       crate(winapi-0.3/sysinfoapi) >= 0.3.9
Provides:       crate(%{pkgname}/backend-bitmap)
Provides:       crate(%{pkgname}/backend-mmap)

%description -n %{name}+backend-bitmap
This metapackage enables feature "backend-bitmap" for the Rust vm-memory crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "backend-mmap" feature.

%package     -n %{name}+bitflags
Summary:        Safe abstractions for accessing the VM physical memory - feature "bitflags"
Requires:       crate(%{pkgname})
Requires:       crate(bitflags-2/default) >= 2.4.0
Provides:       crate(%{pkgname}/bitflags)

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust vm-memory crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rawfd
Summary:        Safe abstractions for accessing the VM physical memory - feature "rawfd" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(libc-0.2/default) >= 0.2.186
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/rawfd)

%description -n %{name}+rawfd
This metapackage enables feature "rawfd" for the Rust vm-memory crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+vmm-sys-util
Summary:        Safe abstractions for accessing the VM physical memory - feature "vmm-sys-util"
Requires:       crate(%{pkgname})
Requires:       crate(vmm-sys-util-0.12/default) >= 0.12.1
Provides:       crate(%{pkgname}/vmm-sys-util)

%description -n %{name}+vmm-sys-util
This metapackage enables feature "vmm-sys-util" for the Rust vm-memory crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xen
Summary:        Safe abstractions for accessing the VM physical memory - feature "xen"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/backend-mmap)
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(%{pkgname}/vmm-sys-util)
Provides:       crate(%{pkgname}/xen)

%description -n %{name}+xen
This metapackage enables feature "xen" for the Rust vm-memory crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

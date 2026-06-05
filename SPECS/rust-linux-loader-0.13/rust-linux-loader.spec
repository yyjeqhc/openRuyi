%global crate_name linux-loader
%global full_version 0.13.2
%global pkgname linux-loader-0.13

Name:           rust-linux-loader-0.13
Version:        0.13.2
Release:        %autorelease
Summary:        Rust crate "linux-loader"
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/rust-vmm/linux-loader
#!RemoteAsset:  sha256:de72cb02c55ecffcf75fe78295926f872eb6eb0a58d629c58a8c324dc26380f6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(vm-memory-0.17/default) >= 0.17.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/bzimage)
Provides:       crate(%{pkgname}/elf)
Provides:       crate(%{pkgname}/pe)

%description
Source code for takopackized Rust crate "linux-loader"

%package     -n %{name}+default
Summary:        Linux kernel image loading crate - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/elf)
Requires:       crate(%{pkgname}/pe)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust linux-loader crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

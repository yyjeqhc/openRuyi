%global crate_name cfg-if
%global full_version 1.0.0
%global pkgname cfg-if-1.0

Name:           rust-cfg-if-1.0
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "cfg-if"
License:        MIT/Apache-2.0
URL:            https://github.com/alexcrichton/cfg-if
#!RemoteAsset:  sha256:baf1de4339761588bc0619e3cbc0120ee582ebb74b53b4efbf79117bd2da40fd
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Structured like an if-else chain, the first matching branch is the item that gets emitted.
Source code for takopackized Rust crate "cfg-if"

%package     -n %{name}+compiler-builtins
Summary:        Macro to ergonomically define an item depending on a large number of #[cfg] parameters - feature "compiler_builtins"
Requires:       crate(%{pkgname})
Requires:       crate(compiler-builtins-0.1/default) >= 0.1.2
Provides:       crate(%{pkgname}/compiler-builtins)

%description -n %{name}+compiler-builtins
Structured like an if-else chain, the first matching branch is the item that gets emitted.
This metapackage enables feature "compiler_builtins" for the Rust cfg-if crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+core
Summary:        Macro to ergonomically define an item depending on a large number of #[cfg] parameters - feature "core"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-core-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/core)

%description -n %{name}+core
Structured like an if-else chain, the first matching branch is the item that gets emitted.
This metapackage enables feature "core" for the Rust cfg-if crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Macro to ergonomically define an item depending on a large number of #[cfg] parameters - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/compiler-builtins)
Requires:       crate(%{pkgname}/core)
Provides:       crate(%{pkgname}/rustc-dep-of-std)

%description -n %{name}+rustc-dep-of-std
Structured like an if-else chain, the first matching branch is the item that gets emitted.
This metapackage enables feature "rustc-dep-of-std" for the Rust cfg-if crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

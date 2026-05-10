%global crate_name bitflags
%global full_version 2.7.0
%global pkgname bitflags-2.0

Name:           rust-bitflags-2.0
Version:        2.7.0
Release:        %autorelease
Summary:        Rust crate "bitflags"
License:        MIT OR Apache-2.0
URL:            https://github.com/bitflags/bitflags
#!RemoteAsset:  sha256:1be3f42a67d6d345ecd59f675f3f012d6974981560836e938c22b424b85ce1be
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{crate_name}) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/example-generated)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "bitflags"

%package     -n %{name}+arbitrary
Summary:        Macro to generate structures which behave like bitflags - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(arbitrary-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust bitflags crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytemuck
Summary:        Macro to generate structures which behave like bitflags - feature "bytemuck"
Requires:       crate(%{pkgname})
Requires:       crate(bytemuck-1.0/default) >= 1.12
Provides:       crate(%{pkgname}/bytemuck)

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust bitflags crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compiler-builtins
Summary:        Macro to generate structures which behave like bitflags - feature "compiler_builtins"
Requires:       crate(%{pkgname})
Requires:       crate(compiler-builtins-0.1/default) >= 0.1.2
Provides:       crate(%{pkgname}/compiler-builtins)

%description -n %{name}+compiler-builtins
This metapackage enables feature "compiler_builtins" for the Rust bitflags crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+core
Summary:        Macro to generate structures which behave like bitflags - feature "core"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-core-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/core)

%description -n %{name}+core
This metapackage enables feature "core" for the Rust bitflags crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Macro to generate structures which behave like bitflags - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/compiler-builtins)
Requires:       crate(%{pkgname}/core)
Provides:       crate(%{pkgname}/rustc-dep-of-std)

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust bitflags crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Macro to generate structures which behave like bitflags - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.103
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust bitflags crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%{?autochangelog}

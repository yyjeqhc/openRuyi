%global crate_name winnow
%global full_version 1.0.3
%global pkgname winnow-1

Name:           rust-winnow-1
Version:        1.0.3
Release:        %autorelease
Summary:        Rust crate "winnow"
License:        MIT
URL:            https://github.com/winnow-rs/winnow
#!RemoteAsset:  sha256:0592e1c9d151f854e6fd382574c3a0855250e1d9b2f99d9281c6e6391af352f1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{full_version}
Provides:       crate(%{pkgname}/alloc) = %{full_version}
Provides:       crate(%{pkgname}/ascii) = %{full_version}
Provides:       crate(%{pkgname}/binary) = %{full_version}
Provides:       crate(%{pkgname}/parser) = %{full_version}
Provides:       crate(%{pkgname}/unstable-recover) = %{full_version}

%description
Source code for takopackized Rust crate "winnow"

%package     -n %{name}+debug
Summary:        Byte-oriented, zero-copy, parser combinators library - feature "debug"
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(%{pkgname}/std) = %{full_version}
Requires:       crate(anstream-0.6/default) >= 0.6.15
Requires:       crate(anstyle-1/default) >= 1.0.8
Requires:       crate(is-terminal-polyfill-1/default) >= 1.48.1
Requires:       crate(terminal-size-0.4/default) >= 0.4.3
Provides:       crate(%{pkgname}/debug) = %{full_version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust winnow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Byte-oriented, zero-copy, parser combinators library - feature "default"
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(%{pkgname}/ascii) = %{full_version}
Requires:       crate(%{pkgname}/binary) = %{full_version}
Requires:       crate(%{pkgname}/std) = %{full_version}
Provides:       crate(%{pkgname}/default) = %{full_version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust winnow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+simd
Summary:        Byte-oriented, zero-copy, parser combinators library - feature "simd"
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(memchr-2) >= 2.7.0
Provides:       crate(%{pkgname}/simd) = %{full_version}

%description -n %{name}+simd
This metapackage enables feature "simd" for the Rust winnow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Byte-oriented, zero-copy, parser combinators library - feature "std"
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(%{pkgname}/alloc) = %{full_version}
Requires:       crate(memchr-2/std) >= 2.7.0
Provides:       crate(%{pkgname}/std) = %{full_version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust winnow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-doc
Summary:        Byte-oriented, zero-copy, parser combinators library - feature "unstable-doc"
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(%{pkgname}/alloc) = %{full_version}
Requires:       crate(%{pkgname}/ascii) = %{full_version}
Requires:       crate(%{pkgname}/binary) = %{full_version}
Requires:       crate(%{pkgname}/simd) = %{full_version}
Requires:       crate(%{pkgname}/std) = %{full_version}
Requires:       crate(%{pkgname}/unstable-recover) = %{full_version}
Provides:       crate(%{pkgname}/unstable-doc) = %{full_version}

%description -n %{name}+unstable-doc
This metapackage enables feature "unstable-doc" for the Rust winnow crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

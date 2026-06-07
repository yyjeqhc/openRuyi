%global crate_name toml_edit
%global full_version 0.25.11+spec-1.1.0
%global pkgname toml-edit-0.25

Name:           rust-toml-edit-0.25
Version:        0.25.11
Release:        %autorelease
Summary:        Rust crate "toml_edit"
License:        MIT OR Apache-2.0
URL:            https://github.com/toml-rs/toml
#!RemoteAsset:  sha256:0b59c4d22ed448339746c59b905d24568fcbb3ab65a500494f7b8c3e97739f2b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(indexmap-2.0/default) >= 2.14.0
Requires:       crate(indexmap-2.0/std) >= 2.14.0
Requires:       crate(toml-datetime-1.0/default) >= 1.1.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/unbounded)

%description
Source code for takopackized Rust crate "toml_edit"

%package     -n %{name}+debug
Summary:        Yet another format-preserving TOML parser - feature "debug"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/display)
Requires:       crate(anstream-1/default) >= 1.0.0
Requires:       crate(anstyle-1/default) >= 1.0.14
Requires:       crate(toml-parser-1.0/debug) >= 1.1.2
Provides:       crate(%{pkgname}/debug)

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust toml_edit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Yet another format-preserving TOML parser - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/display)
Requires:       crate(%{pkgname}/parse)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust toml_edit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+display
Summary:        Yet another format-preserving TOML parser - feature "display"
Requires:       crate(%{pkgname})
Requires:       crate(toml-writer-1.0/default) >= 1.1.1
Provides:       crate(%{pkgname}/display)

%description -n %{name}+display
This metapackage enables feature "display" for the Rust toml_edit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parse
Summary:        Yet another format-preserving TOML parser - feature "parse"
Requires:       crate(%{pkgname})
Requires:       crate(toml-parser-1.0/default) >= 1.1.2
Requires:       crate(winnow-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/parse)

%description -n %{name}+parse
This metapackage enables feature "parse" for the Rust toml_edit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Yet another format-preserving TOML parser - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1/default) >= 1.0.228
Requires:       crate(serde-spanned-1/default) >= 1.1.1
Requires:       crate(serde-spanned-1/serde) >= 1.1.1
Requires:       crate(toml-datetime-1.0/serde) >= 1.1.1
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust toml_edit crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

%global crate_name event-listener-strategy
%global full_version 0.5.4
%global pkgname event-listener-strategy-0.5

Name:           rust-event-listener-strategy-0.5
Version:        0.5.4
Release:        %autorelease
Summary:        Rust crate "event-listener-strategy"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/event-listener-strategy
#!RemoteAsset:  sha256:8be9f3dfaaffdae2972880079a491a1a8bb7cbed0b8dd7a347f668b4150a3b93
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(event-listener-5.0) >= 5.4.1
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.17
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "event-listener-strategy"

%package     -n %{name}+loom
Summary:        Block or poll on event_listener easily - feature "loom"
Requires:       crate(%{pkgname})
Requires:       crate(event-listener-5.0/loom) >= 5.4.1
Provides:       crate(%{pkgname}/loom)

%description -n %{name}+loom
This metapackage enables feature "loom" for the Rust event-listener-strategy crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic
Summary:        Block or poll on event_listener easily - feature "portable-atomic"
Requires:       crate(%{pkgname})
Requires:       crate(event-listener-5.0/portable-atomic) >= 5.4.1
Provides:       crate(%{pkgname}/portable-atomic)

%description -n %{name}+portable-atomic
This metapackage enables feature "portable-atomic" for the Rust event-listener-strategy crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Block or poll on event_listener easily - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(event-listener-5.0/std) >= 5.4.1
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust event-listener-strategy crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

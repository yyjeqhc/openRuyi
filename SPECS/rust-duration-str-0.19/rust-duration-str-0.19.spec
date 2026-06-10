%global crate_name duration-str
%global full_version 0.19.0
%global pkgname duration-str-0.19

Name:           rust-duration-str-0.19
Version:        0.19.0
Release:        %autorelease
Summary:        Rust crate "duration-str"
License:        Apache-2.0
URL:            https://github.com/baoyachi/duration-str
#!RemoteAsset:  sha256:12494809f9915b6132014cc259c4e204ab53ab6c6dd2225672703b5359267d82
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rust-decimal-1) >= 1.29.1
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(winnow-0.7/default) >= 0.7.4
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/cn-unit) = %{version}
Provides:       crate(%{pkgname}/lowercase) = %{version}
Provides:       crate(%{pkgname}/no-calc) = %{version}

%description
Source code for takopackized Rust crate "duration-str"

%package     -n %{name}+chrono
Summary:        Duration string parser - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/now) >= 0.4.38
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust duration-str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Duration string parser - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/chrono) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/time) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust duration-str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Duration string parser - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.147
Requires:       crate(serde-1/derive) >= 1.0.147
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust duration-str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        Duration string parser - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3) >= 0.3.17
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust duration-str crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

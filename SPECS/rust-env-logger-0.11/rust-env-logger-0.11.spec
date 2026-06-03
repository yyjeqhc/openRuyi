# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name env_logger
%global full_version 0.11.10
%global pkgname env-logger-0.11

Name:           rust-env-logger-0.11
Version:        0.11.10
Release:        %autorelease
Summary:        Rust crate "env_logger"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-cli/env_logger
#!RemoteAsset:  sha256:0621c04f2196ac3f488dd583365b9c09be011a4ab8b9f37248ffcc8f6198b56a
Source:         https://static.crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(env-filter-1.0) >= 1.0.1
Requires:       crate(log-0.4/default) >= 0.4.31
Requires:       crate(log-0.4/std) >= 0.4.31
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "env_logger"

%package     -n %{name}+auto-color
Summary:        Logging implementation for `log` which is configured via an environment variable - feature "auto-color"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/color)
Requires:       crate(anstream-1.0/auto) >= 1.0.0
Requires:       crate(anstream-1.0/wincon) >= 1.0.0
Provides:       crate(%{pkgname}/auto-color)

%description -n %{name}+auto-color
This metapackage enables feature "auto-color" for the Rust env_logger crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+color
Summary:        Logging implementation for `log` which is configured via an environment variable - feature "color"
Requires:       crate(%{pkgname})
Requires:       crate(anstream-1.0/wincon) >= 1.0.0
Requires:       crate(anstyle-1.0/default) >= 1.0.14
Provides:       crate(%{pkgname}/color)

%description -n %{name}+color
This metapackage enables feature "color" for the Rust env_logger crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Logging implementation for `log` which is configured via an environment variable - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/auto-color)
Requires:       crate(%{pkgname}/humantime)
Requires:       crate(%{pkgname}/regex)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust env_logger crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+humantime
Summary:        Logging implementation for `log` which is configured via an environment variable - feature "humantime"
Requires:       crate(%{pkgname})
Requires:       crate(jiff-0.2/std) >= 0.2.28
Provides:       crate(%{pkgname}/humantime)

%description -n %{name}+humantime
This metapackage enables feature "humantime" for the Rust env_logger crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+kv
Summary:        Logging implementation for `log` which is configured via an environment variable - feature "kv" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(log-0.4/kv) >= 0.4.31
Requires:       crate(log-0.4/std) >= 0.4.31
Provides:       crate(%{pkgname}/kv)
Provides:       crate(%{pkgname}/unstable-kv)

%description -n %{name}+kv
This metapackage enables feature "kv" for the Rust env_logger crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unstable-kv" feature.

%package     -n %{name}+regex
Summary:        Logging implementation for `log` which is configured via an environment variable - feature "regex"
Requires:       crate(%{pkgname})
Requires:       crate(env-filter-1.0/regex) >= 1.0.1
Provides:       crate(%{pkgname}/regex)

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust env_logger crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

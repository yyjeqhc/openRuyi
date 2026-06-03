# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name flume
%global full_version 0.12.0
%global pkgname flume-0.12

Name:           rust-flume-0.12
Version:        0.12.0
Release:        %autorelease
Summary:        Rust crate "flume"
License:        Apache-2.0/MIT
URL:            https://github.com/zesterer/flume
#!RemoteAsset:  sha256:5e139bc46ca777eb5efaf62df0ab8cc5fd400866427e56c68b22e414e53bd3be
Source:         https://static.crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(spin-0.9/default) >= 0.9.8
Requires:       crate(spin-0.9/mutex) >= 0.9.8
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/select)
Provides:       crate(%{pkgname}/spin)

%description
Source code for takopackized Rust crate "flume"

%package     -n %{name}+async
Summary:        Blazingly fast multi-producer channel - feature "async"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures-core)
Requires:       crate(%{pkgname}/futures-sink)
Provides:       crate(%{pkgname}/async)

%description -n %{name}+async
This metapackage enables feature "async" for the Rust flume crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Blazingly fast multi-producer channel - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async)
Requires:       crate(%{pkgname}/eventual-fairness)
Requires:       crate(%{pkgname}/select)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust flume crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+eventual-fairness
Summary:        Blazingly fast multi-producer channel - feature "eventual-fairness"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/fastrand)
Requires:       crate(%{pkgname}/select)
Provides:       crate(%{pkgname}/eventual-fairness)

%description -n %{name}+eventual-fairness
This metapackage enables feature "eventual-fairness" for the Rust flume crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fastrand
Summary:        Blazingly fast multi-producer channel - feature "fastrand"
Requires:       crate(%{pkgname})
Requires:       crate(fastrand-2.0/default) >= 2.4.1
Requires:       crate(fastrand-2.0/js) >= 2.4.1
Requires:       crate(fastrand-2.0/std) >= 2.4.1
Provides:       crate(%{pkgname}/fastrand)

%description -n %{name}+fastrand
This metapackage enables feature "fastrand" for the Rust flume crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-core
Summary:        Blazingly fast multi-producer channel - feature "futures-core"
Requires:       crate(%{pkgname})
Requires:       crate(futures-core-0.3) >= 0.3.32
Provides:       crate(%{pkgname}/futures-core)

%description -n %{name}+futures-core
This metapackage enables feature "futures-core" for the Rust flume crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-sink
Summary:        Blazingly fast multi-producer channel - feature "futures-sink"
Requires:       crate(%{pkgname})
Requires:       crate(futures-sink-0.3) >= 0.3.32
Provides:       crate(%{pkgname}/futures-sink)

%description -n %{name}+futures-sink
This metapackage enables feature "futures-sink" for the Rust flume crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

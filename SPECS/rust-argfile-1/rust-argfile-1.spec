# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name argfile
%global full_version 1.0.0
%global pkgname argfile-1

Name:           rust-argfile-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "argfile"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-cli/argfile
#!RemoteAsset:  sha256:99489a733dea0d2930bfa59c243146a8513ce7b0991b9d006647687cc61f53e7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fs-err-3/default) >= 3.0.0
Requires:       crate(os-str-bytes-7/default) >= 7.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "argfile"

%package     -n %{name}+response
Summary:        Load additional CLI args from file - feature "response"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(winsplit-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/response) = %{version}

%description -n %{name}+response
This metapackage enables feature "response" for the Rust argfile crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

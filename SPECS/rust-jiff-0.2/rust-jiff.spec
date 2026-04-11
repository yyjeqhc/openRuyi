# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jiff
%global full_version 0.2.23
%global pkgname jiff-0.2

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-jiff-0.2
Version:        0.2.23
Release:        %autorelease
Summary:        Rust crate "jiff"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/jiff
#!RemoteAsset:  sha256:1a3546dc96b6d42c5f24902af9e2538e82e39ad350b0c766eb3fbf2d8f3d8359
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(jiff-static-0.2/default) >= 0.2.23
Requires:       crate(portable-atomic-1.0) >= 1.13.1
Requires:       crate(portable-atomic-util-0.2) >= 0.2.6
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/perf-inline)

%description
This library is heavily inspired by the Temporal project.
Source code for takopackized Rust crate "jiff"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

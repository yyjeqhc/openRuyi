# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name anstream
%global full_version 1.0.0
%global pkgname anstream-1.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-anstream-1.0
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "anstream"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-cli/anstyle.git
#!RemoteAsset:  sha256:824a212faf96e9acacdbd09febd34438f8f711fb84e09a8916013cd7815ca28d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(anstyle-1.0/default) >= 1.0.14
Requires:       crate(anstyle-parse-1.0/default) >= 1.0.0
Requires:       crate(colorchoice-1.0/default) >= 1.0.5
Requires:       crate(is-terminal-polyfill-1.0/default) >= 1.70.2
Requires:       crate(utf8parse-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/test)

%description
Source code for takopackized Rust crate "anstream"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

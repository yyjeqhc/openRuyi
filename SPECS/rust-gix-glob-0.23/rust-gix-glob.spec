# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-glob
%global full_version 0.23.0
%global pkgname gix-glob-0.23

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-gix-glob-0.23
Version:        0.23.0
Release:        %autorelease
Summary:        Rust crate "gix-glob"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:e8546300aee4c65c5862c22a3e321124a69b654a61a8b60de546a9284812b7e2
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bitflags-2.0/default) >= 2.11.0
Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(gix-features-0.45/default) >= 0.45.2
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-glob"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

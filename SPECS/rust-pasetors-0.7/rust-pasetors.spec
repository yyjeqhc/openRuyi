# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pasetors
%global full_version 0.7.8
%global pkgname pasetors-0.7

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-pasetors-0.7
Version:        0.7.8
Release:        %autorelease
Summary:        Rust crate "pasetors"
License:        MIT
URL:            https://github.com/brycx/pasetors
#!RemoteAsset:  sha256:e838401fb2873bad417e6a03179014c748746f67311cb7317ab14fc0881fa9f0
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(ct-codecs-1.0) >= 1.1.6
Requires:       crate(getrandom-0.4/default) >= 0.4.2
Requires:       crate(subtle-2.0) >= 2.6.1
Requires:       crate(zeroize-1.0) >= 1.8.2
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "pasetors"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

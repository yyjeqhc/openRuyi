# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name time
%global full_version 0.3.47
%global pkgname time-0.3

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-time-0.3
Version:        0.3.47
Release:        %autorelease
Summary:        Rust crate "time"
License:        MIT OR Apache-2.0
URL:            https://time-rs.github.io
#!RemoteAsset:  sha256:743bd48c283afc0388f9b8827b976905fb217ad9e647fae3a379a9283c4def2c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(deranged-0.5/default) >= 0.5.8
Requires:       crate(deranged-0.5/powerfmt) >= 0.5.8
Requires:       crate(num-conv-0.2/default) >= 0.2.1
Requires:       crate(powerfmt-0.2) >= 0.2.0
Requires:       crate(time-core-0.1/default) >= 0.1.8
Provides:       crate(%{pkgname})

%description
Fully interoperable with the standard library. Mostly compatible with #![no_std].
Source code for takopackized Rust crate "time"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

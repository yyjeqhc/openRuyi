# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crunchy
%global full_version 0.2.4
%global pkgname crunchy-0.2

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-crunchy-0.2
Version:        0.2.4
Release:        %autorelease
Summary:        Rust crate "crunchy"
License:        MIT
URL:            https://github.com/eira-fransham/crunchy
#!RemoteAsset:  sha256:460fbee9c2c2f33933d720630a6a0bac33ba7053db5344fac858d4b8952d77d5
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/limit-1024)
Provides:       crate(%{pkgname}/limit-128)
Provides:       crate(%{pkgname}/limit-2048)
Provides:       crate(%{pkgname}/limit-256)
Provides:       crate(%{pkgname}/limit-512)
Provides:       crate(%{pkgname}/limit-64)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "crunchy"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name parking_lot_core
%global full_version 0.9.12
%global pkgname parking-lot-core-0.9

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-parking-lot-core-0.9
Version:        0.9.12
Release:        %autorelease
Summary:        Rust crate "parking_lot_core"
License:        MIT OR Apache-2.0
URL:            https://github.com/Amanieu/parking_lot
#!RemoteAsset:  sha256:2621685985a2ebf1c516881c026032ac7deafcda1a2c9b7850dc81e3dfcb64c1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(redox-syscall-0.5/default) >= 0.5.18
Requires:       crate(smallvec-1.0/default) >= 1.15.1
Requires:       crate(windows-link-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/nightly)

%description
Source code for takopackized Rust crate "parking_lot_core"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

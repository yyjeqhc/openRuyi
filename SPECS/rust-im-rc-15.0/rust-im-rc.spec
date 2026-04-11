# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name im-rc
%global full_version 15.1.0
%global pkgname im-rc-15.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-im-rc-15.0
Version:        15.1.0
Release:        %autorelease
Summary:        Rust crate "im-rc"
License:        MPL-2.0+
URL:            http://immutable.rs/
#!RemoteAsset:  sha256:af1955a75fa080c677d3972822ec4bad316169ab1cfc6c257a942c2265dbe5fe
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bitmaps-2.0/default) >= 2.1.0
Requires:       crate(rand-core-0.6/default) >= 0.6.4
Requires:       crate(rand-xoshiro-0.6/default) >= 0.6.0
Requires:       crate(sized-chunks-0.6/default) >= 0.6.5
Requires:       crate(typenum-1.0/default) >= 1.19.0
Requires:       crate(version-check-0.9/default) >= 0.9.5
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/debug)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "im-rc"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

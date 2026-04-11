# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-protocol
%global full_version 0.55.0
%global pkgname gix-protocol-0.55

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-gix-protocol-0.55
Version:        0.55.0
Release:        %autorelease
Summary:        Rust crate "gix-protocol"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:02c5dfd068789442c5709e702ef42d851765f2c09a11bf0a13749d24363f4d07
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(bstr-1.0/unicode) >= 1.12.1
Requires:       crate(gix-date-0.12/default) >= 0.12.1
Requires:       crate(gix-features-0.45/default) >= 0.45.2
Requires:       crate(gix-features-0.45/progress) >= 0.45.2
Requires:       crate(gix-hash-0.21/default) >= 0.21.2
Requires:       crate(gix-ref-0.57/default) >= 0.57.0
Requires:       crate(gix-shallow-0.7/default) >= 0.7.0
Requires:       crate(gix-transport-0.52/default) >= 0.52.1
Requires:       crate(gix-utils-0.3/default) >= 0.3.1
Requires:       crate(maybe-async-0.2/default) >= 0.2.10
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Requires:       crate(winnow-0.7/default) >= 0.7.15
Requires:       crate(winnow-0.7/simd) >= 0.7.15
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-protocol"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

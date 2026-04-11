# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-packetline
%global full_version 0.20.0
%global pkgname gix-packetline-0.20

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-gix-packetline-0.20
Version:        0.20.0
Release:        %autorelease
Summary:        Rust crate "gix-packetline"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:fad0ffb982a289888087a165d3e849cbac724f2aa5431236b050dd2cb9c7de31
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(faster-hex-0.10/std) >= 0.10.0
Requires:       crate(gix-trace-0.1/default) >= 0.1.18
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/blocking-io)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-packetline"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

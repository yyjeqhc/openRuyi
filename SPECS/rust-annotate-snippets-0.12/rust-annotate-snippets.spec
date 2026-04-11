# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name annotate-snippets
%global full_version 0.12.15
%global pkgname annotate-snippets-0.12

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-annotate-snippets-0.12
Version:        0.12.15
Release:        %autorelease
Summary:        Rust crate "annotate-snippets"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/annotate-snippets-rs
#!RemoteAsset:  sha256:92570a3f9c98e7e84df84b71d0965ac99b1871fcd75a3773a3bd1bad13f64cf7
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(anstyle-1.0) >= 1.0.14
Requires:       crate(unicode-width-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/testing-colors)

%description
Source code for takopackized Rust crate "annotate-snippets"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

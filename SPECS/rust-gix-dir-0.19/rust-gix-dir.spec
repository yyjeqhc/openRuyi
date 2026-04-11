# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-dir
%global full_version 0.19.0
%global pkgname gix-dir-0.19

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-gix-dir-0.19
Version:        0.19.0
Release:        %autorelease
Summary:        Rust crate "gix-dir"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:709d9fad32d2eb8b0129850874246569e801b6d5877e0c41356c23e9e2501e06
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bstr-1.0) >= 1.12.1
Requires:       crate(gix-discover-0.45/default) >= 0.45.0
Requires:       crate(gix-fs-0.18/default) >= 0.18.2
Requires:       crate(gix-ignore-0.18/default) >= 0.18.0
Requires:       crate(gix-index-0.45/default) >= 0.45.1
Requires:       crate(gix-object-0.54/default) >= 0.54.1
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(gix-pathspec-0.14/default) >= 0.14.0
Requires:       crate(gix-trace-0.1/default) >= 0.1.18
Requires:       crate(gix-utils-0.3/bstr) >= 0.3.1
Requires:       crate(gix-utils-0.3/default) >= 0.3.1
Requires:       crate(gix-worktree-0.46) >= 0.46.0
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-dir"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

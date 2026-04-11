# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-status
%global full_version 0.24.0
%global pkgname gix-status-0.24

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-gix-status-0.24
Version:        0.24.0
Release:        %autorelease
Summary:        Rust crate "gix-status"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:ed0d94c685a831c679ca5454c22f350e8c233f50dcf377ca00d858bcba9696d2
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bstr-1.0) >= 1.12.1
Requires:       crate(filetime-0.2/default) >= 0.2.27
Requires:       crate(gix-features-0.45/default) >= 0.45.2
Requires:       crate(gix-features-0.45/progress) >= 0.45.2
Requires:       crate(gix-filter-0.24/default) >= 0.24.1
Requires:       crate(gix-fs-0.18/default) >= 0.18.2
Requires:       crate(gix-hash-0.21/default) >= 0.21.2
Requires:       crate(gix-index-0.45/default) >= 0.45.1
Requires:       crate(gix-object-0.54/default) >= 0.54.1
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(gix-pathspec-0.14/default) >= 0.14.0
Requires:       crate(gix-worktree-0.46/attributes) >= 0.46.0
Requires:       crate(portable-atomic-1.0/default) >= 1.13.1
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-status"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

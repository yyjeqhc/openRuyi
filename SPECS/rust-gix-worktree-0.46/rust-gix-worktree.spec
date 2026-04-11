# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-worktree
%global full_version 0.46.0
%global pkgname gix-worktree-0.46

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-gix-worktree-0.46
Version:        0.46.0
Release:        %autorelease
Summary:        Rust crate "gix-worktree"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:1cfb7ce8cdbfe06117d335d1ad329351468d20331e0aafd108ceb647c1326aca
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bstr-1.0) >= 1.12.1
Requires:       crate(gix-features-0.45/default) >= 0.45.2
Requires:       crate(gix-fs-0.18/default) >= 0.18.2
Requires:       crate(gix-glob-0.23/default) >= 0.23.0
Requires:       crate(gix-hash-0.21/default) >= 0.21.2
Requires:       crate(gix-ignore-0.18/default) >= 0.18.0
Requires:       crate(gix-index-0.45/default) >= 0.45.1
Requires:       crate(gix-object-0.54/default) >= 0.54.1
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "gix-worktree"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

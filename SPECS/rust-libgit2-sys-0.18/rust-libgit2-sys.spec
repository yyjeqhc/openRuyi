# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libgit2-sys
%global full_version 0.18.3+1.9.2
%global pkgname libgit2-sys-0.18

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-libgit2-sys-0.18
Version:        0.18.3
Release:        %autorelease
Summary:        Rust crate "libgit2-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/git2-rs
#!RemoteAsset:  sha256:c9b3acc4b91781bb0b3386669d325163746af5f6e4f73e6d2d630e09a35f3487
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(cc-1.0/default) >= 1.2.60
Requires:       crate(cc-1.0/parallel) >= 1.2.60
Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(libz-sys-1.0/libc) >= 1.1.28
Requires:       crate(pkg-config-0.3/default) >= 0.3.32
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/vendored)

%description
Source code for takopackized Rust crate "libgit2-sys"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

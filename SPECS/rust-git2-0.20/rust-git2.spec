# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name git2
%global full_version 0.20.4
%global pkgname git2-0.20

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-git2-0.20
Version:        0.20.4
Release:        %autorelease
Summary:        Rust crate "git2"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/git2-rs
#!RemoteAsset:  sha256:7b88256088d75a56f8ecfa070513a775dd9107f6530ef14919dac831af9cfe2b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bitflags-2.0/default) >= 2.11.0
Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(libgit2-sys-0.18/default) >= 0.18.3
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(url-2.0/default) >= 2.5.8
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/unstable)

%description
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
Source code for takopackized Rust crate "git2"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

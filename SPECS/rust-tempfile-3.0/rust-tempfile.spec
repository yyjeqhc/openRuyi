# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tempfile
%global full_version 3.27.0
%global pkgname tempfile-3.0

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-tempfile-3.0
Version:        3.27.0
Release:        %autorelease
Summary:        Rust crate "tempfile"
License:        MIT OR Apache-2.0
URL:            https://stebalien.com/projects/tempfile-rs/
#!RemoteAsset:  sha256:32497e9a4c7b38532efcdebeef879707aa9f794296a4f0244f6f69e9bc8574bd
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(fastrand-2.0/default) >= 2.4.1
Requires:       crate(once-cell-1.0/std) >= 1.21.4
Requires:       crate(rustix-1.0/default) >= 1.1.4
Requires:       crate(rustix-1.0/fs) >= 1.1.4
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-storage-filesystem) >= 0.61.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/nightly)

%description
Source code for takopackized Rust crate "tempfile"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

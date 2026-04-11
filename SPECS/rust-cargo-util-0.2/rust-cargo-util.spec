# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo-util
%global full_version 0.2.27
%global pkgname cargo-util-0.2

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-cargo-util-0.2
Version:        0.2.27
Release:        %autorelease
Summary:        Rust crate "cargo-util"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/cargo
#!RemoteAsset:  sha256:4a4b72539a4e322539ac3cd07d7e63d60ca3823f3143a2d39a9f8fcdace0e8ca
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(anyhow-1.0/default) >= 1.0.102
Requires:       crate(core-foundation-0.10/default) >= 0.10.1
Requires:       crate(core-foundation-0.10/mac-os-10-7-support) >= 0.10.1
Requires:       crate(filetime-0.2/default) >= 0.2.27
Requires:       crate(hex-0.4/default) >= 0.4.3
Requires:       crate(ignore-0.4/default) >= 0.4.25
Requires:       crate(jobserver-0.1/default) >= 0.1.34
Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(miow-0.6/default) >= 0.6.1
Requires:       crate(same-file-1.0/default) >= 1.0.6
Requires:       crate(sha2-0.10/default) >= 0.10.9
Requires:       crate(shell-escape-0.1/default) >= 0.1.5
Requires:       crate(tempfile-3.0/default) >= 3.27.0
Requires:       crate(tracing-0.1/std) >= 0.1.44
Requires:       crate(walkdir-2.0/default) >= 2.5.0
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-storage-filesystem) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-console) >= 0.61.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "cargo-util"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

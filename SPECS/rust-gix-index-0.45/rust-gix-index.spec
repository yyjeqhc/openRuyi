# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-index
%global full_version 0.45.1
%global pkgname gix-index-0.45

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-gix-index-0.45
Version:        0.45.1
Release:        %autorelease
Summary:        Rust crate "gix-index"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:9ea6d3e9e11647ba49f441dea0782494cc6d2875ff43fa4ad9094e6957f42051
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(bitflags-2.0/default) >= 2.11.0
Requires:       crate(bstr-1.0) >= 1.12.1
Requires:       crate(filetime-0.2/default) >= 0.2.27
Requires:       crate(fnv-1.0/default) >= 1.0.7
Requires:       crate(gix-bitmap-0.2/default) >= 0.2.16
Requires:       crate(gix-features-0.45/default) >= 0.45.2
Requires:       crate(gix-features-0.45/progress) >= 0.45.2
Requires:       crate(gix-fs-0.18/default) >= 0.18.2
Requires:       crate(gix-hash-0.21/default) >= 0.21.2
Requires:       crate(gix-lock-20.0/default) >= 20.0.1
Requires:       crate(gix-object-0.54/default) >= 0.54.1
Requires:       crate(gix-traverse-0.51/default) >= 0.51.1
Requires:       crate(gix-utils-0.3/default) >= 0.3.1
Requires:       crate(gix-validate-0.10/default) >= 0.10.1
Requires:       crate(hashbrown-0.16/default) >= 0.16.1
Requires:       crate(itoa-1.0/default) >= 1.0.18
Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(memmap2-0.9/default) >= 0.9.10
Requires:       crate(rustix-1.0/fs) >= 1.1.4
Requires:       crate(rustix-1.0/std) >= 1.1.4
Requires:       crate(smallvec-1.0/default) >= 1.15.1
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-index"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

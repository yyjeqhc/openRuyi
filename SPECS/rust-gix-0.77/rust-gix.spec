# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix
%global full_version 0.77.0
%global pkgname gix-0.77

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-gix-0.77
Version:        0.77.0
Release:        %autorelease
Summary:        Rust crate "gix"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:3d8284d86a2f5c0987fbf7219a128815cc04af5a18f5fd7eec6a76d83c2b78cc
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(gix-actor-0.37/default) >= 0.37.1
Requires:       crate(gix-commitgraph-0.31/default) >= 0.31.0
Requires:       crate(gix-config-0.50/default) >= 0.50.0
Requires:       crate(gix-date-0.12/default) >= 0.12.1
Requires:       crate(gix-diff-0.57) >= 0.57.1
Requires:       crate(gix-discover-0.45/default) >= 0.45.0
Requires:       crate(gix-features-0.45/default) >= 0.45.2
Requires:       crate(gix-features-0.45/once-cell) >= 0.45.2
Requires:       crate(gix-features-0.45/progress) >= 0.45.2
Requires:       crate(gix-fs-0.18/default) >= 0.18.2
Requires:       crate(gix-glob-0.23/default) >= 0.23.0
Requires:       crate(gix-hash-0.21/default) >= 0.21.2
Requires:       crate(gix-hashtable-0.11/default) >= 0.11.0
Requires:       crate(gix-lock-20.0/default) >= 20.0.1
Requires:       crate(gix-object-0.54/default) >= 0.54.1
Requires:       crate(gix-odb-0.74/default) >= 0.74.0
Requires:       crate(gix-pack-0.64/object-cache-dynamic) >= 0.64.1
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(gix-protocol-0.55/default) >= 0.55.0
Requires:       crate(gix-ref-0.57/default) >= 0.57.0
Requires:       crate(gix-refspec-0.35/default) >= 0.35.0
Requires:       crate(gix-revision-0.39) >= 0.39.0
Requires:       crate(gix-revwalk-0.25/default) >= 0.25.0
Requires:       crate(gix-sec-0.12/default) >= 0.12.2
Requires:       crate(gix-shallow-0.7/default) >= 0.7.0
Requires:       crate(gix-tempfile-20.0) >= 20.0.1
Requires:       crate(gix-trace-0.1/default) >= 0.1.18
Requires:       crate(gix-traverse-0.51/default) >= 0.51.1
Requires:       crate(gix-url-0.34/default) >= 0.34.0
Requires:       crate(gix-utils-0.3/default) >= 0.3.1
Requires:       crate(gix-validate-0.10/default) >= 0.10.1
Requires:       crate(smallvec-1.0/default) >= 1.15.1
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/tree-editor)

%description
Source code for takopackized Rust crate "gix"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name criterion
%global full_version 0.8.2
%global pkgname criterion-0.8

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-criterion-0.8
Version:        0.8.2
Release:        %autorelease
Summary:        Rust crate "criterion"
License:        Apache-2.0 OR MIT
URL:            https://criterion-rs.github.io/book/index.html
#!RemoteAsset:  sha256:950046b2aa2492f9a536f5f4f9a3de7b9e2476e575e05bd6c333371add4d98f3
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(alloca-0.4/default) >= 0.4.0
Requires:       crate(anes-0.1/default) >= 0.1.6
Requires:       crate(cast-0.3/default) >= 0.3.0
Requires:       crate(ciborium-0.2/default) >= 0.2.2
Requires:       crate(clap-4.0/help) >= 4.6.0
Requires:       crate(clap-4.0/std) >= 4.6.0
Requires:       crate(criterion-plot-0.8/default) >= 0.8.2
Requires:       crate(itertools-0.13/default) >= 0.13.0
Requires:       crate(num-traits-0.2/std) >= 0.2.19
Requires:       crate(oorandom-11.0/default) >= 11.1.5
Requires:       crate(page-size-0.6/default) >= 0.6.0
Requires:       crate(regex-1.0/std) >= 1.12.3
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Requires:       crate(tinytemplate-1.0/default) >= 1.2.1
Requires:       crate(walkdir-2.0/default) >= 2.5.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/async)
Provides:       crate(%{pkgname}/cargo-bench-support)
Provides:       crate(%{pkgname}/html-reports)
Provides:       crate(%{pkgname}/real-blackbox)

%description
Source code for takopackized Rust crate "criterion"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

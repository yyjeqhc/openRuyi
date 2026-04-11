# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name plotters
%global full_version 0.3.7
%global pkgname plotters-0.3

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-plotters-0.3
Version:        0.3.7
Release:        %autorelease
Summary:        Rust crate "plotters"
License:        MIT
URL:            https://plotters-rs.github.io/
#!RemoteAsset:  sha256:5aeb6f403d7a4911efb1e33402027fc44f29b5bf6def3effcc22d7bb75f2b747
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(num-traits-0.2/default) >= 0.2.19
Requires:       crate(plotters-backend-0.3/default) >= 0.3.7
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.118
Requires:       crate(web-sys-0.3/canvasrenderingcontext2d) >= 0.3.95
Requires:       crate(web-sys-0.3/default) >= 0.3.95
Requires:       crate(web-sys-0.3/document) >= 0.3.95
Requires:       crate(web-sys-0.3/domrect) >= 0.3.95
Requires:       crate(web-sys-0.3/element) >= 0.3.95
Requires:       crate(web-sys-0.3/htmlcanvaselement) >= 0.3.95
Requires:       crate(web-sys-0.3/htmlelement) >= 0.3.95
Requires:       crate(web-sys-0.3/node) >= 0.3.95
Requires:       crate(web-sys-0.3/window) >= 0.3.95
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/area-series)
Provides:       crate(%{pkgname}/boxplot)
Provides:       crate(%{pkgname}/candlestick)
Provides:       crate(%{pkgname}/colormaps)
Provides:       crate(%{pkgname}/deprecated-items)
Provides:       crate(%{pkgname}/errorbar)
Provides:       crate(%{pkgname}/full-palette)
Provides:       crate(%{pkgname}/histogram)
Provides:       crate(%{pkgname}/line-series)
Provides:       crate(%{pkgname}/point-series)
Provides:       crate(%{pkgname}/surface-series)

%description
Source code for takopackized Rust crate "plotters"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <zhengjunjie@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name micro_http
%global full_version 0.1.0
%global pkgname micro-http-0.1

%global micro_http_commit 876f3feccc30e09225f2c77bf95a6b2d46a9259e

Name:           rust-micro-http-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        A minimal HTTP library for Rust
License:        Apache-2.0
URL:            https://github.com/firecracker-microvm/micro-http
#!RemoteAsset:  git+https://github.com/firecracker-microvm/micro-http.git#%{micro_http_commit}
#!CreateArchive
Source:         %{crate_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc/default) >= 0.2.66
Requires:       crate(vmm-sys-util/default) >= 0.15.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
A minimal HTTP library that can be used to parse HTTP requests and
generate HTTP responses. This library is designed for use in the
Firecracker VMM.

%files
%license LICENSE
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

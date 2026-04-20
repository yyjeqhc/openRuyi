# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cbindgen
%global full_version 0.29.2

Name:           cbindgen
Version:        0.29.2
Release:        %autorelease
Summary:        Rust crate "cbindgen"
License:        MPL-2.0
URL:            https://github.com/mozilla/cbindgen
#!RemoteAsset:  sha256:befbfd072a8e81c02f8c507aefce431fe5e7d051f83d48a23ffc9b9fe5a11799
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rust

Patch:          1.patch

BuildRequires:  rust-rpm-macros
BuildRequires:  rust
BuildRequires:  python3
BuildRequires:  vim
BuildRequires:  crate(winnow-0.7)
BuildRequires:  crate(winnow-1.0)

%description
binary file of Rust crate "cbindgen".

%generate_buildrequires
%cargo_buildrequires

%install -a
install -Dm0755 target/release/cbindgen %{buildroot}%{_bindir}/cbindgen

%files
%{_bindir}/cbindgen
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

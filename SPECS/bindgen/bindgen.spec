# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bindgen-cli
%global full_version 0.72.1

Name:           bindgen
Version:        0.72.1
Release:        %autorelease
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries
License:        BSD-3-Clause
URL:            https://rust-lang.github.io/rust-bindgen/
VCS:            git:https://github.com/rust-lang/rust-bindgen
#!RemoteAsset:  sha256:8a408c0fcb20bf7bd4ceaf4bf990e223e3543a04b84d2394f3edeee29a0e87e2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{crate_name}-%{version}.tar.gz
BuildSystem:    rust

BuildRequires:  rust-rpm-macros
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  clang-devel
BuildRequires:  crate(bindgen-0.72) >= 0.72.1
BuildRequires:  crate(bindgen-0.72/cli)
BuildRequires:  crate(bindgen-0.72/experimental)
BuildRequires:  crate(bindgen-0.72/prettyplease)
BuildRequires:  crate(bindgen-0.72/runtime)
BuildRequires:  crate(env-logger-0.10) >= 0.10.0
BuildRequires:  crate(env-logger-0.10/default)
BuildRequires:  crate(log-0.4) >= 0.4
BuildRequires:  crate(log-0.4/default)
BuildRequires:  crate(proc-macro2-1) >= 1.0.80
BuildRequires:  crate(proc-macro2-1/default)
BuildRequires:  crate(shlex-1) >= 1
BuildRequires:  crate(shlex-1/default)
BuildRequires:  crate(winapi-util-0.1) >= 0.1.3

Requires:       clang

%description
Automatically generates Rust FFI bindings to C and C++ libraries.
This package contains the bindgen command-line tool from the bindgen-cli crate.

%install
install -D -m 0755 target/release/bindgen %{buildroot}%{_bindir}/bindgen

%check
%{buildroot}%{_bindir}/bindgen --version

%files
%license LICENSE
%doc README.md
%{_bindir}/bindgen

%changelog
%autochangelog

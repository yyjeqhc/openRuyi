# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zz_ci_cargo_valid

Name:           zz-ci-cargo-valid
Version:        0.1.0
Release:        %autorelease
Summary:        CI test package for Cargo.toml validation
License:        MIT
URL:            https://example.com/zz-ci-cargo-valid
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  crate(serde) >= 1.0

%description
CI test package used to verify the check-rust-cargo-toml pre-commit hook
accepts a spec with crate() BuildRequires when a valid Cargo.toml is present.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

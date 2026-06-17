# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zz_ci_cargo_missing

Name:           zz-ci-cargo-missing
Version:        0.1.0
Release:        %autorelease
Summary:        CI test package for missing Cargo.toml check
License:        MIT
URL:            https://example.com/zz-ci-cargo-missing
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  crate(serde) >= 1.0

%description
CI test package used to verify the check-rust-cargo-toml pre-commit hook
rejects a spec with crate() BuildRequires when Cargo.toml is missing.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

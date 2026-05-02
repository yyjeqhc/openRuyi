# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname llguidance

Name:           python-%{srcname}
Version:        1.7.5
Release:        %autorelease
Summary:        Bindings for the Low-level Guidance (llguidance) Rust library for use within Guidance
License:        MIT
URL:            https://github.com/microsoft/llguidance
#!RemoteAsset:  sha256:afaa8f979708cd546c762f06a4fe4748e5ef7f06ed45875dabe7db8f07b73645
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Low-level Guidance (llguidance)

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

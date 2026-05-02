# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname booleanoperations

Name:           python-%{srcname}
Version:        0.10.0
Release:        %autorelease
Summary:        Boolean operations on paths.
License:        MIT
URL:            https://github.com/typemytype/booleanOperations
#!RemoteAsset:  sha256:6d719f560d2a1dd676c812b844ecceb693c96791c76579089ab7d0f5db5cedbe
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l booleanoperations

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
|Build Status| |PyPI| |Python Versions|

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

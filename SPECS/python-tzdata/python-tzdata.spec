# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tzdata

Name:           python-%{srcname}
Version:        2026.2
Release:        %autorelease
Summary:        Provider of IANA time zone data
License:        Apache-2.0
URL:            https://github.com/python/tzdata
#!RemoteAsset:  sha256:9173fde7d80d9018e02a662e168e5a2d04f87c41ea174b139fbef642eda62d10
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
tzdata: Python package providing IANA time zone data

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

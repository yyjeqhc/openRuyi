# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname openstep-plist
%global pypi_name openstep_plist

Name:           python-%{srcname}
Version:        0.5.2
Release:        %autorelease
Summary:        ASCII plist parser written in Cython
License:        MIT
URL:            https://github.com/fonttools/openstep-plist
#!RemoteAsset:  sha256:2a0d70ff7a03cce64a727062b64bb2f5c9af9fd4a636aaa4339b6aaa2cf65195
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A parser for the "old style" OpenStep property list format (also known as ASCII
plist), written in Cython.
Largely based on the CoreFoundation implementation found here:

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

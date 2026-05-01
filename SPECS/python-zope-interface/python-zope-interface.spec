# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname zope-interface
%global pypi_name zope_interface

Name:           python-%{srcname}
Version:        8.4
Release:        %autorelease
Summary:        Interfaces for Python
License:        BSD-2-Clause
URL:            https://github.com/zopefoundation/zope.interface
#!RemoteAsset:  sha256:9dbee7925a23aa6349738892c911019d4095a96cff487b743482073ecbc174a8
Source0:        https://files.pythonhosted.org/packages/source/z/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
.. image:: https://img.shields.io/pypi/v/zope.interface.svg
:target: https://pypi.python.org/pypi/zope.interface/
:alt: Latest Version

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

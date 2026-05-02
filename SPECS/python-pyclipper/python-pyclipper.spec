# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyclipper

Name:           python-%{srcname}
Version:        1.4.0
Release:        %autorelease
Summary:        Cython wrapper for the C++ translation of the Angus Johnson's Clipper library (ver. 6.4.2)
License:        MIT
URL:            https://github.com/fonttools/pyclipper
#!RemoteAsset:  sha256:9882bd889f27da78add4dd6f881d25697efc740bf840274e749988d25496c8e1
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)


%description
.. image:: https://badge.fury.io/py/pyclipper.svg
:target: https://badge.fury.io/py/pyclipper
.. image:: https://github.com/fonttools/pyclipper/workflows/Build%20+%20Deploy/badge.svg
:target: https://github.com/fonttools/pyclipper/actions?query=workflow%3A%22Build+%2B+Deploy%22

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

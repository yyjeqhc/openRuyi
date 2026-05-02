# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ufolib2

Name:           python-%{srcname}
Version:        0.18.1
Release:        %autorelease
Summary:        ufoLib2 is a UFO font processing library.
License:        Apache-2.0
URL:            https://github.com/fonttools/ufoLib2
#!RemoteAsset:  sha256:7de0efcc361c573f2537ee7ceabdb3bc64b19b61304cfa25e828caa7db8ae1a4
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l ufolib2

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
ufoLib2 is meant to be a thin representation of the Unified Font Object (UFO) version 3 data model, intended for programmatic manipulation and fast batch processing of UFOs.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

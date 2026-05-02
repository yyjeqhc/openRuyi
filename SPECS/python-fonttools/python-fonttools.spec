# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname fonttools

Name:           python-%{srcname}
Version:        4.62.1
Release:        %autorelease
Summary:        Tools to manipulate font files
License:        MIT
URL:            http://github.com/fonttools/fonttools
#!RemoteAsset:  sha256:e54c75fd6041f1122476776880f7c3c3295ffa31962dc6ebe2543c00dca58b5d
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l fonttools

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
|CI Build Status| |Coverage Status| |PyPI| |Gitter Chat|

%pyproject_extras_subpkg -n python-%{srcname} lxml
%pyproject_extras_subpkg -n python-%{srcname} ufo
%pyproject_extras_subpkg -n python-%{srcname} unicode

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

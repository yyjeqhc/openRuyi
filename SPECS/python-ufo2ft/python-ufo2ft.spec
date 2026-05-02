# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ufo2ft

Name:           python-%{srcname}
Version:        3.7.2
Release:        %autorelease
Summary:        A bridge between UFOs and FontTools.
License:        MIT
URL:            https://github.com/googlefonts/ufo2ft
#!RemoteAsset:  sha256:a43c582620651f3379a85015fc18634aa66dfbcb9be56d33134bb5bc0ac19266
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description

%pyproject_extras_subpkg -n python-%{srcname} compreffor

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

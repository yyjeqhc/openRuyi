# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname natten

Name:           python-%{srcname}
Version:        0.21.6
Release:        %autorelease
Summary:        Neighborhood Attention Extension
License:        MIT
URL:            https://github.com/SHI-Labs/NATTEN.git
#!RemoteAsset:  sha256:c26871225fa533f8a9433ccd4496e3c4dcf6d0e0da369a2f6b547d4321a25dc1
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Fast Multi-dimensional Sparse Attention**

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

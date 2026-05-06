# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname python_socks

Name:           python-socks
Version:        2.8.1
Release:        %autorelease
Summary:        Core proxy (SOCKS4, SOCKS5, HTTP tunneling) functionality for Python
License:        Apache-2.0
URL:            https://github.com/romis2012/python-socks
#!RemoteAsset:  sha256:698daa9616d46dddaffe65b87db222f2902177a2d2b2c0b9a9361df607ab3687
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-socks
%python_provide python3-socks

%description
The python-socks package provides a core proxy client functionality for Python.
Supports SOCKS4(a), SOCKS5, HTTP (tunneling) proxy and provides sync and async
(asyncio, trio) APIs. It is used internally by aiohttp-socks and
httpx-socks packages.

%pyproject_extras_subpkg -n python3-socks asyncio trio curio

%generate_buildrequires
%pyproject_buildrequires -x asyncio

%check
# skip tests as some deps we don't have yet.

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog

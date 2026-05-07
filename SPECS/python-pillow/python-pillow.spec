# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

BuildArch:      noarch
%global srcname pillow

Name:           python-%{srcname}
Version:        12.2.0
Release:        %autorelease
Summary:        Python image processing library
License:        MIT
URL:            http://python-pillow.github.io/
#!RemoteAsset:  sha256:a830b1a40919539d07806aa58e1b114df53ddd43213d9c8b75847eee6c0182b5
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l PIL

BuildRequires:  gcc
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python image processing library, fork of the Python Imaging Library (PIL).

%generate_buildrequires
%pyproject_buildrequires

%check
# skip the tests,as many deps we don't have yet.

%install -a
install -d %{buildroot}/%{_includedir}/python%{python3_version}/Imaging
install -m 644 src/libImaging/*.h %{buildroot}/%{_includedir}/python%{python3_version}/Imaging

%files -f %{pyproject_files}
%doc README.md CHANGES.rst
%license docs/COPYING
%{_includedir}/python%{python3_version}/Imaging/

%changelog
%autochangelog

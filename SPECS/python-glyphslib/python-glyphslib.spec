# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname glyphslib

Name:           python-%{srcname}
Version:        6.13.1
Release:        %autorelease
Summary:        A bridge from Glyphs source files (.glyphs) to UFOs
License:        Apache-2.0
URL:            https://github.com/googlefonts/glyphsLib
#!RemoteAsset:  sha256:00e3db77ee360bfcf4c2fa108ab0a9c2b8774e5eccd499958220b956bbac7097
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l glyphsLib
BuildOption(check):  -e "glyphsLib.featureWriters.markFeatureWriter"
BuildOption(check):  -e "glyphsLib.filters.cornerComponents"
BuildOption(check):  -e "glyphsLib.filters.eraseOpenCorners"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools-scm[toml])
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(fonttools)
BuildRequires:  python3dist(fonttools[ufo])
BuildRequires:  python3dist(fonttools[unicode])
BuildRequires:  python3dist(openstep-plist)
BuildRequires:  python3dist(ufolib2)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
|CI Build Status| |PyPI Version| |Codecov| |Gitter Chat|

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%{_bindir}/glyphs2ufo
%{_bindir}/ufo2glyphs

%changelog
%autochangelog

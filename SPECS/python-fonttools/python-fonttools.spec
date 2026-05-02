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

BuildOption(install):  -l fontTools
BuildOption(check):  -e "fontTools.misc.symfont"
BuildOption(check):  -e "fontTools.pens.freetypePen"
BuildOption(check):  -e "fontTools.pens.quartzPen"
BuildOption(check):  -e "fontTools.pens.reportLabPen"
BuildOption(check):  -e "fontTools.ttLib.removeOverlaps"
BuildOption(check):  -e "fontTools.varLib.interpolatablePlot"
BuildOption(check):  -e "fontTools.varLib.plot"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description

%pyproject_extras_subpkg -n python-%{srcname} lxml
%pyproject_extras_subpkg -n python-%{srcname} ufo
%pyproject_extras_subpkg -n python-%{srcname} unicode

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%{_bindir}/fonttools
%{_bindir}/pyftmerge
%{_bindir}/pyftsubset
%{_bindir}/ttx
%{_mandir}/man1/ttx.1.gz

%changelog
%autochangelog

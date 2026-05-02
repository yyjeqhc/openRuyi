# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname fontmake

Name:           python-%{srcname}
Version:        3.11.1
Release:        %autorelease
Summary:        Compile fonts from sources (UFO, Glyphs) to binary (OpenType, TrueType).
License:        Apache-2.0
URL:            https://github.com/googlei18n/fontmake
#!RemoteAsset:  sha256:a3b958a2f6d0b978a803a5643f04c27c88c5ed9dc5af999752408aa94053d082
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
`fontmake` compiles fonts from various sources (`.glyphs`, `.ufo`, `designspace`) into binaries (`.otf`, `.ttf`). You can use it to create static instances and variable fonts.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%{_bindir}/fontmake

%changelog
%autochangelog

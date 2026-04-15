# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-rpm-macros
Version:        0.1
Release:        %autorelease
Summary:        perl macros for openRuyi packaging
License:        MIT
# TODO: Update the URL when there is a proper project page
URL:            https://git.openruyi.cn/openRuyi/perl-rpm-macros
#!RemoteAsset:  sha256:5659e8ee57a1669b23a64bf9ae580908f04257d069d1b5c924279682a4feae17
Source0:        perl-rpm-macros.tar.gz
BuildArch:      noarch
BuildSystem:    autotools

%description
This package provides RPM macros for packaging perl software in openRuyi.

%conf
# No configure

# No build needed
%build

# No check needed
%check

%files
%license LICENSE
%{_rpmmacrodir}/macros.buildsystem.perlmaker
%{_rpmmacrodir}/macros.buildsystem.perlbuild

%changelog
%autochangelog

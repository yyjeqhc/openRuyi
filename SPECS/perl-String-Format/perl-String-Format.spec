# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-String-Format
Version:        1.18
Release:        %autorelease
Summary:        Sprintf-like string formatting capabilities with arbitrary format definitions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/String-Format
#!RemoteAsset:  sha256:9e417a8f8d9ea623beea2d13a47c0d5a696fc8602c0509b826cd45f97b76e778
Source0:        http://www.cpan.org/authors/id/S/SR/SREZIC/String-Format-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
String::Format lets you define arbitrary printf-like format sequences to be
expanded. This module would be most useful in configuration files and
reporting tools, where the results of a query need to be formatted in a
particular way. It was inspired by mutt's index_format and related
directives (see <URL:http://www.mutt.org/doc/manual/manual-
6.html#index_format>).

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog

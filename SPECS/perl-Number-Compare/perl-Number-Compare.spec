# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Number-Compare
Version:        0.03
Release:        %autorelease
Summary:        Numeric comparisons
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Number-Compare
#!RemoteAsset:  sha256:83293737e803b43112830443fb5208ec5208a2e6ea512ed54ef8e4dd2b880827
Source0:        http://www.cpan.org/authors/id/R/RC/RCLAMP/Number-Compare-%{version}.tar.gz
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
Number::Compare compiles a simple comparison to an anonymous subroutine,
which you can call with a value to be tested again.

%files -f %{name}.files
%doc Changes

%changelog
%autochangelog

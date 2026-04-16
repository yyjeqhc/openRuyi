# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-ExtUtils-PkgConfig
Version:        1.16
Release:        %autorelease
Summary:        Simplistic interface to pkg-config
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/ExtUtils-PkgConfig
#!RemoteAsset:  sha256:bbeaced995d7d8d10cfc51a3a5a66da41ceb2bc04fedcab50e10e6300e801c6e
Source0:        http://www.cpan.org/authors/id/X/XA/XAOC/ExtUtils-PkgConfig-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
The pkg-config program retrieves information about installed libraries,
usually for the purposes of compiling against and linking to them.

%files -f %{name}.files
%doc Changes perl-ExtUtils-PkgConfig.doap README

%changelog
%autochangelog

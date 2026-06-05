# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Alien-cmake3
Version:        0.10
Release:        %autorelease
Summary:        Find or download or build cmake 3
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Alien-cmake3
#!RemoteAsset:  sha256:c87a09d8687b5c5057b825c56329513d8b1b7741b1ec4fca346465ee0219485f
Source0:        https://www.cpan.org/authors/id/P/PL/PLICEASE/Alien-cmake3-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(Alien::Base) >= 0.92
BuildRequires:  perl(Alien::Build) >= 0.32
BuildRequires:  perl(Alien::Build::MM) >= 0.32
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test2::V0) >= 0.000121
BuildRequires:  perl(Test::Alien) >= 0.92

Requires:       perl(Alien::Base) >= 0.92

%description
This Alien distribution provides an external dependency on the build tool
cmake version 3.x.x. cmake is a popular alternative to autoconf.

%files -f %{name}.files
%doc alienfile author.yml Changes perlcriticrc README

%changelog
%autochangelog

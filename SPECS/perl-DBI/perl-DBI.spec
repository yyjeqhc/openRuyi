Name:           perl-DBI
Version:        1.648
Release:        %autorelease
Summary:        Database independent interface for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/DBI
#!RemoteAsset:  sha256:ef266aad6010ce2eabb7e465ebd73ca3020bc58150f6989bd89c2b8f9bac6a86
Source0:        https://www.cpan.org/authors/id/H/HM/HMBRAND/DBI-%{version}.tgz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Simple) >= 0.90

%description
The DBI is a database access module for the Perl programming language.
It defines a set of methods, variables, and conventions that provide a
consistent database interface, independent of the actual database
being used.

%files -f %{name}.files
%doc ChangeLog Driver.xst README.md

%changelog
%autochangelog

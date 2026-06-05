Name:           perl-Test-Simple
Version:        1.302219
Release:        %autorelease
Summary:        Basic utilities for writing tests
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-Simple
#!RemoteAsset:  sha256:420600911230de768427f6646758d89b6c07977b565e5b40118e5b8440dbb30b
Source0:        https://www.cpan.org/authors/id/E/EX/EXODIST/Test-Simple-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.2
BuildRequires:  perl(B)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util) >= 1.13
BuildRequires:  perl(Storable)
BuildRequires:  perl(Term::Table) >= 0.013
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(utf8)

Requires:       perl(Scalar::Util) >= 1.13
Requires:       perl(Term::Table) >= 0.013

%description
** If you are unfamiliar with testing read Test::Tutorial first! **

%files -f %{name}.files
%doc appveyor.yml Changes examples perltidyrc README README.md

%changelog
%autochangelog

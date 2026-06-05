Name:           perl-Test-Harness
Version:        3.52
Release:        %autorelease
Summary:        Run Perl standard test scripts with statistics
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-Harness
#!RemoteAsset:  sha256:8fe65cfc0261ed3c8a4395f0524286f5719669fe305f9b03b16cf3684d62cd70
Source0:        https://www.cpan.org/authors/id/L/LE/LEONT/Test-Harness-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::Usage) >= 1.12

Requires:       perl(Pod::Usage) >= 1.12

%description
Although, for historical reasons, the Test::Harness distribution takes its
name from this module it now exists only to provide TAP::Harness with an
interface that is somewhat backwards compatible with Test::Harness 2.xx. If
you're writing new code consider using TAP::Harness directly instead.

%files -f %{name}.files
%doc Changes Changes-2.64 MANIFEST.CUMMULATIVE perlcriticrc README

%changelog
%autochangelog

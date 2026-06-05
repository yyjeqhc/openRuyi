Name:           perl-Devel-Caller
Version:        2.07
Release:        %autorelease
Summary:        Meatier versions of caller
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Devel-Caller
#!RemoteAsset:  sha256:b679a2b18034b0b720de82c3708724c364b10a6ca164cbc67cdc3af283f3503f
Source0:        https://www.cpan.org/authors/id/R/RC/RCLAMP/Devel-Caller-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(PadWalker) >= 0.08
BuildRequires:  perl(Test::More)

Requires:       perl(PadWalker) >= 0.08

%description
caller_cv($level)

%files -f %{name}.files
%doc Changes

%changelog
%autochangelog

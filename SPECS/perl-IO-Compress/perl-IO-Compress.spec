Name:           perl-IO-Compress
Version:        2.220
Release:        %autorelease
Summary:        Read/write compressed data in multiple formats
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IO-Compress
#!RemoteAsset:  sha256:9d96ea291f2c54ef367c7396b857d93ba1ac1c4b2f1bce13ed8a3e5f3eebb627
Source0:        https://www.cpan.org/authors/id/P/PM/PMQS/IO-Compress-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Compress::Raw::Bzip2) >= 2.218
BuildRequires:  perl(Compress::Raw::Zlib) >= 2.218
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Time::Local)

Requires:       perl(Compress::Raw::Bzip2) >= 2.218
Requires:       perl(Compress::Raw::Zlib) >= 2.218

%description
This is a stub module. It contains no code.

%files -f %{name}.files
%doc Changes README SECURITY.md

%changelog
%autochangelog

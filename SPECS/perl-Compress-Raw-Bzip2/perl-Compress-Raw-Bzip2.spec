Name:           perl-Compress-Raw-Bzip2
Version:        2.218
Release:        %autorelease
Summary:        Low-Level Interface to bzip2 compression library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Compress-Raw-Bzip2
#!RemoteAsset:  sha256:89153e6a2ebda52349493b074fa4b7549ff1f9053de7613c18a5e05c5b415fa8
Source0:        https://www.cpan.org/authors/id/P/PM/PMQS/Compress-Raw-Bzip2-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
Compress::Raw::Bzip2 provides an interface to the in-memory
compression/uncompression functions from the bzip2 compression library.

%files -f %{name}.files
%doc Changes README SECURITY.md

%changelog
%autochangelog

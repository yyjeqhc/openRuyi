# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-File-TreeCreate
Version:        0.0.1
Release:        %autorelease
Summary:        Recursively create a directory tree
License:        MIT
URL:            https://metacpan.org/dist/File-TreeCreate
#!RemoteAsset:  sha256:57686f10843be81affad185ae4131790ba0c4af36d2104d6fb69126528055267
Source0:        https://www.cpan.org/authors/id/S/SH/SHLOMIF/File-TreeCreate-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlbuild

BuildOption(build):  --installdirs=vendor
BuildOption(install):  --destdir=%{buildroot} --create_packlist=0

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(autodie)
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)

%description
This module was extracted from several near-identical copies used in the
tests of some of my CPAN distributions.

%files -f %{name}.files
%doc Changes README weaver.ini

%changelog
%autochangelog

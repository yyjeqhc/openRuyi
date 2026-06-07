# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-HTML-Tree
Version:        5.07
Release:        %autorelease
Summary:        Build and scan parse-trees of HTML
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/HTML-Tree
#!RemoteAsset:  sha256:f0374db84731c204b86c1d5b90975fef0d30a86bd9def919343e554e31a9dbbf
Source0:        https://www.cpan.org/authors/id/K/KE/KENTNL/HTML-Tree-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlbuild

BuildOption(build):  --installdirs=vendor
BuildOption(install):  --destdir=%{buildroot} --create_packlist=0

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::FormatText)
BuildRequires:  perl(HTML::Parser) >= 3.46
BuildRequires:  perl(HTML::Tagset) >= 3.02
BuildRequires:  perl(integer)
BuildRequires:  perl(LWP::UserAgent) >= 5.815
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)

Requires:       perl(HTML::Parser) >= 3.46
Requires:       perl(HTML::Tagset) >= 3.02
Requires:       perl(LWP::UserAgent) >= 5.815

%description
HTML-Tree is a suite of Perl modules for making parse trees out of HTML
source. It consists of mainly two modules, whose documentation you should
refer to: HTML::TreeBuilder and HTML::Element.

%files -f %{name}.files
%doc Changes README TODO

%changelog
%autochangelog

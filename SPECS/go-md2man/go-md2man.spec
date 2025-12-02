# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-md2man
%define go_import_path  github.com/cpuguy83/go-md2man/v2

Name:           go-md2man
Version:        2.0.7
Release:        %autorelease
Summary:        Converts markdown into roff (man pages).
License:        MIT
URL:            https://github.com/cpuguy83/go-md2man
#!RemoteAsset
Source0:        https://github.com/cpuguy83/go-md2man/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go-github-russross-blackfriday-v2

%description
go-md2man Converts markdown into roff (man pages).

%files
%license LICENSE*
%doc README*
%{_bindir}/%{_name}

%changelog
%{?autochangelog}

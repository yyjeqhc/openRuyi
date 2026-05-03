%global srcname nltk

Name:           python-%{srcname}
Version:        3.9.4
Release:        %autorelease
Summary:        Natural Language Toolkit
License:        Apache-2.0
URL:            https://github.com/nltk/nltk
#!RemoteAsset:  sha256:ed03bc098a40481310320808b2db712d95d13ca65b27372f8a403949c8b523d0
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The Natural Language Toolkit (NLTK) is a Python package for
natural language processing. NLTK requires Python 3.10, 3.11, 3.12, 3.13, or 3.14.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

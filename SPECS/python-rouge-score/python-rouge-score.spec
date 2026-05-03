%global srcname rouge-score
%global pypi_name rouge_score

Name:           python-%{srcname}
Version:        0.1.2
Release:        %autorelease
Summary:        Pure python implementation of ROUGE-1.5.5.
License:        Apache-2.0
URL:            https://github.com/google-research/google-research/tree/master/rouge
#!RemoteAsset:  sha256:c7d4da2683e68c9abf0135ef915d63a46643666f848e558a1b9f7ead17ff0f04
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python ROUGE Implementation

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

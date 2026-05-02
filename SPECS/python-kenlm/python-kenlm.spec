%global srcname kenlm

Name:           python-%{srcname}
Version:        0.3.0
Release:        %autorelease
Summary:        Python package kenlm
License:        LicenseRef-Unknown-Please-Check-Manual
URL:            https://pypi.org/project/kenlm/
#!RemoteAsset:  sha256:c4628bb9fb63c8a6f9240035b8b037385cfc404cb72e933cf48878291edac1e8
Source0:        https://files.pythonhosted.org/packages/source/k/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python package kenlm

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

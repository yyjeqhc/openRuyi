%global srcname absl-py
%global pypi_name absl_py

Name:           python-%{srcname}
Version:        2.4.0
Release:        %autorelease
Summary:        Abseil Python Common Libraries, see https://github.com/abseil/abseil-py.
License:        Apache-2.0
URL:            https://github.com/abseil/abseil-py
#!RemoteAsset:  sha256:8c6af82722b35cf71e0f4d1d47dcaebfff286e27110a99fc359349b247dfb5d4
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l absl_py

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Abseil Python Common Libraries

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

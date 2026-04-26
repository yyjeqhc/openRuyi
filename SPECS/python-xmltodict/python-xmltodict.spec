%global srcname xmltodict

Name:           python-%{srcname}
Version:        1.0.4
Release:        %autorelease
Summary:        Makes working with XML feel like you are working with JSON
License:        MIT
URL:            https://github.com/martinblech/xmltodict
#!RemoteAsset:  sha256:6d94c9f834dd9e44514162799d344d815a3a4faec913717a9ecbfa5be1bb8e61
Source0:        https://files.pythonhosted.org/packages/source/x/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
`xmltodict` is a Python module that makes working with XML feel like you are working with JSON, as in this "spec":

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

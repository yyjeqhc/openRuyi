%global srcname zipp

Name:           python-%{srcname}
Version:        3.23.1
Release:        %autorelease
Summary:        Backport of pathlib-compatible object wrapper for zip files
License:        MIT
URL:            https://github.com/jaraco/zipp
#!RemoteAsset:  sha256:32120e378d32cd9714ad503c1d024619063ec28aad2248dc6672ad13edfa5110
Source0:        https://files.pythonhosted.org/packages/source/z/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(coherent-licensed)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools-scm[toml])

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
.. image:: https://img.shields.io/pypi/v/zipp.svg
:target: https://pypi.org/project/zipp

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

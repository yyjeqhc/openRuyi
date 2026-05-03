%global srcname nvidia-ml-py
%global pypi_name nvidia_ml_py

Name:           python-%{srcname}
Version:        13.595.45
Release:        %autorelease
Summary:        Python Bindings for the NVIDIA Management Library
License:        BSD-3-Clause
URL:            https://forums.developer.nvidia.com
#!RemoteAsset:  sha256:c9f34897fe0441ff35bc8f35baf80f830a20b0f4e6ce71e0a325bc0e66acf079
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l pynvml -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python bindings to the NVIDIA Management Library

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%{_prefix}/lib/python3.13/site-packages/__pycache__/example.cpython-313.pyc
%{_prefix}/lib/python3.13/site-packages/example.py

%changelog
%autochangelog

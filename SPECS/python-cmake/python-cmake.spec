%global srcname cmake

Name:           python-%{srcname}
Version:        4.3.2
Release:        %autorelease
Summary:        CMake is an open-source, cross-platform family of tools designed to build, test and package software
License:        Apache-2.0
URL:            https://github.com/scikit-build/cmake-python-distributions
#!RemoteAsset:  sha256:5f47f5f00910c474662d09a0516413c6e9750bde73cdc52dea3988102a274e06
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
CMake Python Distributions

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

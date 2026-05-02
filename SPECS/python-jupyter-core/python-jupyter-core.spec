%global srcname jupyter-core
%global pypi_name jupyter_core

Name:           python-%{srcname}
Version:        5.9.1
Release:        %autorelease
Summary:        Jupyter core package. A base package on which Jupyter projects rely.
License:        BSD-3-Clause
URL:            https://github.com/jupyter/jupyter_core
#!RemoteAsset:  sha256:4d09aaff303b9566c3ce657f580bd089ff5c91f5f89cf7d8846c3cdf465b5508
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Jupyter core package. A base package on which Jupyter projects rely.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

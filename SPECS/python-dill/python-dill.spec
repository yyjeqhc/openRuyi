%global srcname dill

Name:           python-%{srcname}
Version:        0.4.1
Release:        %autorelease
Summary:        serialize all of Python
License:        BSD-3-Clause
URL:            https://github.com/uqfoundation/dill
#!RemoteAsset:  sha256:423092df4182177d4d8ba8290c8a5b640c66ab35ec7da59ccfa00f6fa3eea5fa
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

# Exclude upstream test modules from BuildSystem import checks.
BuildOption(check):  -e "dill.tests.*"
%description
dill: serialize all of Python

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

# Include upstream helper scripts installed by the wheel.
%{_bindir}/get_gprof
%{_bindir}/get_objgraph
%{_bindir}/undill
%changelog
%autochangelog

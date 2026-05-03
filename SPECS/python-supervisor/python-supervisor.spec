%global srcname supervisor

Name:           python-%{srcname}
Version:        4.3.0
Release:        %autorelease
Summary:        A system for controlling process state under UNIX
License:        BSD-3-Clause
URL:            https://github.com/Supervisor/supervisor
#!RemoteAsset:  sha256:4a2bf149adf42997e1bb44b70c43b613275ec9852c3edacca86a9166b27e945e
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Supervisor is a client/server system that allows its users to
control a number of processes on UNIX-like operating systems.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

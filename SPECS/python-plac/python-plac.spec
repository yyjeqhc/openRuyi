%global srcname plac

Name:           python-%{srcname}
Version:        1.4.5
Release:        %autorelease
Summary:        The smartest command line arguments parser in the world
License:        BSD-3-Clause
URL:            https://github.com/ialbert/plac
#!RemoteAsset:  sha256:5f05bf85235c017fcd76c73c8101d4ff8e96beb3dc58b9a37de49cac7de82d14
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Plac: parsing the command line the easy way

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%{_bindir}/plac_runner.py
%{_prefix}/lib/python3.13/site-packages/__pycache__/plac_core.cpython-313.pyc
%{_prefix}/lib/python3.13/site-packages/__pycache__/plac_ext.cpython-313.pyc
%{_prefix}/lib/python3.13/site-packages/__pycache__/plac_tk.cpython-313.pyc
%{_prefix}/lib/python3.13/site-packages/plac_core.py
%{_prefix}/lib/python3.13/site-packages/plac_ext.py
%{_prefix}/lib/python3.13/site-packages/plac_tk.py

%changelog
%autochangelog

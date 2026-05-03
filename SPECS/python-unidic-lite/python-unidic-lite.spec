%global srcname unidic-lite

Name:           python-%{srcname}
Version:        1.0.8
Release:        %autorelease
Summary:        A small version of UniDic packaged for Python
License:        MIT
URL:            https://github.com/polm/unidic-lite
#!RemoteAsset:  sha256:db9d4572d9fdd4d00a97949d4b0741ec480ee05a7e7e2e32f547500dae27b245
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l unidic_lite

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This is a version of unidic-py that is
designed to be installable with pip alone, not requiring any extra downloads.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

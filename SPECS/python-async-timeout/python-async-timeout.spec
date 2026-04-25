%global srcname async-timeout
%global pypi_name async_timeout

Name:           python-%{srcname}
Version:        5.0.1
Release:        %autorelease
Summary:        Timeout context manager for asyncio programs
License:        Apache-2.0
URL:            https://github.com/aio-libs/async-timeout
#!RemoteAsset:  sha256:d9321a7a3d5a6a5e187e824d2fa0793ce379a202935782d555d6e9d2735677d3
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
async-timeout
.. image:: https://travis-ci.com/aio-libs/async-timeout.svg?branch=master
:target: https://travis-ci.com/aio-libs/async-timeout
..

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

%global srcname requests-oauthlib

Name:           python-%{srcname}
Version:        2.0.0
Release:        %autorelease
Summary:        OAuthlib authentication support for Requests.
License:        ISC
URL:            https://github.com/requests/requests-oauthlib
#!RemoteAsset:  sha256:b3dffaebd884d8cd778494369603a9e7b58d29111bf6b41bdc2dcd87203af4e9
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l requests_oauthlib

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(oauthlib)
BuildRequires:  python3dist(requests)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Requests-OAuthlib |build-status| |coverage-status| |docs|

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

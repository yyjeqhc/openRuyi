%global srcname authlib

Name:           python-%{srcname}
Version:        1.7.0
Release:        %autorelease
Summary:        The ultimate Python library in building OAuth and OpenID Connect servers and clients.
License:        BSD-3-Clause
URL:            https://github.com/authlib/authlib
#!RemoteAsset:  sha256:b3e326c9aa9cc3ea95fe7d89fd880722d3608da4d00e8a27e061e64b48d801d5
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The ultimate Python library in building OAuth and OpenID Connect servers.
JWS, JWK, JWA, JWT are included.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

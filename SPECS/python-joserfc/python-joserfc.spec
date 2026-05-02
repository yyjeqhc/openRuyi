%global srcname joserfc

Name:           python-%{srcname}
Version:        1.6.4
Release:        %autorelease
Summary:        The ultimate Python library for JOSE RFCs, including JWS, JWE, JWK, JWA, JWT
License:        BSD-3-Clause
URL:            https://github.com/authlib/joserfc
#!RemoteAsset:  sha256:34ce5f499bfcc5e9ad4cc75077f9278ab3227b71da9aaf28f9ab705f8a560d3c
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
``joserfc`` is a Python library that provides a comprehensive implementation of several
essential JSON Object Signing and Encryption (JOSE) standards.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

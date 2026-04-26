%global srcname blis

Name:           python-%{srcname}
Version:        1.3.3
Release:        %autorelease
Summary:        The Blis BLAS-like linear algebra library, as a self-contained C-extension.
License:        BSD-3-Clause
URL:            https://github.com/explosion/cython-blis
#!RemoteAsset:  sha256:034d4560ff3cc43e8aa37e188451b0440e3261d989bb8a42ceee865607715ecd
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Cython BLIS: Fast BLAS-like operations from Python and Cython, without the tears

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

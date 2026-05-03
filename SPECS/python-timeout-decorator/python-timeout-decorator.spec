%global srcname timeout-decorator

Name:           python-%{srcname}
Version:        0.5.0
Release:        %autorelease
Summary:        Timeout decorator
License:        MIT
URL:            https://github.com/pnpnpn/timeout-decorator
#!RemoteAsset:  sha256:6a2f2f58db1c5b24a2cc79de6345760377ad8bdc13813f5265f6c3e63d16b3d7
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l timeout-decorator

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
|Build Status| |Pypi Status| |Coveralls Status|

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

%global srcname types-dataclasses

Name:           python-%{srcname}
Version:        0.6.6
Release:        %autorelease
Summary:        Typing stubs for dataclasses
License:        Apache-2.0
URL:            https://github.com/python/typeshed
#!RemoteAsset:  sha256:4b5a2fcf8e568d5a1974cd69010e320e1af8251177ec968de7b9bb49aa49f7b9
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Typing stubs for dataclasses

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

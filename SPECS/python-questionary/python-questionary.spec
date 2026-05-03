%global srcname questionary

Name:           python-%{srcname}
Version:        2.1.1
Release:        %autorelease
Summary:        Python library to build pretty command line user prompts ⭐️
License:        MIT
URL:            https://github.com/tmbo/questionary
#!RemoteAsset:  sha256:3d7e980292bb0107abaa79c68dd3eee3c561b83a0f89ae482860b181c8bd412d
Source0:        https://files.pythonhosted.org/packages/source/q/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
✨ Questionary is a Python library for effortlessly building pretty command line interfaces ✨

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

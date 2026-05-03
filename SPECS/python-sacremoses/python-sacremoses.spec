%global srcname sacremoses

Name:           python-%{srcname}
Version:        0.1.1
Release:        %autorelease
Summary:        SacreMoses
License:        MIT
URL:            https://github.com/hplt-project/sacremoses
#!RemoteAsset:  sha256:b6fd5d3a766b02154ed80b962ddca91e1fd25629c0978c7efba21ebccf663934
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  -e "sacremoses.sent_tokenize"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pip install -U sacremoses

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%{_bindir}/sacremoses

%changelog
%autochangelog

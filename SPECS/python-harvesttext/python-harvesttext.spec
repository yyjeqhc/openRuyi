%global srcname harvesttext

Name:           python-%{srcname}
Version:        0.8.2.1
Release:        %autorelease
Summary:        UNKNOWN
License:        MIT
URL:            https://github.com/blmoistawinde/HarvestText
#!RemoteAsset:  sha256:621bcfa334f17d5c5daf3408595506a7c224e7246c38d6742b5e927e6e9c846f
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
HarvestText : A Toolkit for Text Mining and Preprocessing

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

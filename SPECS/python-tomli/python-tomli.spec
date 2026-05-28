%global srcname tomli

Name:           python-%{srcname}
Version:        2.4.1
Release:        %autorelease
Summary:        A lil' TOML parser
License:        MIT
URL:            https://github.com/hukkin/tomli
#!RemoteAsset:  sha256:7c7e1a961a0b2f2472c1ac5b69affa0ae1132c39adcb67aba98568702b9cc23f
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Table of Contents** *generated with mdformat-toc*

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

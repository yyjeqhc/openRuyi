%global srcname accelerate

Name:           python-%{srcname}
Version:        1.13.0
Release:        %autorelease
Summary:        Accelerate
License:        Apache-2.0
URL:            https://github.com/huggingface/accelerate
#!RemoteAsset:  sha256:d631b4e0f5b3de4aff2d7e9e6857d164810dfc3237d54d017f075122d057b236
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Copyright 2021 The HuggingFace Team. All rights reserved.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

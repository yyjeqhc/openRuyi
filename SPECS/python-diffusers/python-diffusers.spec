%global srcname diffusers

Name:           python-%{srcname}
Version:        0.38.0
Release:        %autorelease
Summary:        State-of-the-art diffusion in PyTorch and JAX.
License:        Apache-2.0
URL:            https://github.com/huggingface/diffusers
#!RemoteAsset:  sha256:1e094ec5c16f18c42fb89d37f07a94cf9aab3ebbe527ab059c609597b8857626
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Copyright 2022 - The HuggingFace Team. All rights reserved.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

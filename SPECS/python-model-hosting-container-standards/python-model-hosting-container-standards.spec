%global srcname model-hosting-container-standards
%global pypi_name model_hosting_container_standards

Name:           python-%{srcname}
Version:        0.1.14
Release:        %autorelease
Summary:        Python toolkit for standardized model hosting container implementations with Amazon SageMaker integration
License:        Apache-2.0
URL:            https://pypi.org/project/model-hosting-container-standards/
#!RemoteAsset:  sha256:b6cf4c46d88ce6acd6e543a578bb88ffd55d1179a7c09c22e61ae1d8a567c564
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Model Hosting Container Standards - Python

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

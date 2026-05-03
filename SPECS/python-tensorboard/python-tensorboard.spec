%global srcname tensorboard

Name:           python-%{srcname}
Version:        2.20.0
Release:        %autorelease
Summary:        
License:        LicenseRef-Unknown-Please-Check-Manual
URL:            
#!RemoteAsset:  sha256:
Source0:        
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
TODO: PyPI package metadata/source archive unavailable, please fill in summary, license, URL and Source0 manually.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

# Manual check note:
# package: tensorboard
# reason: no supported source distribution (.tar.gz/.tgz) found on PyPI for version 2.20.0

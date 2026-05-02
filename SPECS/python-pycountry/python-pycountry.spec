%global srcname pycountry

Name:           python-%{srcname}
Version:        26.2.16
Release:        %autorelease
Summary:        ISO country, subdivision, language, currency and script definitions and their translations
License:        LicenseRef-Unknown-Please-Check-Manual
URL:            https://github.com/pycountry/pycountry
#!RemoteAsset:  sha256:5b6027d453fcd6060112b951dd010f01f168b51b4bf8a1f1fc8c95c8d94a0801
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pycountry provides the ISO databases for the standards:

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

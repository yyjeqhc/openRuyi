%global srcname stabilize

Name:           python-%{srcname}
Version:        0
Release:        %autorelease
Summary:        Bootstrap package for python3dist(stabilize) >= 0.9
License:        LicenseRef-Unknown
URL:            https://pypi.org/
BuildSystem:    pyproject

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

%description
Bootstrap package placeholder for dependency python3dist(stabilize) >= 0.9.

%files

%changelog
%{?autochangelog}

%global srcname pypinyin

Name:           python-%{srcname}
Version:        0.55.0
Release:        %autorelease
Summary:        汉字拼音转换模块/工具.
License:        MIT
URL:            https://github.com/mozillazg/python-pinyin
#!RemoteAsset:  sha256:b5711b3a0c6f76e67408ec6b2e3c4987a3a806b7c528076e7c7b86fcf0eaa66b
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
汉字拼音转换工具（Python 版）

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

%global srcname zhconv

Name:           python-%{srcname}
Version:        1.4.3
Release:        %autorelease
Summary:        A simple implementation of Simplified-Traditional Chinese conversion.
License:        GPL-2.0-or-later
URL:            https://github.com/gumblex/zhconv
#!RemoteAsset:  sha256:ad42d9057ca0605f8e41d62b67ca797f879f58193ee6840562c51459b2698c45
Source0:        https://files.pythonhosted.org/packages/source/z/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
zhconv** 提供基于 MediaWiki 词汇表的最大正向匹配简繁转换。Python 2, 3 通用。支持以下地区词转换：

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog

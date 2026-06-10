# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pydantic-core
%global pypi_name pydantic_core

Name:           python-%{srcname}
Version:        2.41.5
Release:        %autorelease
Summary:        Core functionality for Pydantic validation and serialization
License:        MIT
URL:            https://github.com/pydantic/pydantic-core
#!RemoteAsset:  sha256:08daa51ea16ad373ffd5e7606252cc32f07bc72b28284b6bc9c6df804816476e
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(puccinialin)
BuildRequires:  python3dist(maturin)
BuildRequires:  crate(ahash-0.8)
BuildRequires:  crate(ahash-0.8/default)
BuildRequires:  crate(base64-0.22)
BuildRequires:  crate(base64-0.22/default)
BuildRequires:  crate(enum-dispatch-0.3)
BuildRequires:  crate(enum-dispatch-0.3/default)
BuildRequires:  crate(hex-0.4) >= 0.4.3
BuildRequires:  crate(hex-0.4/default)
BuildRequires:  crate(idna-1) >= 1.1.0
BuildRequires:  crate(idna-1/default)
BuildRequires:  crate(jiter-0.11) >= 0.11.1
BuildRequires:  crate(jiter-0.11/default)
BuildRequires:  crate(jiter-0.11/python)
BuildRequires:  crate(num-bigint-0.4)
BuildRequires:  crate(num-bigint-0.4/default)
BuildRequires:  crate(num-traits-0.2) >= 0.2.19
BuildRequires:  crate(num-traits-0.2/default)
BuildRequires:  crate(percent-encoding-2) >= 2.3.2
BuildRequires:  crate(percent-encoding-2/default)
BuildRequires:  crate(pyo3-0.26)
BuildRequires:  crate(pyo3-0.26/default)
BuildRequires:  crate(pyo3-0.26/generate-import-lib)
BuildRequires:  crate(pyo3-0.26/num-bigint)
BuildRequires:  crate(pyo3-0.26/py-clone)
BuildRequires:  crate(pyo3-build-config-0.26)
BuildRequires:  crate(pyo3-build-config-0.26/default)
BuildRequires:  crate(regex-1) >= 1.12.2
BuildRequires:  crate(regex-1/default)
BuildRequires:  crate(serde-1) >= 1.0.219
BuildRequires:  crate(serde-1/default)
BuildRequires:  crate(serde-1/derive)
BuildRequires:  crate(serde-json-1) >= 1.0.145
BuildRequires:  crate(serde-json-1/arbitrary-precision)
BuildRequires:  crate(serde-json-1/default)
BuildRequires:  crate(smallvec-1)
BuildRequires:  crate(smallvec-1/default)
BuildRequires:  crate(speedate-0.17) >= 0.17.0
BuildRequires:  crate(speedate-0.17/default)
BuildRequires:  crate(strum-0.27)
BuildRequires:  crate(strum-0.27/default)
BuildRequires:  crate(strum-0.27/derive)
BuildRequires:  crate(strum-macros-0.27)
BuildRequires:  crate(strum-macros-0.27/default)
BuildRequires:  crate(url-2) >= 2.5.4
BuildRequires:  crate(url-2/default)
BuildRequires:  crate(uuid-1) >= 1.18.1
BuildRequires:  crate(uuid-1/default)
BuildRequires:  crate(version-check-0.9)
BuildRequires:  crate(version-check-0.9/default)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package provides the core functionality for
pydantic validation and serialization. Pydantic-core is
currently around 17x faster than pydantic V1.

%prep -a
rm -f Cargo.lock
mkdir -p .cargo ~/.cargo
cat > .cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "system-registry"

[source.system-registry]
directory = "/usr/share/cargo/registry"
EOF
cp .cargo/config.toml ~/.cargo/config.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog

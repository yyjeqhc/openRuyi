%global crate_name heed-types
%global full_version 0.21.0
%global pkgname heed-types-0.21

Name:           rust-heed-types-0.21
Version:        0.21.0
Release:        %autorelease
Summary:        Rust crate "heed-types"
License:        MIT
URL:            https://github.com/Kerollmops/heed
#!RemoteAsset:  sha256:13c255bdf46e07fb840d120a36dcc81f385140d7191c76a7391672675c01a55d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1/default) >= 1.5.0
Requires:       crate(heed-traits-0.20/default) >= 0.20.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "heed-types"

%package     -n %{name}+arbitrary-precision
Summary:        Types used with the fully typed LMDB wrapper, heed - feature "arbitrary_precision"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/arbitrary-precision) >= 1.0.133
Provides:       crate(%{pkgname}/arbitrary-precision) = %{version}

%description -n %{name}+arbitrary-precision
This metapackage enables feature "arbitrary_precision" for the Rust heed-types crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bincode
Summary:        Types used with the fully typed LMDB wrapper, heed - feature "bincode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bincode-1/default) >= 1.3.3
Provides:       crate(%{pkgname}/bincode) = %{version}

%description -n %{name}+bincode
This metapackage enables feature "bincode" for the Rust heed-types crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Types used with the fully typed LMDB wrapper, heed - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde-bincode) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust heed-types crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+preserve-order
Summary:        Types used with the fully typed LMDB wrapper, heed - feature "preserve_order"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/preserve-order) >= 1.0.133
Provides:       crate(%{pkgname}/preserve-order) = %{version}

%description -n %{name}+preserve-order
This metapackage enables feature "preserve_order" for the Rust heed-types crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+raw-value
Summary:        Types used with the fully typed LMDB wrapper, heed - feature "raw_value"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/raw-value) >= 1.0.133
Provides:       crate(%{pkgname}/raw-value) = %{version}

%description -n %{name}+raw-value
This metapackage enables feature "raw_value" for the Rust heed-types crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rmp-serde
Summary:        Types used with the fully typed LMDB wrapper, heed - feature "rmp-serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rmp-serde-1/default) >= 1.3.0
Provides:       crate(%{pkgname}/rmp-serde) = %{version}

%description -n %{name}+rmp-serde
This metapackage enables feature "rmp-serde" for the Rust heed-types crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Types used with the fully typed LMDB wrapper, heed - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.215
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust heed-types crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-bincode
Summary:        Types used with the fully typed LMDB wrapper, heed - feature "serde-bincode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bincode) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serde-bincode) = %{version}

%description -n %{name}+serde-bincode
This metapackage enables feature "serde-bincode" for the Rust heed-types crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-rmp
Summary:        Types used with the fully typed LMDB wrapper, heed - feature "serde-rmp"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rmp-serde) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serde-rmp) = %{version}

%description -n %{name}+serde-rmp
This metapackage enables feature "serde-rmp" for the Rust heed-types crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Types used with the fully typed LMDB wrapper, heed - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.133
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust heed-types crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unbounded-depth
Summary:        Types used with the fully typed LMDB wrapper, heed - feature "unbounded_depth"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/unbounded-depth) >= 1.0.133
Provides:       crate(%{pkgname}/unbounded-depth) = %{version}

%description -n %{name}+unbounded-depth
This metapackage enables feature "unbounded_depth" for the Rust heed-types crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

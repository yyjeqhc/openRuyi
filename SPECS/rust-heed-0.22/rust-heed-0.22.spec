%global crate_name heed
%global full_version 0.22.0
%global pkgname heed-0.22

Name:           rust-heed-0.22
Version:        0.22.0
Release:        %autorelease
Summary:        Rust crate "heed"
License:        MIT
URL:            https://github.com/Kerollmops/heed
#!RemoteAsset:  sha256:6a56c94661ddfb51aa9cdfbf102cfcc340aa69267f95ebccc4af08d7c530d393
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.9.0
Requires:       crate(bitflags-2/serde) >= 2.9.0
Requires:       crate(byteorder-1) >= 1.5.0
Requires:       crate(heed-traits-0.20/default) >= 0.20.0
Requires:       crate(heed-types-0.21) >= 0.21.0
Requires:       crate(libc-0.2/default) >= 0.2.170
Requires:       crate(lmdb-master-sys-0.2/default) >= 0.2.5
Requires:       crate(once-cell-1/default) >= 1.20.3
Requires:       crate(page-size-0.6/default) >= 0.6.0
Requires:       crate(synchronoise-1/default) >= 1.0.1
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "heed"

%package     -n %{name}+arbitrary-precision
Summary:        Fully typed LMDB (mdb.master) wrapper with minimum overhead - feature "arbitrary_precision"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(heed-types-0.21/arbitrary-precision) >= 0.21.0
Provides:       crate(%{pkgname}/arbitrary-precision) = %{version}

%description -n %{name}+arbitrary-precision
This metapackage enables feature "arbitrary_precision" for the Rust heed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Fully typed LMDB (mdb.master) wrapper with minimum overhead - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-bincode) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust heed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+longer-keys
Summary:        Fully typed LMDB (mdb.master) wrapper with minimum overhead - feature "longer-keys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lmdb-master-sys-0.2/longer-keys) >= 0.2.5
Provides:       crate(%{pkgname}/longer-keys) = %{version}

%description -n %{name}+longer-keys
This metapackage enables feature "longer-keys" for the Rust heed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mdb-idl-logn-10
Summary:        Fully typed LMDB (mdb.master) wrapper with minimum overhead - feature "mdb_idl_logn_10"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lmdb-master-sys-0.2/mdb-idl-logn-10) >= 0.2.5
Provides:       crate(%{pkgname}/mdb-idl-logn-10) = %{version}

%description -n %{name}+mdb-idl-logn-10
This metapackage enables feature "mdb_idl_logn_10" for the Rust heed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mdb-idl-logn-11
Summary:        Fully typed LMDB (mdb.master) wrapper with minimum overhead - feature "mdb_idl_logn_11"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lmdb-master-sys-0.2/mdb-idl-logn-11) >= 0.2.5
Provides:       crate(%{pkgname}/mdb-idl-logn-11) = %{version}

%description -n %{name}+mdb-idl-logn-11
This metapackage enables feature "mdb_idl_logn_11" for the Rust heed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mdb-idl-logn-12
Summary:        Fully typed LMDB (mdb.master) wrapper with minimum overhead - feature "mdb_idl_logn_12"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lmdb-master-sys-0.2/mdb-idl-logn-12) >= 0.2.5
Provides:       crate(%{pkgname}/mdb-idl-logn-12) = %{version}

%description -n %{name}+mdb-idl-logn-12
This metapackage enables feature "mdb_idl_logn_12" for the Rust heed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mdb-idl-logn-13
Summary:        Fully typed LMDB (mdb.master) wrapper with minimum overhead - feature "mdb_idl_logn_13"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lmdb-master-sys-0.2/mdb-idl-logn-13) >= 0.2.5
Provides:       crate(%{pkgname}/mdb-idl-logn-13) = %{version}

%description -n %{name}+mdb-idl-logn-13
This metapackage enables feature "mdb_idl_logn_13" for the Rust heed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mdb-idl-logn-14
Summary:        Fully typed LMDB (mdb.master) wrapper with minimum overhead - feature "mdb_idl_logn_14"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lmdb-master-sys-0.2/mdb-idl-logn-14) >= 0.2.5
Provides:       crate(%{pkgname}/mdb-idl-logn-14) = %{version}

%description -n %{name}+mdb-idl-logn-14
This metapackage enables feature "mdb_idl_logn_14" for the Rust heed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mdb-idl-logn-15
Summary:        Fully typed LMDB (mdb.master) wrapper with minimum overhead - feature "mdb_idl_logn_15"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lmdb-master-sys-0.2/mdb-idl-logn-15) >= 0.2.5
Provides:       crate(%{pkgname}/mdb-idl-logn-15) = %{version}

%description -n %{name}+mdb-idl-logn-15
This metapackage enables feature "mdb_idl_logn_15" for the Rust heed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mdb-idl-logn-16
Summary:        Fully typed LMDB (mdb.master) wrapper with minimum overhead - feature "mdb_idl_logn_16"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lmdb-master-sys-0.2/mdb-idl-logn-16) >= 0.2.5
Provides:       crate(%{pkgname}/mdb-idl-logn-16) = %{version}

%description -n %{name}+mdb-idl-logn-16
This metapackage enables feature "mdb_idl_logn_16" for the Rust heed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mdb-idl-logn-8
Summary:        Fully typed LMDB (mdb.master) wrapper with minimum overhead - feature "mdb_idl_logn_8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lmdb-master-sys-0.2/mdb-idl-logn-8) >= 0.2.5
Provides:       crate(%{pkgname}/mdb-idl-logn-8) = %{version}

%description -n %{name}+mdb-idl-logn-8
This metapackage enables feature "mdb_idl_logn_8" for the Rust heed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mdb-idl-logn-9
Summary:        Fully typed LMDB (mdb.master) wrapper with minimum overhead - feature "mdb_idl_logn_9"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lmdb-master-sys-0.2/mdb-idl-logn-9) >= 0.2.5
Provides:       crate(%{pkgname}/mdb-idl-logn-9) = %{version}

%description -n %{name}+mdb-idl-logn-9
This metapackage enables feature "mdb_idl_logn_9" for the Rust heed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+posix-sem
Summary:        Fully typed LMDB (mdb.master) wrapper with minimum overhead - feature "posix-sem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lmdb-master-sys-0.2/posix-sem) >= 0.2.5
Provides:       crate(%{pkgname}/posix-sem) = %{version}

%description -n %{name}+posix-sem
This metapackage enables feature "posix-sem" for the Rust heed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+preserve-order
Summary:        Fully typed LMDB (mdb.master) wrapper with minimum overhead - feature "preserve_order"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(heed-types-0.21/preserve-order) >= 0.21.0
Provides:       crate(%{pkgname}/preserve-order) = %{version}

%description -n %{name}+preserve-order
This metapackage enables feature "preserve_order" for the Rust heed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+raw-value
Summary:        Fully typed LMDB (mdb.master) wrapper with minimum overhead - feature "raw_value"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(heed-types-0.21/raw-value) >= 0.21.0
Provides:       crate(%{pkgname}/raw-value) = %{version}

%description -n %{name}+raw-value
This metapackage enables feature "raw_value" for the Rust heed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Fully typed LMDB (mdb.master) wrapper with minimum overhead - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/serde) >= 2.9.0
Requires:       crate(serde-1/default) >= 1.0.218
Requires:       crate(serde-1/derive) >= 1.0.218
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust heed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-bincode
Summary:        Fully typed LMDB (mdb.master) wrapper with minimum overhead - feature "serde-bincode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(heed-types-0.21/serde-bincode) >= 0.21.0
Provides:       crate(%{pkgname}/serde-bincode) = %{version}

%description -n %{name}+serde-bincode
This metapackage enables feature "serde-bincode" for the Rust heed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Fully typed LMDB (mdb.master) wrapper with minimum overhead - feature "serde-json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(heed-types-0.21/serde-json) >= 0.21.0
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde-json" for the Rust heed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-rmp
Summary:        Fully typed LMDB (mdb.master) wrapper with minimum overhead - feature "serde-rmp"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(heed-types-0.21/serde-rmp) >= 0.21.0
Provides:       crate(%{pkgname}/serde-rmp) = %{version}

%description -n %{name}+serde-rmp
This metapackage enables feature "serde-rmp" for the Rust heed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unbounded-depth
Summary:        Fully typed LMDB (mdb.master) wrapper with minimum overhead - feature "unbounded_depth"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(heed-types-0.21/unbounded-depth) >= 0.21.0
Provides:       crate(%{pkgname}/unbounded-depth) = %{version}

%description -n %{name}+unbounded-depth
This metapackage enables feature "unbounded_depth" for the Rust heed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-valgrind
Summary:        Fully typed LMDB (mdb.master) wrapper with minimum overhead - feature "use-valgrind"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lmdb-master-sys-0.2/use-valgrind) >= 0.2.5
Provides:       crate(%{pkgname}/use-valgrind) = %{version}

%description -n %{name}+use-valgrind
This metapackage enables feature "use-valgrind" for the Rust heed crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

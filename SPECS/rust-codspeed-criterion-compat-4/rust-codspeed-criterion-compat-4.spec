%global crate_name codspeed-criterion-compat
%global full_version 4.4.1
%global pkgname codspeed-criterion-compat-4

Name:           rust-codspeed-criterion-compat-4
Version:        4.4.1
Release:        %autorelease
Summary:        Rust crate "codspeed-criterion-compat"
License:        MIT OR Apache-2.0
URL:            https://codspeed.io
#!RemoteAsset:  sha256:2e65444156eb73ad7f57618188f8d4a281726d133ef55b96d1dcff89528609ab
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(clap-4/std) >= 4.0.0
Requires:       crate(codspeed-4/default) >= 4.4.1
Requires:       crate(codspeed-criterion-compat-walltime-4) >= 4.4.1
Requires:       crate(colored-2/default) >= 2.1.0
Requires:       crate(regex-1/std) >= 1.5.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "codspeed-criterion-compat"

%package     -n %{name}+async
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "async"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures) = %{version}
Requires:       crate(codspeed-criterion-compat-walltime-4/async) >= 4.4.1
Provides:       crate(%{pkgname}/async) = %{version}

%description -n %{name}+async
This metapackage enables feature "async" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-futures
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "async_futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(codspeed-criterion-compat-walltime-4/async-futures) >= 4.4.1
Requires:       crate(futures-0.3/executor) >= 0.3.0
Provides:       crate(%{pkgname}/async-futures) = %{version}

%description -n %{name}+async-futures
This metapackage enables feature "async_futures" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-smol
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "async_smol"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(%{pkgname}/smol) = %{version}
Requires:       crate(codspeed-criterion-compat-walltime-4/async-smol) >= 4.4.1
Provides:       crate(%{pkgname}/async-smol) = %{version}

%description -n %{name}+async-smol
This metapackage enables feature "async_smol" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-std
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "async_std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(async-std-1/default) >= 1.12.0
Requires:       crate(codspeed-criterion-compat-walltime-4/async-std) >= 4.4.1
Provides:       crate(%{pkgname}/async-std) = %{version}

%description -n %{name}+async-std
This metapackage enables feature "async_std" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-tokio
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "async_tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(codspeed-criterion-compat-walltime-4/async-tokio) >= 4.4.1
Provides:       crate(%{pkgname}/async-tokio) = %{version}

%description -n %{name}+async-tokio
This metapackage enables feature "async_tokio" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cargo-bench-support
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "cargo_bench_support"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(codspeed-criterion-compat-walltime-4/cargo-bench-support) >= 4.4.1
Provides:       crate(%{pkgname}/cargo-bench-support) = %{version}

%description -n %{name}+cargo-bench-support
This metapackage enables feature "cargo_bench_support" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+csv-output
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "csv_output"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(codspeed-criterion-compat-walltime-4/csv-output) >= 4.4.1
Provides:       crate(%{pkgname}/csv-output) = %{version}

%description -n %{name}+csv-output
This metapackage enables feature "csv_output" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cargo-bench-support) = %{version}
Requires:       crate(%{pkgname}/plotters) = %{version}
Requires:       crate(%{pkgname}/rayon) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/futures) = %{version}

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+html-reports
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "html_reports"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(codspeed-criterion-compat-walltime-4/html-reports) >= 4.4.1
Provides:       crate(%{pkgname}/html-reports) = %{version}

%description -n %{name}+html-reports
This metapackage enables feature "html_reports" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+plotters
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "plotters"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(codspeed-criterion-compat-walltime-4/plotters) >= 4.4.1
Provides:       crate(%{pkgname}/plotters) = %{version}

%description -n %{name}+plotters
This metapackage enables feature "plotters" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(codspeed-criterion-compat-walltime-4/rayon) >= 4.4.1
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smol
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "smol"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smol-2) >= 2.0.0
Provides:       crate(%{pkgname}/smol) = %{version}

%description -n %{name}+smol
This metapackage enables feature "smol" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/rt) >= 1.39.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

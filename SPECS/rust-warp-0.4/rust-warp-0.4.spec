%global crate_name warp
%global full_version 0.4.2
%global pkgname warp-0.4

Name:           rust-warp-0.4
Version:        0.4.2
Release:        %autorelease
Summary:        Rust crate "warp"
License:        MIT
URL:            https://github.com/seanmonstar/warp
#!RemoteAsset:  sha256:51d06d9202adc1f15d709c4f4a2069be5428aa912cc025d6f268ac441ab066b0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(futures-util-0.3/sink) >= 0.3.0
Requires:       crate(headers-0.4/default) >= 0.4.0
Requires:       crate(http-1/default) >= 1.0.0
Requires:       crate(http-body-1/default) >= 1.0.0
Requires:       crate(http-body-util-0.1/default) >= 0.1.2
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(mime-0.3/default) >= 0.3.0
Requires:       crate(mime-guess-2/default) >= 2.0.0
Requires:       crate(percent-encoding-2/default) >= 2.1.0
Requires:       crate(pin-project-1/default) >= 1.0.0
Requires:       crate(scoped-tls-1/default) >= 1.0.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(serde-urlencoded-0.7/default) >= 0.7.1
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/fs) >= 1.0.0
Requires:       crate(tokio-1/io-util) >= 1.0.0
Requires:       crate(tokio-1/sync) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Requires:       crate(tokio-util-0.7/default) >= 0.7.1
Requires:       crate(tokio-util-0.7/io) >= 0.7.1
Requires:       crate(tower-service-0.3/default) >= 0.3.0
Requires:       crate(tracing-0.1/log) >= 0.1.21
Requires:       crate(tracing-0.1/std) >= 0.1.21
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "warp"

%package     -n %{name}+async-compression
Summary:        Serve the web at warp speeds - feature "async-compression"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-compression-0.4/default) >= 0.4.5
Requires:       crate(async-compression-0.4/tokio) >= 0.4.5
Provides:       crate(%{pkgname}/async-compression) = %{version}

%description -n %{name}+async-compression
This metapackage enables feature "async-compression" for the Rust warp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compression
Summary:        Serve the web at warp speeds - feature "compression"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/compression-brotli) = %{version}
Requires:       crate(%{pkgname}/compression-gzip) = %{version}
Provides:       crate(%{pkgname}/compression) = %{version}

%description -n %{name}+compression
This metapackage enables feature "compression" for the Rust warp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compression-brotli
Summary:        Serve the web at warp speeds - feature "compression-brotli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-compression-0.4/brotli) >= 0.4.5
Requires:       crate(async-compression-0.4/tokio) >= 0.4.5
Provides:       crate(%{pkgname}/compression-brotli) = %{version}

%description -n %{name}+compression-brotli
This metapackage enables feature "compression-brotli" for the Rust warp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compression-gzip
Summary:        Serve the web at warp speeds - feature "compression-gzip"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-compression-0.4/deflate) >= 0.4.5
Requires:       crate(async-compression-0.4/gzip) >= 0.4.5
Requires:       crate(async-compression-0.4/tokio) >= 0.4.5
Provides:       crate(%{pkgname}/compression-gzip) = %{version}

%description -n %{name}+compression-gzip
This metapackage enables feature "compression-gzip" for the Rust warp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+multipart
Summary:        Serve the web at warp speeds - feature "multipart"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(multer-3/default) >= 3.0.0
Provides:       crate(%{pkgname}/multipart) = %{version}

%description -n %{name}+multipart
This metapackage enables feature "multipart" for the Rust warp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+server
Summary:        Serve the web at warp speeds - feature "server"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-1/default) >= 1.0.0
Requires:       crate(hyper-util-0.1/default) >= 0.1.12
Requires:       crate(hyper-util-0.1/http1) >= 0.1.12
Requires:       crate(hyper-util-0.1/http2) >= 0.1.12
Requires:       crate(hyper-util-0.1/server) >= 0.1.12
Requires:       crate(hyper-util-0.1/server-auto) >= 0.1.12
Requires:       crate(hyper-util-0.1/server-graceful) >= 0.1.12
Requires:       crate(hyper-util-0.1/service) >= 0.1.12
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.12
Requires:       crate(tokio-1/fs) >= 1.0.0
Requires:       crate(tokio-1/io-util) >= 1.0.0
Requires:       crate(tokio-1/net) >= 1.0.0
Requires:       crate(tokio-1/sync) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Provides:       crate(%{pkgname}/server) = %{version}

%description -n %{name}+server
This metapackage enables feature "server" for the Rust warp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+test
Summary:        Serve the web at warp speeds - feature "test"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/server) = %{version}
Requires:       crate(futures-channel-0.3/default) >= 0.3.17
Requires:       crate(futures-channel-0.3/sink) >= 0.3.17
Requires:       crate(hyper-1/client) >= 1.0.0
Requires:       crate(hyper-1/http1) >= 1.0.0
Provides:       crate(%{pkgname}/test) = %{version}

%description -n %{name}+test
This metapackage enables feature "test" for the Rust warp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+websocket
Summary:        Serve the web at warp speeds - feature "websocket"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-1/default) >= 1.0.0
Requires:       crate(hyper-util-0.1/http1) >= 0.1.12
Requires:       crate(hyper-util-0.1/http2) >= 0.1.12
Requires:       crate(hyper-util-0.1/server) >= 0.1.12
Requires:       crate(hyper-util-0.1/server-auto) >= 0.1.12
Requires:       crate(hyper-util-0.1/server-graceful) >= 0.1.12
Requires:       crate(hyper-util-0.1/service) >= 0.1.12
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.12
Requires:       crate(tokio-tungstenite-0.27/default) >= 0.27.0
Provides:       crate(%{pkgname}/websocket) = %{version}

%description -n %{name}+websocket
This metapackage enables feature "websocket" for the Rust warp crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

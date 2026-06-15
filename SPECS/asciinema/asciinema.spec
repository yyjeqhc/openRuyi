# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name asciinema
%global full_version 3.2.0
%global pkgname asciinema-3

Name:           rust-asciinema-3
Version:        3.2.0
Release:        %autorelease
Summary:        Terminal session recorder, streamer, and player
License:        GPL-3.0-or-later
URL:            https://asciinema.org
#!RemoteAsset:  sha256:1ce7128d51c1c2fe6a58ae80e2d9a6206a5338d29bf64aab04c50a73a1cd29dd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rust

BuildRequires:  rust-rpm-macros
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  rust-hyper-1+server >= 1.9.0
BuildRequires:  crate(hyper-1/server) >= 1.9.0
BuildRequires:  crate(anyhow-1/default) >= 1.0.0
BuildRequires:  crate(async-trait-0.1/default) >= 0.1.0
BuildRequires:  crate(avt-0.17/default) >= 0.17.0
BuildRequires:  crate(axum-0.8/http1) >= 0.8.0
BuildRequires:  crate(axum-0.8/ws) >= 0.8.0
BuildRequires:  crate(bytes-1/default) >= 1.11.0
BuildRequires:  crate(clap-4/default) >= 4.0.0
BuildRequires:  crate(clap-4/derive) >= 4.0.0
BuildRequires:  crate(clap-4/wrap-help) >= 4.0.0
BuildRequires:  crate(clap-complete-4/default) >= 4.0.0
BuildRequires:  crate(clap-mangen-0.2/default) >= 0.2.0
BuildRequires:  crate(config-0.15/toml) >= 0.15.0
BuildRequires:  crate(futures-util-0.3/sink) >= 0.3.0
BuildRequires:  crate(nix-0.30/default) >= 0.30.0
BuildRequires:  crate(nix-0.30/fs) >= 0.30.0
BuildRequires:  crate(nix-0.30/poll) >= 0.30.0
BuildRequires:  crate(nix-0.30/process) >= 0.30.0
BuildRequires:  crate(nix-0.30/signal) >= 0.30.0
BuildRequires:  crate(nix-0.30/term) >= 0.30.0
BuildRequires:  crate(rand-0.9/default) >= 0.9.0
BuildRequires:  crate(reqwest-0.12/blocking) >= 0.12.0
BuildRequires:  crate(reqwest-0.12/gzip) >= 0.12.0
BuildRequires:  crate(reqwest-0.12/json) >= 0.12.0
BuildRequires:  crate(reqwest-0.12/multipart) >= 0.12.0
BuildRequires:  crate(reqwest-0.12/rustls-tls-native-roots) >= 0.12.0
BuildRequires:  crate(reqwest-0.12/stream) >= 0.12.0
BuildRequires:  crate(rgb-0.8) >= 0.8.0
BuildRequires:  crate(rust-embed-8/default) >= 8.8.0
BuildRequires:  crate(rustls-0.23/ring) >= 0.23.0
BuildRequires:  crate(rustyline-17) >= 17.0.0
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/derive) >= 1.0.0
BuildRequires:  crate(serde-json-1/default) >= 1.0.0
BuildRequires:  crate(signal-hook-0.3) >= 0.3.0
BuildRequires:  crate(signal-hook-tokio-0.3/default) >= 0.3.0
BuildRequires:  crate(signal-hook-tokio-0.3/futures-v0-3) >= 0.3.0
BuildRequires:  crate(tempfile-3/default) >= 3.23.0
BuildRequires:  crate(tokio-1/default) >= 1.40.0
BuildRequires:  crate(tokio-1/fs) >= 1.40.0
BuildRequires:  crate(tokio-1/net) >= 1.40.0
BuildRequires:  crate(tokio-1/process) >= 1.40.0
BuildRequires:  crate(tokio-1/rt-multi-thread) >= 1.40.0
BuildRequires:  crate(tokio-1/sync) >= 1.40.0
BuildRequires:  crate(tokio-1/time) >= 1.40.0
BuildRequires:  crate(tokio-stream-0.1/sync) >= 0.1.0
BuildRequires:  crate(tokio-stream-0.1/time) >= 0.1.0
BuildRequires:  crate(tokio-tungstenite-0.28/connect) >= 0.28.0
BuildRequires:  crate(tokio-tungstenite-0.28/rustls-tls-native-roots) >= 0.28.0
BuildRequires:  crate(tokio-util-0.7/default) >= 0.7.0
BuildRequires:  crate(tokio-util-0.7/rt) >= 0.7.0
BuildRequires:  crate(tower-http-0.6/compression-gzip) >= 0.6.0
BuildRequires:  crate(tower-http-0.6/default) >= 0.6.0
BuildRequires:  crate(tower-http-0.6/trace) >= 0.6.0
BuildRequires:  crate(tracing-0.1) >= 0.1.0
BuildRequires:  crate(tracing-subscriber-0.3/env-filter) >= 0.3.20
BuildRequires:  crate(tracing-subscriber-0.3/fmt) >= 0.3.20
BuildRequires:  crate(url-2/default) >= 2.5.0
BuildRequires:  crate(uuid-1/default) >= 1.6.0
BuildRequires:  crate(uuid-1/v4) >= 1.6.0
BuildRequires:  crate(which-8/default) >= 8.0.0
BuildRequires:  crate(clipboard-win-5) >= 5.0.0
BuildRequires:  crate(clipboard-win-5/default) >= 5.0.0
BuildRequires:  crate(windows-sys-0.60) >= 0.60.2
BuildRequires:  crate(windows-sys-0.60/default) >= 0.60.2
BuildRequires:  crate(schannel-0.1) >= 0.1.0
BuildRequires:  crate(schannel-0.1/default) >= 0.1.0
BuildRequires:  crate(winapi-util-0.1) >= 0.1.0
BuildRequires:  crate(winapi-util-0.1/default) >= 0.1.0
BuildRequires:  crate(error-code-3) >= 3.0.0
BuildRequires:  crate(error-code-3/default) >= 3.0.0

%description
Terminal session recorder, streamer, and player.

%install
install -D -m 0755 target/release/asciinema %{buildroot}%{_bindir}/asciinema

%files
%{_bindir}/asciinema

%changelog
%autochangelog

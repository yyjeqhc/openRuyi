# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: corestudy <2760018909@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           aardvark-dns
Version:        1.17.1
Release:        %autorelease
License:        Apache-2.0 AND MIT AND Zlib
Summary:        Authoritative DNS server for A/AAAA container records
URL:            https://github.com/containers/aardvark-dns
#!RemoteAsset:  sha256:25b39bfad079a03862825b2f9db8b71b82fc80aad5552a9c76ea912edc9b889e
Source0:        https://github.com/containers/aardvark-dns/archive/v%{version}.tar.gz
BuildSystem:    rust

Patch0:         0001-fix-version.patch

BuildOption(build):  -- --bin aardvark-dns

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
# Static Rust crate closure for aardvark-dns.
BuildRequires:  crate(arc-swap-1) >= 1.7.1
BuildRequires:  crate(arc-swap-1/default)
BuildRequires:  crate(chrono-0.4) >= 0.4.42
BuildRequires:  crate(chrono-0.4/default)
BuildRequires:  crate(clap-4) >= 4.5.51
BuildRequires:  crate(clap-4/default)
BuildRequires:  crate(clap-4/derive)
BuildRequires:  crate(flume-0.11) >= 0.11.1
BuildRequires:  crate(flume-0.11/default)
BuildRequires:  crate(futures-0.3) >= 0.3.31
BuildRequires:  crate(futures-0.3/default)
BuildRequires:  crate(futures-util-0.3) >= 0.3.31
BuildRequires:  crate(hickory-client-0.25) >= 0.25.2
BuildRequires:  crate(hickory-client-0.25/default)
BuildRequires:  crate(hickory-proto-0.25) >= 0.25.2
BuildRequires:  crate(hickory-proto-0.25/default)
BuildRequires:  crate(hickory-proto-0.25/tokio)
BuildRequires:  crate(hickory-server-0.25) >= 0.25.2
BuildRequires:  crate(hickory-server-0.25/default)
BuildRequires:  crate(inotify-0.11) >= 0.11.0
BuildRequires:  crate(inotify-0.11/default)
BuildRequires:  crate(libc-0.2) >= 0.2.177
BuildRequires:  crate(libc-0.2/default)
BuildRequires:  crate(log-0.4) >= 0.4.28
BuildRequires:  crate(log-0.4/default)
BuildRequires:  crate(nix-0.30) >= 0.30.1
BuildRequires:  crate(nix-0.30/default)
BuildRequires:  crate(nix-0.30/fs)
BuildRequires:  crate(nix-0.30/net)
BuildRequires:  crate(nix-0.30/signal)
BuildRequires:  crate(syslog-7) >= 7.0.0
BuildRequires:  crate(syslog-7/default)
BuildRequires:  crate(tokio-1) >= 1.48.0
BuildRequires:  crate(tokio-1/default)
BuildRequires:  crate(tokio-1/macros)
BuildRequires:  crate(tokio-1/net)
BuildRequires:  crate(tokio-1/rt-multi-thread)
BuildRequires:  crate(tokio-1/signal)
BuildRequires:  crate(windows-link-0.1) >= 0.1.3
BuildRequires:  crate(windows-link-0.1/default)

%description
%{summary}

Forwards other requests to configured resolvers.
Read more about configuration in `src/backend/mod.rs`.

%install
install -Dm0755 target/release/aardvark-dns %{buildroot}%{_libexecdir}/podman/aardvark-dns

%check
# Upstream's integration tests require network namespace setup, bats, and a
# container-oriented environment. Keep the build check minimal here.

%files
%doc README.md
%license LICENSE
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/aardvark-dns

%changelog
%autochangelog

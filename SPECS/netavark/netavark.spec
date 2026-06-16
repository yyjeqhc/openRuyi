# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           netavark
Version:        1.17.1
Release:        %autorelease
License:        Apache-2.0 AND BSD-3-Clause AND MIT
Summary:        OCI network stack
URL:            https://github.com/containers/netavark
#!RemoteAsset:  sha256:00009bfad079a03862825b2f9db8b71b82fc80aad5552a9c76ea912edc9b0000
Source0:        https://github.com/containers/netavark/archive/v%{version}.tar.gz
BuildSystem:    rust

Patch0:         0001-fix-version.patch

BuildOption(build):  -- --bin netavark --bin netavark-dhcp-proxy-client --bin netavark-connection-tester

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  make
BuildRequires:  go-md2man
# build.rs needs a protoc binary for generated DHCP proxy bindings.
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  systemd
BuildRequires:  pkgconfig(systemd)

# Static Rust crate closure for netavark 1.17.1.
BuildRequires:  crate(anyhow-1) >= 1.0.93
BuildRequires:  crate(anyhow-1/default)
BuildRequires:  crate(chrono-0.4) >= 0.4.42
BuildRequires:  crate(chrono-0.4/clock)
BuildRequires:  crate(clap-4) >= 4.5.51
BuildRequires:  crate(clap-4/default)
BuildRequires:  crate(clap-4/derive)
BuildRequires:  crate(clap-4/env)
BuildRequires:  crate(env-logger-0.11) >= 0.11.8
BuildRequires:  crate(env-logger-0.11/default)
BuildRequires:  crate(fs2-0.4) >= 0.4.3
BuildRequires:  crate(fs2-0.4/default)
# Cargo's offline resolver also needs fs2's Windows target source crates.
BuildRequires:  crate(winapi-0.3) >= 0.3.9
BuildRequires:  crate(winapi-i686-pc-windows-gnu-0.4) >= 0.4.0
BuildRequires:  crate(winapi-x86-64-pc-windows-gnu-0.4) >= 0.4.0
BuildRequires:  crate(futures-channel-0.3) >= 0.3.31
BuildRequires:  crate(futures-channel-0.3/default)
BuildRequires:  crate(futures-core-0.3) >= 0.3.31
BuildRequires:  crate(futures-core-0.3/default)
BuildRequires:  crate(futures-util-0.3) >= 0.3.31
BuildRequires:  crate(futures-util-0.3/default)
BuildRequires:  crate(hyper-util-0.1) >= 0.1.17
BuildRequires:  crate(hyper-util-0.1/default)
BuildRequires:  crate(ipnet-2) >= 2.11.0
BuildRequires:  crate(ipnet-2/default)
BuildRequires:  crate(ipnet-2/serde)
BuildRequires:  crate(iptables-0.6) >= 0.6.0
BuildRequires:  crate(iptables-0.6/default)
BuildRequires:  crate(libc-0.2) >= 0.2.157
BuildRequires:  crate(libc-0.2/default)
BuildRequires:  crate(log-0.4) >= 0.4.28
BuildRequires:  crate(log-0.4/default)
BuildRequires:  crate(mozim-0.3) >= 0.3.1
BuildRequires:  crate(mozim-0.3/default)
BuildRequires:  crate(netlink-packet-core-0.8) >= 0.8.1
BuildRequires:  crate(netlink-packet-core-0.8/default)
BuildRequires:  crate(netlink-packet-route-0.25) >= 0.25.1
BuildRequires:  crate(netlink-packet-route-0.25/default)
BuildRequires:  crate(netlink-sys-0.8) >= 0.8.7
BuildRequires:  crate(netlink-sys-0.8/default)
BuildRequires:  crate(nftables-0.6) >= 0.6.3
BuildRequires:  crate(nftables-0.6/default)
BuildRequires:  crate(nix-0.30) >= 0.30.1
BuildRequires:  crate(nix-0.30/default)
BuildRequires:  crate(nix-0.30/net)
BuildRequires:  crate(nix-0.30/sched)
BuildRequires:  crate(nix-0.30/signal)
BuildRequires:  crate(nix-0.30/socket)
BuildRequires:  crate(nix-0.30/user)
BuildRequires:  crate(prost-0.14) >= 0.14.1
BuildRequires:  crate(prost-0.14/default)
BuildRequires:  crate(rand-0.9) >= 0.9.2
BuildRequires:  crate(rand-0.9/default)
BuildRequires:  crate(serde-1) >= 1.0.228
BuildRequires:  crate(serde-1/default)
BuildRequires:  crate(serde-1/derive)
BuildRequires:  crate(serde-json-1) >= 1.0.145
BuildRequires:  crate(serde-json-1/default)
BuildRequires:  crate(sha2-0.10) >= 0.10.9
BuildRequires:  crate(sha2-0.10/default)
BuildRequires:  crate(tokio-1) >= 1.48.0
BuildRequires:  crate(tokio-1/default)
BuildRequires:  crate(tokio-1/fs)
BuildRequires:  crate(tokio-1/rt)
BuildRequires:  crate(tokio-1/rt-multi-thread)
BuildRequires:  crate(tokio-1/signal)
BuildRequires:  crate(tokio-1/time)
BuildRequires:  crate(tokio-stream-0.1) >= 0.1.17
BuildRequires:  crate(tokio-stream-0.1/default)
BuildRequires:  crate(tokio-stream-0.1/net)
BuildRequires:  crate(tonic-0.14) >= 0.14.2
BuildRequires:  crate(tonic-0.14/default)
BuildRequires:  crate(tonic-prost-0.14) >= 0.14.2
BuildRequires:  crate(tonic-prost-0.14/default)
BuildRequires:  crate(tonic-prost-build-0.14) >= 0.14.2
BuildRequires:  crate(tonic-prost-build-0.14/default)
BuildRequires:  crate(tower-0.5) >= 0.5.2
BuildRequires:  crate(tower-0.5/default)
BuildRequires:  crate(tower-0.5/util)
# Cargo's offline resolver also needs zbus's Windows target source crate.
BuildRequires:  crate(uds-windows-1) >= 1.1.0
BuildRequires:  crate(zbus-5) >= 5.12.0
BuildRequires:  crate(zbus-5/default)

Requires:       nftables
Requires:       aardvark-dns

%description
%{summary}

Netavark is a rust based network stack for containers. It is being
designed to work with Podman but is also applicable for other OCI
container management applications.

Netavark is a tool for configuring networking for Linux containers.
Its features include:
* Configuration of container networks via JSON configuration file
* Creation and management of required network interfaces,
    including MACVLAN networks
* All required firewall configuration to perform NAT and port
    forwarding as required for containers
* Support for iptables, firewalld and nftables
* Support for rootless containers
* Support for IPv4 and IPv6
* Support for container DNS resolution via aardvark-dns.

%build -p
export NETAVARK_DEFAULT_FW=nftables
%__make -C docs

%install
mkdir -p bin
install -Dm0755 target/release/netavark bin/netavark
install -Dm0755 target/release/netavark-dhcp-proxy-client bin/netavark-dhcp-proxy-client
install -Dm0755 target/release/netavark-connection-tester bin/netavark-connection-tester

%__make DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBEXECDIR=%{_libexecdir} \
  LIBEXECPODMAN=%{_libexecdir}/podman SYSTEMDDIR=%{_unitdir} install

%check
# Upstream's tests require network namespace setup, bats, and a
# container-oriented environment. Keep the build check minimal here.

%preun
%systemd_preun netavark-dhcp-proxy.service netavark-firewalld-reload.service netavark-nftables-reload.service

%postun
%systemd_postun netavark-dhcp-proxy.service netavark-firewalld-reload.service netavark-nftables-reload.service

%files
%doc README.md
%license LICENSE
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/netavark
%{_mandir}/man1/netavark.1*
%{_mandir}/man7/netavark-firewalld.7*
%{_unitdir}/netavark-dhcp-proxy.service
%{_unitdir}/netavark-dhcp-proxy.socket
%{_unitdir}/netavark-firewalld-reload.service
%{_unitdir}/netavark-nftables-reload.service

%changelog
%autochangelog

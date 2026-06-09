# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Ruoqing He <heruoqing@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global gitver 52.0

Name:           cloud-hypervisor
Url:            https://github.com/cloud-hypervisor/cloud-hypervisor
Summary:        Cloud Hypervisor is a Virtual Machine Monitor (VMM) that runs on top of KVM
Version:        %{gitver}
Release:        %autorelease
License:        Apache-2.0 OR BSD-3-Clause


%global ch_commit 829676e6403ff3fa711c9e901f90f05737c08b88
%global micro_http_commit 876f3feccc30e09225f2c77bf95a6b2d46a9259e

#!RemoteAsset:  git+https://github.com/cloud-hypervisor/cloud-hypervisor.git#%{ch_commit}
#!CreateArchive
Source0:        %{name}-%{ch_commit}.tar.gz

#!RemoteAsset:  git+https://github.com/firecracker-microvm/micro-http.git#%{micro_http_commit}
#!CreateArchive
Source1:        micro-http-%{micro_http_commit}.tar.gz

BuildSystem:    rust

BuildRequires:  rust-rpm-macros
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  binutils
BuildRequires:  pkgconfig(openssl)

# Static Rust crate closure for cloud-hypervisor %{ch_commit}.
BuildRequires:  crate(acpi-tables-0.2) >= 0.2.0
BuildRequires:  crate(adler2-2) >= 2.0.1
BuildRequires:  crate(aho-corasick-1) >= 1.1.4
BuildRequires:  crate(aho-corasick-1/perf-literal) >= 1.1.4
BuildRequires:  crate(aho-corasick-1/std) >= 1.1.4
BuildRequires:  crate(anstream-1) >= 1.0.0
BuildRequires:  crate(anstream-1/auto) >= 1.0.0
BuildRequires:  crate(anstream-1/default) >= 1.0.0
BuildRequires:  crate(anstream-1/wincon) >= 1.0.0
BuildRequires:  crate(anstyle-1) >= 1.0.14
BuildRequires:  crate(anstyle-1/default) >= 1.0.14
BuildRequires:  crate(anstyle-1/std) >= 1.0.14
BuildRequires:  crate(anstyle-parse-1) >= 1.0.0
BuildRequires:  crate(anstyle-parse-1/default) >= 1.0.0
BuildRequires:  crate(anstyle-parse-1/utf8) >= 1.0.0
BuildRequires:  crate(anstyle-query-1) >= 1.1.5
BuildRequires:  crate(anyhow-1) >= 1.0.102
BuildRequires:  crate(anyhow-1/default) >= 1.0.102
BuildRequires:  crate(anyhow-1/std) >= 1.0.102
BuildRequires:  crate(arc-swap-1) >= 1.9.1
BuildRequires:  crate(async-broadcast-0.7) >= 0.7.2
BuildRequires:  crate(async-broadcast-0.7/default) >= 0.7.2
BuildRequires:  crate(bitflags-1) >= 1.3.2
BuildRequires:  crate(bitflags-1/default) >= 1.3.2
BuildRequires:  crate(bitflags-2) >= 2.11.1
BuildRequires:  crate(bitflags-2/std) >= 2.11.1
BuildRequires:  crate(blocking-1) >= 1.6.2
BuildRequires:  crate(blocking-1/default) >= 1.6.2
BuildRequires:  crate(bitfield-struct-0.13) >= 0.13.0
BuildRequires:  crate(bitfield-struct-0.13/default) >= 0.13.0
BuildRequires:  crate(bitfield-struct-0.10) >= 0.10.1
BuildRequires:  crate(bitfield-struct-0.10/default) >= 0.10.1
BuildRequires:  crate(block-buffer-0.12) >= 0.12.0
BuildRequires:  crate(byteorder-1) >= 1.5.0
BuildRequires:  crate(byteorder-1/default) >= 1.5.0
BuildRequires:  crate(byteorder-1/std) >= 1.5.0
BuildRequires:  crate(cc-1) >= 1.2.63
BuildRequires:  crate(cc-1/parallel) >= 1.2.63
BuildRequires:  crate(cfg-if-1) >= 1.0.4
BuildRequires:  crate(chacha20-0.10) >= 0.10.0
BuildRequires:  crate(chacha20-0.10/rng) >= 0.10.0
BuildRequires:  crate(clap-4) >= 4.6.1
BuildRequires:  crate(clap-4/cargo) >= 4.6.1
BuildRequires:  crate(clap-4/color) >= 4.6.1
BuildRequires:  crate(clap-4/default) >= 4.6.1
BuildRequires:  crate(clap-4/error-context) >= 4.6.1
BuildRequires:  crate(clap-4/help) >= 4.6.1
BuildRequires:  crate(clap-4/std) >= 4.6.1
BuildRequires:  crate(clap-4/string) >= 4.6.1
BuildRequires:  crate(clap-4/suggestions) >= 4.6.1
BuildRequires:  crate(clap-4/usage) >= 4.6.1
BuildRequires:  crate(clap-4/wrap-help) >= 4.6.1
BuildRequires:  crate(clap-builder-4) >= 4.6.0
BuildRequires:  crate(clap-builder-4/cargo) >= 4.6.0
BuildRequires:  crate(clap-builder-4/color) >= 4.6.0
BuildRequires:  crate(clap-builder-4/error-context) >= 4.6.0
BuildRequires:  crate(clap-builder-4/help) >= 4.6.0
BuildRequires:  crate(clap-builder-4/std) >= 4.6.0
BuildRequires:  crate(clap-builder-4/string) >= 4.6.0
BuildRequires:  crate(clap-builder-4/suggestions) >= 4.6.0
BuildRequires:  crate(clap-builder-4/usage) >= 4.6.0
BuildRequires:  crate(clap-builder-4/wrap-help) >= 4.6.0
BuildRequires:  crate(clap-lex-1) >= 1.1.0
BuildRequires:  crate(colorchoice-1) >= 1.0.5
BuildRequires:  crate(concat-idents-1) >= 1.1.5
BuildRequires:  crate(concat-idents-1/default) >= 1.1.5
BuildRequires:  crate(const-oid-0.10) >= 0.10.2
BuildRequires:  crate(cpufeatures-0.3) >= 0.3.0
BuildRequires:  crate(crc-any-2) >= 2.5.0
BuildRequires:  crate(crc-any-2/alloc) >= 2.5.0
BuildRequires:  crate(crc-any-2/debug-helper) >= 2.5.0
BuildRequires:  crate(crc-any-2/default) >= 2.5.0
BuildRequires:  crate(crc32fast-1) >= 1.5.0
BuildRequires:  crate(crc32fast-1/default) >= 1.5.0
BuildRequires:  crate(crc32fast-1/std) >= 1.5.0
BuildRequires:  crate(crypto-common-0.2) >= 0.2.2
BuildRequires:  crate(darling-0.23) >= 0.23.0
BuildRequires:  crate(darling-0.23/default) >= 0.23.0
BuildRequires:  crate(darling-0.23/suggestions) >= 0.23.0
BuildRequires:  crate(darling-core-0.23) >= 0.23.0
BuildRequires:  crate(darling-core-0.23/strsim) >= 0.23.0
BuildRequires:  crate(darling-core-0.23/suggestions) >= 0.23.0
BuildRequires:  crate(debug-helper-0.3) >= 0.3.13
BuildRequires:  crate(dhat-0.3) >= 0.3.3
BuildRequires:  crate(dhat-0.3/default) >= 0.3.3
BuildRequires:  crate(dirs-6) >= 6.0.0
BuildRequires:  crate(dirs-6/default) >= 6.0.0
BuildRequires:  crate(digest-0.11) >= 0.11.3
BuildRequires:  crate(digest-0.11/alloc) >= 0.11.3
BuildRequires:  crate(digest-0.11/block-api) >= 0.11.3
BuildRequires:  crate(digest-0.11/default) >= 0.11.3
BuildRequires:  crate(digest-0.11/oid) >= 0.11.3
BuildRequires:  crate(either-1) >= 1.16.0
BuildRequires:  crate(either-1/std) >= 1.16.0
BuildRequires:  crate(either-1/use-std) >= 1.16.0
BuildRequires:  crate(enumflags2-0.7) >= 0.7.12
BuildRequires:  crate(env-filter-1) >= 1.0.1
BuildRequires:  crate(env-filter-1/regex) >= 1.0.1
BuildRequires:  crate(env-logger-0.11) >= 0.11.10
BuildRequires:  crate(env-logger-0.11/auto-color) >= 0.11.10
BuildRequires:  crate(env-logger-0.11/color) >= 0.11.10
BuildRequires:  crate(env-logger-0.11/default) >= 0.11.10
BuildRequires:  crate(env-logger-0.11/humantime) >= 0.11.10
BuildRequires:  crate(env-logger-0.11/regex) >= 0.11.10
BuildRequires:  crate(epoll-4) >= 4.4.0
BuildRequires:  crate(equivalent-1) >= 1.0.2
BuildRequires:  crate(errno-0.3) >= 0.3.14
BuildRequires:  crate(errno-0.3/default) >= 0.3.14
BuildRequires:  crate(errno-0.3/std) >= 0.3.14
BuildRequires:  crate(event-listener-strategy-0.5) >= 0.5.4
BuildRequires:  crate(event-listener-strategy-0.5/default) >= 0.5.4
BuildRequires:  crate(fastrand-2) >= 2.4.1
BuildRequires:  crate(fastrand-2/alloc) >= 2.4.1
BuildRequires:  crate(fastrand-2/default) >= 2.4.1
BuildRequires:  crate(fastrand-2/getrandom) >= 2.4.1
BuildRequires:  crate(fastrand-2/js) >= 2.4.1
BuildRequires:  crate(fastrand-2/std) >= 2.4.1
BuildRequires:  crate(fdt-0.1) >= 0.1.5
BuildRequires:  crate(fdt-0.1/default) >= 0.1.5
BuildRequires:  crate(find-msvc-tools-0.1) >= 0.1.9
BuildRequires:  crate(flate2-1) >= 1.1.9
BuildRequires:  crate(flate2-1/any-impl) >= 1.1.9
BuildRequires:  crate(flate2-1/default) >= 1.1.9
BuildRequires:  crate(flate2-1/miniz-oxide) >= 1.1.9
BuildRequires:  crate(flate2-1/rust-backend) >= 1.1.9
BuildRequires:  crate(flume-0.12) >= 0.12.0
BuildRequires:  crate(flume-0.12/async) >= 0.12.0
BuildRequires:  crate(flume-0.12/default) >= 0.12.0
BuildRequires:  crate(flume-0.12/eventual-fairness) >= 0.12.0
BuildRequires:  crate(flume-0.12/fastrand) >= 0.12.0
BuildRequires:  crate(flume-0.12/futures-core) >= 0.12.0
BuildRequires:  crate(flume-0.12/futures-sink) >= 0.12.0
BuildRequires:  crate(flume-0.12/select) >= 0.12.0
BuildRequires:  crate(futures-0.3) >= 0.3.32
BuildRequires:  crate(futures-0.3/default) >= 0.3.32
BuildRequires:  crate(futures-core-0.3) >= 0.3.32
BuildRequires:  crate(futures-sink-0.3) >= 0.3.32
BuildRequires:  crate(gdbstub-0.7) >= 0.7.10
BuildRequires:  crate(gdbstub-0.7/default) >= 0.7.10
BuildRequires:  crate(gdbstub-arch-0.3) >= 0.3.3
BuildRequires:  crate(gdbstub-arch-0.3/default) >= 0.3.3
BuildRequires:  crate(getrandom-0.4) >= 0.4.2
BuildRequires:  crate(getrandom-0.4/std) >= 0.4.2
BuildRequires:  crate(getrandom-0.4/sys-rng) >= 0.4.2
BuildRequires:  crate(hashbrown-0.17) >= 0.17.0
BuildRequires:  crate(hybrid-array-0.4) >= 0.4.12
BuildRequires:  crate(iced-x86-1) >= 1.21.0
BuildRequires:  crate(iced-x86-1/decoder) >= 1.21.0
BuildRequires:  crate(iced-x86-1/encoder) >= 1.21.0
BuildRequires:  crate(iced-x86-1/instr-info) >= 1.21.0
BuildRequires:  crate(iced-x86-1/lazy-static) >= 1.21.0
BuildRequires:  crate(iced-x86-1/no-d3now) >= 1.21.0
BuildRequires:  crate(iced-x86-1/no-evex) >= 1.21.0
BuildRequires:  crate(iced-x86-1/no-vex) >= 1.21.0
BuildRequires:  crate(iced-x86-1/no-xop) >= 1.21.0
BuildRequires:  crate(iced-x86-1/op-code-info) >= 1.21.0
BuildRequires:  crate(iced-x86-1/std) >= 1.21.0
BuildRequires:  crate(ident-case-1) >= 1.0.1
BuildRequires:  crate(igvm-0.4) >= 0.4.0
BuildRequires:  crate(igvm-0.4/default) >= 0.4.0
BuildRequires:  crate(igvm-defs-0.4) >= 0.4.0
BuildRequires:  crate(igvm-defs-0.4/default) >= 0.4.0
BuildRequires:  crate(igvm-defs-0.4/unstable) >= 0.4.0
BuildRequires:  crate(indexmap-2) >= 2.14.0
BuildRequires:  crate(indexmap-2/default) >= 2.14.0
BuildRequires:  crate(indexmap-2/std) >= 2.14.0
BuildRequires:  crate(iommufd-bindings-0.1) >= 0.1.0
BuildRequires:  crate(iommufd-ioctls-0.1) >= 0.1.0
BuildRequires:  crate(ipnetwork-0.20) >= 0.20.0
BuildRequires:  crate(ipnetwork-0.20/default) >= 0.20.0
BuildRequires:  crate(io-uring-0.7) >= 0.7.12
BuildRequires:  crate(io-uring-0.7/default) >= 0.7.12
BuildRequires:  crate(is-terminal-polyfill-1) >= 1.70.2
BuildRequires:  crate(is-terminal-polyfill-1/default) >= 1.70.2
BuildRequires:  crate(itertools-0.14) >= 0.14.0
BuildRequires:  crate(itertools-0.14/default) >= 0.14.0
BuildRequires:  crate(itertools-0.14/use-alloc) >= 0.14.0
BuildRequires:  crate(itertools-0.14/use-std) >= 0.14.0
BuildRequires:  crate(itoa-1) >= 1.0.18
BuildRequires:  crate(jiff-0.2) >= 0.2.28
BuildRequires:  crate(jiff-0.2/alloc) >= 0.2.28
BuildRequires:  crate(jiff-0.2/std) >= 0.2.28
BuildRequires:  crate(jobserver-0.1) >= 0.1.34
BuildRequires:  crate(kvm-bindings-0.14) >= 0.14.0
BuildRequires:  crate(kvm-bindings-0.14/fam-wrappers) >= 0.14.0
BuildRequires:  crate(kvm-bindings-0.14/serde) >= 0.14.0
BuildRequires:  crate(kvm-bindings-0.14/vmm-sys-util) >= 0.14.0
BuildRequires:  crate(kvm-ioctls-0.24) >= 0.24.0
BuildRequires:  crate(landlock-0.4) >= 0.4.5
BuildRequires:  crate(lazy-static-1) >= 1.5.0
BuildRequires:  crate(libc-0.2) >= 0.2.186
BuildRequires:  crate(libc-0.2/default) >= 0.2.186
BuildRequires:  crate(libc-0.2/std) >= 0.2.186
BuildRequires:  crate(libssh2-sys-0.3) >= 0.3.1
BuildRequires:  crate(libssh2-sys-0.3/default) >= 0.3.1
BuildRequires:  crate(libssh2-sys-0.3/vendored-openssl) >= 0.3.1
BuildRequires:  crate(libz-sys-1) >= 1.1.28
BuildRequires:  crate(libz-sys-1/libc) >= 1.1.28
BuildRequires:  crate(linux-loader-0.13) >= 0.13.2
BuildRequires:  crate(linux-loader-0.13/bzimage) >= 0.13.2
BuildRequires:  crate(linux-loader-0.13/default) >= 0.13.2
BuildRequires:  crate(linux-loader-0.13/elf) >= 0.13.2
BuildRequires:  crate(linux-loader-0.13/pe) >= 0.13.2
BuildRequires:  crate(linux-raw-sys-0.12) >= 0.12.1
BuildRequires:  crate(linux-raw-sys-0.12/auxvec) >= 0.12.1
BuildRequires:  crate(linux-raw-sys-0.12/elf) >= 0.12.1
BuildRequires:  crate(linux-raw-sys-0.12/errno) >= 0.12.1
BuildRequires:  crate(linux-raw-sys-0.12/general) >= 0.12.1
BuildRequires:  crate(linux-raw-sys-0.12/ioctl) >= 0.12.1
BuildRequires:  crate(linux-raw-sys-0.12/no-std) >= 0.12.1
BuildRequires:  crate(lock-api-0.4) >= 0.4.14
BuildRequires:  crate(lock-api-0.4/atomic-usize) >= 0.4.14
BuildRequires:  crate(lock-api-0.4/default) >= 0.4.14
BuildRequires:  crate(log-0.4) >= 0.4.30
BuildRequires:  crate(log-0.4/std) >= 0.4.30
BuildRequires:  crate(memchr-2) >= 2.8.1
BuildRequires:  crate(memchr-2/alloc) >= 2.8.1
BuildRequires:  crate(memchr-2/std) >= 2.8.1
BuildRequires:  crate(miniz-oxide-0.8) >= 0.8.9
BuildRequires:  crate(miniz-oxide-0.8/simd) >= 0.8.9
BuildRequires:  crate(miniz-oxide-0.8/simd-adler32) >= 0.8.9
BuildRequires:  crate(miniz-oxide-0.8/with-alloc) >= 0.8.9
BuildRequires:  crate(mintex-0.1) >= 0.1.4
BuildRequires:  crate(mintex-0.1/default) >= 0.1.4
BuildRequires:  crate(mshv-bindings-0.6) >= 0.6.9
BuildRequires:  crate(mshv-bindings-0.6/fam-wrappers) >= 0.6.9
BuildRequires:  crate(mshv-bindings-0.6/serde) >= 0.6.9
BuildRequires:  crate(mshv-bindings-0.6/serde-derive) >= 0.6.9
BuildRequires:  crate(mshv-bindings-0.6/with-serde) >= 0.6.9
BuildRequires:  crate(mshv-ioctls-0.6) >= 0.6.9
BuildRequires:  crate(no-std-net-0.6) >= 0.6.0
BuildRequires:  crate(no-std-net-0.6/std) >= 0.6.0
BuildRequires:  crate(num-enum-0.7) >= 0.7.6
BuildRequires:  crate(num-enum-0.7/default) >= 0.7.6
BuildRequires:  crate(num-enum-0.7/std) >= 0.7.6
BuildRequires:  crate(open-enum-0.5) >= 0.5.2
BuildRequires:  crate(openssl-src-300) >= 300.6.0
BuildRequires:  crate(openssl-src-300/default) >= 300.6.0
BuildRequires:  crate(openssl-src-300/legacy) >= 300.6.0
BuildRequires:  crate(openssl-sys-0.9) >= 0.9.115
BuildRequires:  crate(openssl-sys-0.9/default) >= 0.9.115
BuildRequires:  crate(openssl-sys-0.9/vendored) >= 0.9.115
BuildRequires:  crate(ordered-stream-0.2) >= 0.2.0
BuildRequires:  crate(ordered-stream-0.2/default) >= 0.2.0
BuildRequires:  crate(parking-lot-0.12) >= 0.12.5
BuildRequires:  crate(parking-lot-0.12/default) >= 0.12.5
BuildRequires:  crate(parking-lot-core-0.9) >= 0.9.12
BuildRequires:  crate(parking-lot-core-0.9/default) >= 0.9.12
BuildRequires:  crate(pkg-config-0.3) >= 0.3.33
BuildRequires:  crate(piper-0.2/default) >= 0.2.0
BuildRequires:  crate(pin-project-lite-0.2) >= 0.2.17
BuildRequires:  crate(pin-project-lite-0.2/default) >= 0.2.17
BuildRequires:  crate(glob-0.3) >= 0.3.3
BuildRequires:  crate(glob-0.3/default) >= 0.3.3
BuildRequires:  crate(pnet-0.35) >= 0.35.0
BuildRequires:  crate(pnet-0.35/default) >= 0.35.0
BuildRequires:  crate(proptest-1/default) >= 1.0.0
BuildRequires:  crate(proc-macro-crate-3) >= 3.5.0
BuildRequires:  crate(proc-macro2-1) >= 1.0.106
BuildRequires:  crate(proc-macro2-1/default) >= 1.0.106
BuildRequires:  crate(proc-macro2-1/proc-macro) >= 1.0.106
BuildRequires:  crate(quote-1) >= 1.0.45
BuildRequires:  crate(quote-1/default) >= 1.0.45
BuildRequires:  crate(quote-1/proc-macro) >= 1.0.45
BuildRequires:  crate(remain-0.2) >= 0.2.15
BuildRequires:  crate(remain-0.2/default) >= 0.2.15
BuildRequires:  crate(range-map-vec-0.2) >= 0.2.0
BuildRequires:  crate(range-map-vec-0.2/default) >= 0.2.0
BuildRequires:  crate(rand-0.10) >= 0.10.1
BuildRequires:  crate(rand-0.10/alloc) >= 0.10.1
BuildRequires:  crate(rand-0.10/default) >= 0.10.1
BuildRequires:  crate(rand-0.10/std) >= 0.10.1
BuildRequires:  crate(rand-0.10/std-rng) >= 0.10.1
BuildRequires:  crate(rand-0.10/sys-rng) >= 0.10.1
BuildRequires:  crate(rand-0.10/thread-rng) >= 0.10.1
BuildRequires:  crate(rand-core-0.10) >= 0.10.1
BuildRequires:  crate(regex-1) >= 1.12.3
BuildRequires:  crate(regex-1/perf) >= 1.12.3
BuildRequires:  crate(regex-1/perf-backtrack) >= 1.12.3
BuildRequires:  crate(regex-1/perf-cache) >= 1.12.3
BuildRequires:  crate(regex-1/perf-dfa) >= 1.12.3
BuildRequires:  crate(regex-1/perf-inline) >= 1.12.3
BuildRequires:  crate(regex-1/perf-literal) >= 1.12.3
BuildRequires:  crate(regex-1/perf-onepass) >= 1.12.3
BuildRequires:  crate(regex-1/std) >= 1.12.3
BuildRequires:  crate(regex-automata-0.4) >= 0.4.14
BuildRequires:  crate(regex-automata-0.4/alloc) >= 0.4.14
BuildRequires:  crate(regex-automata-0.4/dfa-onepass) >= 0.4.14
BuildRequires:  crate(regex-automata-0.4/hybrid) >= 0.4.14
BuildRequires:  crate(regex-automata-0.4/meta) >= 0.4.14
BuildRequires:  crate(regex-automata-0.4/nfa-backtrack) >= 0.4.14
BuildRequires:  crate(regex-automata-0.4/nfa-pikevm) >= 0.4.14
BuildRequires:  crate(regex-automata-0.4/nfa-thompson) >= 0.4.14
BuildRequires:  crate(regex-automata-0.4/perf-inline) >= 0.4.14
BuildRequires:  crate(regex-automata-0.4/perf-literal) >= 0.4.14
BuildRequires:  crate(regex-automata-0.4/perf-literal-multisubstring) >= 0.4.14
BuildRequires:  crate(regex-automata-0.4/perf-literal-substring) >= 0.4.14
BuildRequires:  crate(regex-automata-0.4/std) >= 0.4.14
BuildRequires:  crate(regex-automata-0.4/syntax) >= 0.4.14
BuildRequires:  crate(regex-syntax-0.8) >= 0.8.10
BuildRequires:  crate(regex-syntax-0.8/std) >= 0.8.10
BuildRequires:  crate(rustix-1) >= 1.1.4
BuildRequires:  crate(rustix-1/alloc) >= 1.1.4
BuildRequires:  crate(rustix-1/default) >= 1.1.4
BuildRequires:  crate(rustix-1/std) >= 1.1.4
BuildRequires:  crate(rustix-1/termios) >= 1.1.4
BuildRequires:  crate(scopeguard-1) >= 1.2.0
BuildRequires:  crate(seccompiler-0.5) >= 0.5.0
BuildRequires:  crate(serde-1) >= 1.0.228
BuildRequires:  crate(serde-1/default) >= 1.0.228
BuildRequires:  crate(serde-1/derive) >= 1.0.228
BuildRequires:  crate(serde-1/rc) >= 1.0.228
BuildRequires:  crate(serde-1/serde-derive) >= 1.0.228
BuildRequires:  crate(serde-1/std) >= 1.0.228
BuildRequires:  crate(serde-core-1) >= 1.0.228
BuildRequires:  crate(serde-core-1/rc) >= 1.0.228
BuildRequires:  crate(serde-core-1/result) >= 1.0.228
BuildRequires:  crate(serde-core-1/std) >= 1.0.228
BuildRequires:  crate(serde-json-1) >= 1.0.150
BuildRequires:  crate(serde-json-1/default) >= 1.0.150
BuildRequires:  crate(serde-json-1/std) >= 1.0.150
BuildRequires:  crate(serde-repr-0.1) >= 0.1.20
BuildRequires:  crate(serde-repr-0.1/default) >= 0.1.20
BuildRequires:  crate(serde-with-3) >= 3.20.0
BuildRequires:  crate(serde-with-3/macros) >= 3.20.0
BuildRequires:  crate(sha2-0.11) >= 0.11.0
BuildRequires:  crate(sha2-0.11/alloc) >= 0.11.0
BuildRequires:  crate(sha2-0.11/default) >= 0.11.0
BuildRequires:  crate(sha2-0.11/oid) >= 0.11.0
BuildRequires:  crate(ssh2-0.9) >= 0.9.5
BuildRequires:  crate(ssh2-0.9/default) >= 0.9.5
BuildRequires:  crate(ssh2-0.9/vendored-openssl) >= 0.9.5
BuildRequires:  crate(shlex-2) >= 2.0.1
BuildRequires:  crate(shlex-2/default) >= 2.0.1
BuildRequires:  crate(shlex-2/std) >= 2.0.1
BuildRequires:  crate(signal-hook-0.4) >= 0.4.4
BuildRequires:  crate(signal-hook-0.4/channel) >= 0.4.4
BuildRequires:  crate(signal-hook-0.4/default) >= 0.4.4
BuildRequires:  crate(signal-hook-0.4/iterator) >= 0.4.4
BuildRequires:  crate(signal-hook-registry-1) >= 1.4.8
BuildRequires:  crate(simd-adler32-0.3) >= 0.3.9
BuildRequires:  crate(smallvec-1) >= 1.15.1
BuildRequires:  crate(spin-0.9) >= 0.9.8
BuildRequires:  crate(spin-0.9/barrier) >= 0.9.8
BuildRequires:  crate(spin-0.9/default) >= 0.9.8
BuildRequires:  crate(spin-0.9/lazy) >= 0.9.8
BuildRequires:  crate(spin-0.9/lock-api) >= 0.9.8
BuildRequires:  crate(spin-0.9/lock-api-crate) >= 0.9.8
BuildRequires:  crate(spin-0.9/mutex) >= 0.9.8
BuildRequires:  crate(spin-0.9/once) >= 0.9.8
BuildRequires:  crate(spin-0.9/rwlock) >= 0.9.8
BuildRequires:  crate(spin-0.9/spin-mutex) >= 0.9.8
BuildRequires:  crate(strsim-0.11) >= 0.11.1
BuildRequires:  crate(syn-2) >= 2.0.117
BuildRequires:  crate(syn-2/clone-impls) >= 2.0.117
BuildRequires:  crate(syn-2/default) >= 2.0.117
BuildRequires:  crate(syn-2/derive) >= 2.0.117
BuildRequires:  crate(syn-2/extra-traits) >= 2.0.117
BuildRequires:  crate(syn-2/full) >= 2.0.117
BuildRequires:  crate(syn-2/parsing) >= 2.0.117
BuildRequires:  crate(syn-2/printing) >= 2.0.117
BuildRequires:  crate(syn-2/proc-macro) >= 2.0.117
BuildRequires:  crate(syn-2/visit-mut) >= 2.0.117
BuildRequires:  crate(terminal-size-0.4) >= 0.4.4
BuildRequires:  crate(thousands-0.2) >= 0.2.0
BuildRequires:  crate(thousands-0.2/default) >= 0.2.0
BuildRequires:  crate(thiserror-2) >= 2.0.18
BuildRequires:  crate(thiserror-2/default) >= 2.0.18
BuildRequires:  crate(thiserror-2/std) >= 2.0.18
BuildRequires:  crate(toml-datetime-1) >= 1.1.1+spec-1.1.0
BuildRequires:  crate(toml-datetime-1/alloc) >= 1.1.1+spec-1.1.0
BuildRequires:  crate(toml-datetime-1/default) >= 1.1.1+spec-1.1.0
BuildRequires:  crate(toml-datetime-1/std) >= 1.1.1+spec-1.1.0
BuildRequires:  crate(toml-edit-0.25) >= 0.25.12+spec-1.1.0
BuildRequires:  crate(toml-edit-0.25/parse) >= 0.25.12+spec-1.1.0
BuildRequires:  crate(toml-parser-1) >= 1.1.2+spec-1.1.0
BuildRequires:  crate(toml-parser-1/alloc) >= 1.1.2+spec-1.1.0
BuildRequires:  crate(toml-parser-1/default) >= 1.1.2+spec-1.1.0
BuildRequires:  crate(toml-parser-1/std) >= 1.1.2+spec-1.1.0
BuildRequires:  crate(typenum-1) >= 1.20.1
BuildRequires:  crate(typenum-1/const-generics) >= 1.20.1
BuildRequires:  crate(unicode-ident-1) >= 1.0.24
BuildRequires:  crate(utf8parse-0.2) >= 0.2.2
BuildRequires:  crate(utf8parse-0.2/default) >= 0.2.2
BuildRequires:  crate(uuid-1) >= 1.23.2
BuildRequires:  crate(uuid-1/default) >= 1.23.2
BuildRequires:  crate(uuid-1/fast-rng) >= 1.23.2
BuildRequires:  crate(uuid-1/rng) >= 1.23.2
BuildRequires:  crate(uuid-1/std) >= 1.23.2
BuildRequires:  crate(uuid-1/v4) >= 1.23.2
BuildRequires:  crate(vcpkg-0.2) >= 0.2.15
BuildRequires:  crate(vcpkg-0.2/default) >= 0.2.15
BuildRequires:  crate(vfio-bindings-0.6) >= 0.6.2
BuildRequires:  crate(vfio-bindings-0.6/fam-wrappers) >= 0.6.2
BuildRequires:  crate(vfio-bindings-0.6/vmm-sys-util) >= 0.6.2
BuildRequires:  crate(vfio-ioctls-0.6) >= 0.6.0
BuildRequires:  crate(vfio-ioctls-0.6/iommufd-bindings) >= 0.6.0
BuildRequires:  crate(vfio-ioctls-0.6/iommufd-ioctls) >= 0.6.0
BuildRequires:  crate(vfio-ioctls-0.6/kvm) >= 0.6.0
BuildRequires:  crate(vfio-ioctls-0.6/kvm-bindings) >= 0.6.0
BuildRequires:  crate(vfio-ioctls-0.6/kvm-ioctls) >= 0.6.0
BuildRequires:  crate(vfio-ioctls-0.6/mshv) >= 0.6.0
BuildRequires:  crate(vfio-ioctls-0.6/mshv-bindings) >= 0.6.0
BuildRequires:  crate(vfio-ioctls-0.6/mshv-ioctls) >= 0.6.0
BuildRequires:  crate(vfio-ioctls-0.6/vfio-cdev) >= 0.6.0
BuildRequires:  crate(vfio-user-0.1) >= 0.1.3
BuildRequires:  crate(vhost-0.16) >= 0.16.0
BuildRequires:  crate(vhost-0.16/default) >= 0.16.0
BuildRequires:  crate(vhost-0.16/vhost-kern) >= 0.16.0
BuildRequires:  crate(vhost-0.16/vhost-user) >= 0.16.0
BuildRequires:  crate(vhost-0.16/vhost-user-backend) >= 0.16.0
BuildRequires:  crate(vhost-0.16/vhost-user-frontend) >= 0.16.0
BuildRequires:  crate(vhost-0.16/vhost-vdpa) >= 0.16.0
BuildRequires:  crate(vhost-user-backend-0.22) >= 0.22.0
BuildRequires:  crate(virtio-bindings-0.2) >= 0.2.7
BuildRequires:  crate(virtio-queue-0.17) >= 0.17.0
BuildRequires:  crate(vm-fdt-0.3) >= 0.3.0
BuildRequires:  crate(vm-fdt-0.3/default) >= 0.3.0
BuildRequires:  crate(vm-memory-0.17) >= 0.17.1
BuildRequires:  crate(vm-memory-0.17/arc-swap) >= 0.17.1
BuildRequires:  crate(vm-memory-0.17/backend-atomic) >= 0.17.1
BuildRequires:  crate(vm-memory-0.17/backend-bitmap) >= 0.17.1
BuildRequires:  crate(vm-memory-0.17/backend-mmap) >= 0.17.1
BuildRequires:  crate(vm-memory-0.17/default) >= 0.17.1
BuildRequires:  crate(vm-memory-0.17/rawfd) >= 0.17.1
BuildRequires:  crate(winapi-0.3) >= 0.3.9
BuildRequires:  crate(winapi-0.3/default) >= 0.3.9
BuildRequires:  crate(winapi-i686-pc-windows-gnu-0.4) >= 0.4.0
BuildRequires:  crate(winapi-i686-pc-windows-gnu-0.4/default) >= 0.4.0
BuildRequires:  crate(winapi-x86-64-pc-windows-gnu-0.4) >= 0.4.0
BuildRequires:  crate(winapi-x86-64-pc-windows-gnu-0.4/default) >= 0.4.0
BuildRequires:  crate(vmm-sys-util-0.15) >= 0.15.0
BuildRequires:  crate(vmm-sys-util-0.15/serde) >= 0.15.0
BuildRequires:  crate(vmm-sys-util-0.15/serde-derive) >= 0.15.0
BuildRequires:  crate(vmm-sys-util-0.15/with-serde) >= 0.15.0
BuildRequires:  crate(winnow-1) >= 1.0.3
BuildRequires:  crate(winnow-1/alloc) >= 1.0.3
BuildRequires:  crate(winnow-1/ascii) >= 1.0.3
BuildRequires:  crate(winnow-1/binary) >= 1.0.3
BuildRequires:  crate(winnow-1/default) >= 1.0.3
BuildRequires:  crate(winnow-1/parser) >= 1.0.3
BuildRequires:  crate(winnow-1/std) >= 1.0.3
BuildRequires:  crate(zerocopy-0.8) >= 0.8.50
BuildRequires:  crate(zerocopy-0.8/alloc) >= 0.8.50
BuildRequires:  crate(zerocopy-0.8/derive) >= 0.8.50
BuildRequires:  crate(zerocopy-0.8/zerocopy-derive) >= 0.8.50
BuildRequires:  crate(zbus-5) >= 5.15.0
BuildRequires:  crate(zbus-5/default) >= 5.15.0
BuildRequires:  crate(zbus-5/async-executor) >= 5.15.0
BuildRequires:  crate(zbus-5/async-io) >= 5.15.0
BuildRequires:  crate(zbus-5/async-lock) >= 5.15.0
BuildRequires:  crate(zbus-5/async-process) >= 5.15.0
BuildRequires:  crate(zbus-5/async-task) >= 5.15.0
BuildRequires:  crate(zbus-5/blocking) >= 5.15.0
BuildRequires:  crate(zbus-5/blocking-api) >= 5.15.0
BuildRequires:  crate(async-executor-1/default) >= 1.14.0
BuildRequires:  crate(async-io-2/default) >= 2.6.0
BuildRequires:  crate(async-lock-3/default) >= 3.4.2
BuildRequires:  crate(async-process-2/default) >= 2.5.0
BuildRequires:  crate(async-recursion-1/default) >= 1.1.1
BuildRequires:  crate(async-signal-0.2/default) >= 0.2.14
BuildRequires:  crate(async-task-4/default) >= 4.7.1
BuildRequires:  crate(async-trait-0.1/default) >= 0.1.89
BuildRequires:  crate(concurrent-queue-2/default) >= 2.5.0
BuildRequires:  crate(crossbeam-utils-0.8/default) >= 0.8.21
BuildRequires:  crate(event-listener-5/default) >= 5.4.1
BuildRequires:  crate(futures-io-0.3/default) >= 0.3.32
BuildRequires:  crate(futures-lite-2/default) >= 2.6.1
BuildRequires:  crate(futures-lite-2/std) >= 2.6.1
BuildRequires:  crate(hex-0.4/default) >= 0.4.3
BuildRequires:  crate(parking-2/default) >= 2.2.1
BuildRequires:  crate(polling-3/default) >= 3.11.0
BuildRequires:  crate(slab-0.4/default) >= 0.4.12
BuildRequires:  crate(tracing-0.1/default) >= 0.1.44
BuildRequires:  crate(tracing-core-0.1/default) >= 0.1.36
BuildRequires:  crate(tracing-attributes-0.1/default) >= 0.1.31
BuildRequires:  crate(windows-link-0.2) >= 0.2.1
BuildRequires:  crate(windows-sys-0.61/default) >= 0.61.2
BuildRequires:  crate(windows-sys-0.61/win32-foundation) >= 0.61.2
BuildRequires:  crate(uds-windows-1/default) >= 1.2.1
BuildRequires:  crate(zmij-1) >= 1.0.21
BuildRequires:  crate(zstd-0.13) >= 0.13.3
BuildRequires:  crate(zstd-0.13/arrays) >= 0.13.3
BuildRequires:  crate(zstd-0.13/default) >= 0.13.3
BuildRequires:  crate(zstd-0.13/legacy) >= 0.13.3
BuildRequires:  crate(zstd-0.13/zdict-builder) >= 0.13.3
BuildRequires:  crate(zstd-safe-7) >= 7.2.4
BuildRequires:  crate(zstd-safe-7/arrays) >= 7.2.4
BuildRequires:  crate(zstd-safe-7/legacy) >= 7.2.4
BuildRequires:  crate(zstd-safe-7/std) >= 7.2.4
BuildRequires:  crate(zstd-safe-7/zdict-builder) >= 7.2.4
BuildRequires:  crate(zstd-sys-2) >= 2.0.16+zstd.1.5.7
BuildRequires:  crate(zstd-sys-2/legacy) >= 2.0.16+zstd.1.5.7
BuildRequires:  crate(zstd-sys-2/std) >= 2.0.16+zstd.1.5.7
BuildRequires:  crate(zstd-sys-2/zdict-builder) >= 2.0.16+zstd.1.5.7

Requires:       bash
Requires:       glibc
Requires:       libcap

# TODO: Use rva23 rust toolchain to compile
%ifarch x86_64
%define rust_def_target x86_64-unknown-linux-gnu
%define cargo_pkg_feature_opts --no-default-features --features "mshv,kvm" -p cloud-hypervisor
%endif

%ifarch riscv64
%define rust_def_target riscv64gc-unknown-linux-gnu
%define cargo_pkg_feature_opts --no-default-features --features "kvm" -p cloud-hypervisor
%endif

%description
Cloud Hypervisor is an open source Virtual Machine Monitor (VMM) that runs on
top of KVM. The project focuses on exclusively running modern, cloud workloads,
on top of a limited set of hardware architectures and platforms. Cloud
workloads refers to those that are usually run by customers inside a cloud
provider. For our purposes this means modern Linux* distributions with most I/O
handled by paravirtualised devices (i.e. virtio), no requirement for legacy
devices and recent CPUs and KVM.

%prep
%setup -q -n %{name}-%{ch_commit}
# Extract micro-http git dependency to deps/
mkdir -p deps
tar -xf %{SOURCE1} -C deps/
# git+ archives extract to directory named after repo (no version suffix)
if [ -d deps/micro-http ]; then
  : # already exists
elif [ -d deps/micro-http-* ]; then
  mv deps/micro-http-* deps/micro-http
fi

# Create .cargo-checksum.json for git dependency
echo '{"files":{},"package":null}' > deps/micro-http/.cargo-checksum.json

# Patch Cargo.toml to use local path instead of git URL
# Note: vmm/Cargo.toml is in vmm/ subdirectory, so use ../deps/micro-http
sed -i 's|micro_http = { git = "https://github.com/firecracker-microvm/micro-http", branch = "main" }|micro_http = { path = "../deps/micro-http" }|' vmm/Cargo.toml
%rust_setup_registry

%build
rm -rf Cargo.lock
export OPENSSL_NO_VENDOR=1
cargo build --offline --release --target=%{rust_def_target} %{cargo_pkg_feature_opts}
cargo build --offline --release --target=%{rust_def_target} --package vhost_user_net
cargo build --offline --release --target=%{rust_def_target} --package vhost_user_block

%install
install -d %{buildroot}%{_bindir}
install -D -m755 target/%{rust_def_target}/release/cloud-hypervisor %{buildroot}%{_bindir}
install -D -m755 target/%{rust_def_target}/release/ch-remote %{buildroot}%{_bindir}
install -d %{buildroot}%{_libdir}/cloud-hypervisor
install -D -m755 target/%{rust_def_target}/release/vhost_user_block %{buildroot}%{_libdir}/cloud-hypervisor
install -D -m755 target/%{rust_def_target}/release/vhost_user_net %{buildroot}%{_libdir}/cloud-hypervisor

%files
%{_bindir}/ch-remote
%caps(cap_net_admin=ep) %{_bindir}/cloud-hypervisor
%dir %{_libdir}/cloud-hypervisor
%{_libdir}/cloud-hypervisor/vhost_user_block
%caps(cap_net_admin=ep) %{_libdir}/cloud-hypervisor/vhost_user_net
%license LICENSES/Apache-2.0.txt
%license LICENSES/BSD-3-Clause.txt
%license LICENSES/CC-BY-4.0.txt

%changelog
%autochangelog

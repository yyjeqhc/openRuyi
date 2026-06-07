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

#!RemoteAsset:  git+https://github.com/cloud-hypervisor/cloud-hypervisor.git#v%{version}
#!CreateArchive
Source0:        %{name}-%{version}.tar.gz

#!RemoteAsset:  git+https://github.com/firecracker-microvm/micro-http.git#876f3feccc30e09225f2c77bf95a6b2d46a9259e
#!CreateArchive
Source1:        micro-http.tar.gz

BuildSystem:    rust

BuildRequires:  rust-rpm-macros
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  binutils
BuildRequires:  pkgconfig(openssl)

# Disambiguate multi-version crates
BuildRequires:  crate(anstream-1)
BuildRequires:  crate(anstyle-parse-1)
BuildRequires:  crate(block-buffer-0.12)
BuildRequires:  crate(const-oid-0.10)
BuildRequires:  crate(crypto-common-0.2)
BuildRequires:  crate(digest-0.11)
BuildRequires:  crate(itertools-0.14)
BuildRequires:  crate(sha2-0.11)
BuildRequires:  crate(signal-hook-0.4)
BuildRequires:  crate(dirs-6)
BuildRequires:  crate(dirs-sys-0.5)
BuildRequires:  crate(redox-users-0.5)
BuildRequires:  crate(wasi-0.14)
BuildRequires:  crate(fdt-0.1)
BuildRequires:  crate(bitfield-struct-0.13)

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

%prep -a
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

%generate_buildrequires
%cargo_buildrequires

%build
rm -rf Cargo.lock
export OPENSSL_NO_VENDOR=1
cargo build --release --target=%{rust_def_target} %{cargo_pkg_feature_opts}
cargo build --release --target=%{rust_def_target} --package vhost_user_net
cargo build --release --target=%{rust_def_target} --package vhost_user_block

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

